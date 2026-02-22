import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pymongo import MongoClient
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
mongo_uri = os.getenv("MONGODB_URI")

# ✅ Changed database to "study_bot" and collection to "chat_history"
client = MongoClient(mongo_uri)
db = client["study_bot"]
collection = db["chat_history"]

app = FastAPI()

class chatRequest(BaseModel):
    user_id: str
    question: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# ✅ Serve the static folder (where index.html lives)
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ Changed system prompt to Study Bot
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an expert AI Study Assistant. Your job is to help students learn and understand academic topics clearly and effectively.

Guidelines:
- Answer only study-related and academic questions (e.g., science, math, history, programming, literature, etc.)
- If a question is NOT study-related, politely decline and redirect the user to ask academic questions.
- Always explain concepts step-by-step in a simple and easy-to-understand way.
- Use examples, analogies, or breakdowns where helpful.
- Encourage the student and keep a supportive, motivating tone.
- Remember previous messages in the conversation to give context-aware responses."""
        ),
        ("placeholder", "{history}"),
        ("user", "{question}"),
    ]
)

# ✅ Changed to a valid Groq model (llama3-8b-8192 is fast & free)
llm = ChatGroq(api_key=groq_api_key, model="llama-3.1-8b-instant")
chain = prompt | llm


def get_chat_history(user_id):
    chats = collection.find({"user_id": user_id}).sort("timestamp", -1).limit(10)
    history = []
    for chat in chats:
        history.append((chat["role"], chat["message"]))
    history.reverse()
    return history

# ✅ Serve index.html at root URL "/"
@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/chat")
def chat(request: chatRequest):
    history = get_chat_history(request.user_id)
    response = chain.invoke({"history": history, "question": request.question})

    # Save user message
    collection.insert_one({
        "user_id": request.user_id,
        "role": "user",
        "message": request.question,
        "timestamp": datetime.utcnow()
    })

    # Save bot response
    collection.insert_one({
        "user_id": request.user_id,
        "role": "assistant",
        "message": response.content,
        "timestamp": datetime.utcnow()
    })

    return {"message": response.content}