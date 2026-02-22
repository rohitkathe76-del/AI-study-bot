<<<<<<< HEAD
# 🧠 AI Study Bot — Your Academic Co-Pilot

An intelligent AI-powered chatbot that answers academic questions and remembers your conversation history. Built with FastAPI, LangChain, Groq, and MongoDB — deployed on Render.

---

## 🌐 Live Demo
🔗[ **[https://ai-study-bot.onrender.com](https://ai-study-bot-u4tt.onrender.com)**]


---

## 📸 Preview

> A futuristic, student-friendly UI designed for everyday academic use.
> Ask questions on Math, Science, Programming, History, and more!

---

## ✨ Features

- 🤖 **AI-Powered Responses** — Uses Groq's LLaMA 3.1 for ultra-fast answers
- 🧠 **Memory** — Remembers your previous messages using MongoDB
- 📚 **Academic Focus** — Answers only study-related questions
- ⚡ **Fast & Free** — Groq inference is blazing fast
- 🎨 **Futuristic UI** — Student-friendly dark theme with quick topic chips
- 🔐 **Secure** — API keys stored safely via environment variables
- ☁️ **Cloud Deployed** — Live on Render, accessible from any device

---

## 🚀 Tech Stack

| Technology | Purpose |
|---|---|
| **FastAPI** | REST API backend |
| **LangChain** | LLM orchestration & prompt management |
| **Groq (LLaMA 3.1-8b-instant)** | Ultra-fast AI model inference |
| **MongoDB Atlas** | Persistent chat history storage |
| **Uvicorn** | ASGI server |
| **HTML/CSS/JS** | Frontend UI served via FastAPI |
| **Render** | Cloud deployment platform |

---

## 📁 Project Structure

```
AI-study-bot/
├── app.py              # FastAPI backend + chat logic
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignores .env and venv
├── .env                # Secret keys (never pushed to GitHub)
└── static/
    └── index.html      # Futuristic frontend UI
```

---

## ⚙️ How It Works

```
Student sends a question
        ↓
FastAPI /chat endpoint receives { user_id, question }
        ↓
MongoDB retrieves previous messages for that session
        ↓
LangChain builds prompt (system + history + new question)
        ↓
Groq LLaMA 3.1 generates a fast AI response
        ↓
MongoDB saves user message + bot response
        ↓
FastAPI returns response → displayed in UI
```

---

## 🛠️ Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/rohitkathe76-del/AI-study-bot.git
cd AI-study-bot
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` File
```
GROQ_API_KEY=your_groq_api_key_here
MONGODB_URI=your_mongodb_uri_here
```

### 5. Run the App
```bash
uvicorn app:app --reload
```

### 6. Open in Browser
```
http://127.0.0.1:8000
```

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Get from [console.groq.com](https://console.groq.com) |
| `MONGODB_URI` | Get from [cloud.mongodb.com](https://cloud.mongodb.com) |

---

## 📦 Dependencies

```
fastapi
uvicorn
langchain
langchain-groq
langchain_core
langchain_community
pymongo
python-multipart
python-dotenv
aiofiles
```

---

## ☁️ Deployment (Render)

1. Push code to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repository
4. Set Build Command: `pip install -r requirements.txt`
5. Set Start Command: `uvicorn app:app --host 0.0.0.0 --port 10000`
6. Add environment variables: `GROQ_API_KEY` and `MONGODB_URI`
7. Click Deploy!

---

## 📚 Supported Study Topics

- ⚙️ Physics
- 🌿 Biology  
- 📐 Mathematics
- 💻 Programming & Computer Science
- 🌍 History
- ⚗️ Chemistry
- 🤖 Artificial Intelligence & ML
- 🧬 General Science
- 📚 Study Tips & Techniques

---

## 🔒 Security

- API keys are stored in `.env` locally and Render's encrypted dashboard
- `.env` is excluded from GitHub via `.gitignore`
- No sensitive credentials are ever hardcoded in the source code

---

## 👨‍💻 Author

**Rohit Kathe**  
🔗 [GitHub](https://github.com/rohitkathe76-del)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).



> Built with ❤️ for students who want smarter ways to study.
=======
# 🧠 AI Study Bot — Your Academic Co-Pilot

An intelligent AI-powered chatbot that answers academic questions and remembers your conversation history. Built with FastAPI, LangChain, Groq, and MongoDB — deployed on Render.

---

## 🌐 Live Demo
🔗 **[https://ai-study-bot.onrender.com](https://ai-study-bot.onrender.com)**

---

## 📸 Preview

> A futuristic, student-friendly UI designed for everyday academic use.
> Ask questions on Math, Science, Programming, History, and more!

---

## ✨ Features

- 🤖 **AI-Powered Responses** — Uses Groq's LLaMA 3.1 for ultra-fast answers
- 🧠 **Memory** — Remembers your previous messages using MongoDB
- 📚 **Academic Focus** — Answers only study-related questions
- ⚡ **Fast & Free** — Groq inference is blazing fast
- 🎨 **Futuristic UI** — Student-friendly dark theme with quick topic chips
- 🔐 **Secure** — API keys stored safely via environment variables
- ☁️ **Cloud Deployed** — Live on Render, accessible from any device

---

## 🚀 Tech Stack

| Technology | Purpose |
|---|---|
| **FastAPI** | REST API backend |
| **LangChain** | LLM orchestration & prompt management |
| **Groq (LLaMA 3.1-8b-instant)** | Ultra-fast AI model inference |
| **MongoDB Atlas** | Persistent chat history storage |
| **Uvicorn** | ASGI server |
| **HTML/CSS/JS** | Frontend UI served via FastAPI |
| **Render** | Cloud deployment platform |

---

## 📁 Project Structure

```
AI-study-bot/
├── app.py              # FastAPI backend + chat logic
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignores .env and venv
├── .env                # Secret keys (never pushed to GitHub)
└── static/
    └── index.html      # Futuristic frontend UI
```

---

## ⚙️ How It Works

```
Student sends a question
        ↓
FastAPI /chat endpoint receives { user_id, question }
        ↓
MongoDB retrieves previous messages for that session
        ↓
LangChain builds prompt (system + history + new question)
        ↓
Groq LLaMA 3.1 generates a fast AI response
        ↓
MongoDB saves user message + bot response
        ↓
FastAPI returns response → displayed in UI
```

---

## 🛠️ Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/rohitkathe76-del/AI-study-bot.git
cd AI-study-bot
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` File
```
GROQ_API_KEY=your_groq_api_key_here
MONGODB_URI=your_mongodb_uri_here
```

### 5. Run the App
```bash
uvicorn app:app --reload
```

### 6. Open in Browser
```
http://127.0.0.1:8000
```

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Get from [console.groq.com](https://console.groq.com) |
| `MONGODB_URI` | Get from [cloud.mongodb.com](https://cloud.mongodb.com) |

---

## 📦 Dependencies

```
fastapi
uvicorn
langchain
langchain-groq
langchain_core
langchain_community
pymongo
python-multipart
python-dotenv
aiofiles
```

---

## ☁️ Deployment (Render)

1. Push code to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repository
4. Set Build Command: `pip install -r requirements.txt`
5. Set Start Command: `uvicorn app:app --host 0.0.0.0 --port 10000`
6. Add environment variables: `GROQ_API_KEY` and `MONGODB_URI`
7. Click Deploy!

---

## 📚 Supported Study Topics

- ⚙️ Physics
- 🌿 Biology  
- 📐 Mathematics
- 💻 Programming & Computer Science
- 🌍 History
- ⚗️ Chemistry
- 🤖 Artificial Intelligence & ML
- 🧬 General Science
- 📚 Study Tips & Techniques

---

## 🔒 Security

- API keys are stored in `.env` locally and Render's encrypted dashboard
- `.env` is excluded from GitHub via `.gitignore`
- No sensitive credentials are ever hardcoded in the source code

---

## 👨‍💻 Author

**Rohit Kathe**  
🔗 [GitHub](https://github.com/rohitkathe76-del)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> Built with ❤️ for students who want smarter ways to study.
>>>>>>> 5255450814dc716fa3d3dd35e4f6dbd1a28fe44d
