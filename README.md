markdown
# 🤖 AI Chatbot – Full-Stack Conversational Assistant

A full-stack chatbot application built with **React**, **Tailwind CSS**, and **JavaScript** on the frontend, and **Python** on the backend. It integrates with AI APIs to deliver intelligent, real-time responses in a sleek, responsive interface.

---

## 🚀 Features

- 💬 Real-time chat interface with user-friendly design
- 🧠 AI integration via OpenAI, Gemini, or Hugging Face APIs
- 🔐 Secure backend with environment-based API key handling
- 🌐 JSON-based communication between frontend and backend
- 🎨 Responsive UI styled with Tailwind CSS
- 📜 Message history and loading indicators

---

## 🛠 Tech Stack

- **Frontend**: React, JavaScript, HTML, Tailwind CSS
- **Backend**: Python (FastAPI or Flask)
- **API**: OpenAI / Gemini / Hugging Face (customizable)
- **Deployment**: Netlify (frontend), Render or Railway (backend)

---

## ▶️ How to Run

### 🔧 Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
set GEMINI_API_KEY=your_api_key_here  # PowerShell: $env:GEMINI_API_KEY="your_api_key_here"
python app.py
```

### 💻 Frontend

```bash
cd frontend
npm install
npm start
```

The backend reads `GEMINI_API_KEY` or `GOOGLE_API_KEY` from the environment. If the key is missing, `/api/chat` returns a clear configuration error instead of a raw server failure.
