# 🤖 InterviewBot - AI-Powered Interview Preparation Platform

<div align="center">

![InterviewBot Banner](https://img.shields.io/badge/Interview-Bot-blue?style=for-the-badge)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org)
[![LangChain](https://img.shields.io/badge/🦜_LangChain-2C3E50?style=for-the-badge)](https://www.langchain.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com)

**An intelligent interview preparation platform powered by AI that helps job seekers prepare for interviews by generating personalized interview questions based on their resume.**

Built with FastAPI, LangChain, LangGraph, MongoDB, and React, this project demonstrates end-to-end skills in Python backend development, modern frontend integration, AI orchestration, and database handling.

[Features](#-features) • [Demo](#-live-demo) • [Architecture](#-system-architecture) • [Installation](#-installation--setup) • [API Documentation](#-api-documentation)

</div>

---

## 📑 Table of Contents

- [Features](#-features)
- [Live Demo](#-live-demo)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Chatbot Architecture](#-chatbot-architecture)
- [Installation & Setup](#-installation--setup)
- [Configuration](#-configuration)
- [Contributing](#-contributing)


---

## 🚀 Features

### 🤖 AI-Powered Chatbot Assistant
- **Intelligent Conversation**: Powered by Groq (Llama 3.3) and LangGraph for natural interactions
- **RAG-Based Responses**: Retrieval Augmented Generation using indexed website content
- **Contextual Help**: Real-time assistance during interviews without revealing answers
- **Multi-turn Setup**: Interactive questionnaire to configure personalized interviews
- **Chat History**: Persistent conversation storage with session management
- **Three Conversation Modes**:
  - **Normal Chat** - Answer questions about the platform using RAG
  - **Interview Setup** - Interactive multi-turn questionnaire
  - **Contextual Help** - Explanations during interviews

### 📄 Resume Upload & Parsing
- Upload resumes (PDF/Docx) which are parsed into structured JSON using LangChain
- Secure storage of parsed resumes in MongoDB
- Resume-based question generation

### 🎤 AI Interview Simulation
- **MCQ Tests**: Multiple choice question tests with various difficulty levels
- **Mock Interviews**: AI-conducted voice/text interviews with realistic scenarios
- **Technical & Behavioral**: Comprehensive coverage of different interview types
- **Role-Specific**: Customized questions based on target job roles
- **Company-Specific**: Questions tailored to target companies (FAANG, startups, etc.)

### 📊 Progress Tracking & Analytics
- **Dashboard**: Comprehensive performance metrics and insights
- **Score Tracking**: Detailed scoring for each interview session
- **PDF Reports**: Downloadable performance summaries
- **Progress Visualization**: Charts and graphs showing improvement

### 👤 User Management
- Secure JWT-based authentication
- Profile management
- Session history tracking

---

## 🌐 Live Demo

> **🚀 Try it now**: [https://frontend-pj-192c.vercel.app](https://frontend-pj-192c.vercel.app)

| Service | Live URL | API Docs |
|---------|----------|----------|
| **Frontend** (React + Vite) | [frontend-pj-192c.vercel.app](https://frontend-pj-192c.vercel.app) | — |
| **Main API** (FastAPI) | [interviewbot-api-j1zy.onrender.com](https://interviewbot-api-j1zy.onrender.com) | [Swagger UI](https://interviewbot-api-j1zy.onrender.com/docs) |
| **Chatbot API** (LangGraph) | [interviewbot-chatbot.onrender.com](https://interviewbot-chatbot.onrender.com) | [Swagger UI](https://interviewbot-chatbot.onrender.com/docs) |

### ☁️ Deployment Architecture

| Component | Platform |
|-----------|----------|
| Frontend (React + Vite) | Vercel |
| Main API (FastAPI + LangChain) | Render |
| Chatbot (FastAPI + LangGraph) | Render |
| Database | MongoDB Atlas |

> ⚠️ **Note**: Backends run on Render's free tier — the first request after ~15 min of inactivity may take **~50 seconds** while the server wakes up (cold start). Subsequent requests are fast.

---

## 🛠️ Tech Stack

### Backend Technologies

| Technology | Purpose | Version |
|------------|---------|---------|
| **FastAPI** | High-performance async API framework | 0.116+ |
| **LangGraph** | AI conversation flow and state management | 0.2+ |
| **LangChain** | LLM integration and orchestration | 0.3+ |
| **Groq (Llama 3.3)** | Large language model for AI responses | Latest |
| **Google Gemini** | Optional fallback LLM | 1.5+ |
| **ChromaDB** | Vector database for RAG implementation | 0.4+ |
| **MongoDB** | Database for user data and chat history | Latest |
| **Motor** | Async MongoDB driver | 3.7+ |
| **PyJWT** | JWT token authentication | 2.10+ |
| **PyPDF** | Resume PDF processing | 5.9+ |
| **ReportLab** | PDF report generation | 4.0+ |
| **ChromaDB Default Embeddings** | Text embeddings (ONNX MiniLM) | 1.0+ |
| **BeautifulSoup4** | Web scraping for content indexing | 4.12+ |
| **Passlib & Bcrypt** | Password hashing | 1.7.4 |

### Frontend Technologies

| Technology | Purpose | Version |
|------------|---------|---------|
| **React** | UI framework | 19.1+ |
| **Vite** | Build tool and dev server | 7.1+ |
| **Redux Toolkit** | State management | 2.8+ |
| **React Router** | Client-side routing | 7.8+ |
| **Tailwind CSS** | Utility-first styling | 4.1+ |
| **Radix UI** | Accessible component primitives | Latest |
| **React Hook Form** | Form handling | 7.62+ |
| **Lucide React** | Icon library | 0.540+ |
| **React Speech Recognition** | Voice input for interviews | 4.0+ |
| **React Toastify** | Toast notifications | 11.0+ |

### AI & ML Stack
- **Groq (Llama 3.3 70B)** - Main LLM for chatbot and question generation
- **Google Gemini** - Optional fallback LLM
- **all-MiniLM-L6-v2 (ONNX via ChromaDB)** - Sentence embeddings for RAG
- **ChromaDB** - Vector similarity search
- **LangGraph** - Stateful conversation graphs
- **LangChain** - LLM orchestration and tools



### Data Flow Diagram

```
┌──────────────┐
│     USER     │
└──────┬───────┘
       │
       ├─────────────────────────────────────────────────┐
       │                                                 │
       ▼                                                 ▼
┌─────────────────┐                             ┌─────────────────┐
│ Upload Resume   │                             │  Start Chat     │
└────────┬────────┘                             └────────┬────────┘
         │                                               │
         ▼                                               ▼
┌─────────────────┐                             ┌─────────────────┐
│ Parse PDF       │                             │ Send Message    │
│ (PyPDF/         │                             │ to Chatbot      │
│  LangChain)     │                             └────────┬────────┘
└────────┬────────┘                                      │
         │                                               ▼
         ▼                                     ┌──────────────────────┐
┌─────────────────┐                           │ LangGraph Workflow   │
│ Extract Skills  │                           │ • Intent Detection   │
│ & Experience    │                           │ • Mode Routing       │
└────────┬────────┘                           │ • State Update       │
         │                                    └────────┬─────────────┘
         │                                             │
         │                                    ┌────────┴────────┐
         │                                    │                 │
         │                                    ▼                 ▼
         │                          ┌─────────────┐   ┌──────────────┐
         │                          │ RAG Search  │   │ Multi-turn   │
         │                          │ (ChromaDB)  │   │ Dialogue     │
         │                          └─────────────┘   └──────────────┘
         │                                    │                 │
         │                                    └────────┬────────┘
         │                                             │
         ▼                                             ▼
┌─────────────────┐                          ┌─────────────────┐
│ Store in        │                          │ Generate        │
│ MongoDB         │                          │ Response        │
│ (Resume DB)     │                          │ (Groq LLM)      │
└────────┬────────┘                          └────────┬────────┘
         │                                            │
         │                                            ▼
         │                                   ┌─────────────────┐
         │                                   │ Save to Chat    │
         │                                   │ History         │
         │                                   └────────┬────────┘
         │                                            │
         └────────────┬───────────────────────────────┘
                      │
                      ▼
            ┌──────────────────┐
            │ Start Interview  │
            └────────┬─────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
         ▼                       ▼
┌──────────────────┐    ┌─────────────────┐
│  MCQ Test        │    │  Mock Interview │
│  • Time-bound    │    │  • AI Questions │
│  • Auto-score    │    │  • Voice/Text   │
└────────┬─────────┘    └────────┬────────┘
         │                       │
         └───────────┬───────────┘
                     │
                     ▼
            ┌──────────────────┐
            │ Generate Report  │
            │ (ReportLab PDF)  │
            └────────┬─────────┘
                     │
                     ▼
            ┌──────────────────┐
            │ Store Results    │
            │ (MongoDB)        │
            └────────┬─────────┘
                     │
                     ▼
            ┌──────────────────┐
            │ Display on       │
            │ Dashboard        │
            └──────────────────┘
```

---

## 📁 Project Structure

```
interview-bot/
│
├── backend/                        # Main FastAPI Application (Port 8000)
│   ├── connections/               # Database connection modules
│   │   └── mongodb.py            # MongoDB connection setup
│   │
│   ├── models/                    # Pydantic models & schemas
│   │   ├── auth.py               # User authentication models
│   │   ├── schemas.py            # Request/response schemas
│   │   └── __init__.py
│   │
│   ├── routers/                   # API route handlers
│   │   ├── auth.py               # Authentication endpoints
│   │   │   • POST /signup        # User registration
│   │   │   • POST /login         # User login
│   │   │   • GET /me             # Get current user
│   │   │
│   │   ├── bot.py                # Interview bot endpoints
│   │   │   • POST /parse-resume  # Upload & parse resume
│   │   │   • POST /generate-questions  # Generate interview questions
│   │   │   • POST /start-interview  # Start interview session
│   │   │   • POST /submit-answer    # Submit MCQ answer
│   │   │
│   │   ├── mock.py               # Mock interview endpoints
│   │   │   • POST /start-mock    # Start mock interview
│   │   │   • POST /next-question # Get next mock question
│   │   │   • POST /submit-response  # Submit response
│   │   │   • GET /mock-feedback  # Get interview feedback
│   │   │
│   │   ├── dashboard.py          # Analytics endpoints
│   │   │   • GET /stats          # Get user statistics
│   │   │   • GET /recent-tests   # Get recent test history
│   │   │   • GET /download-report  # Download PDF report
│   │   │
│   │   ├── main_router.py        # General utility endpoints
│   │   │   • GET /health         # Health check
│   │   │   • POST /contact       # Contact form
│   │   │
│   │   └── __init__.py
│   │
│   ├── utils/                     # Utility functions
│   │   ├── exception.py          # Custom exception handlers
│   │   ├── logger.py             # Logging configuration
│   │   ├── main_utils.py         # Common utility functions
│   │   ├── prompts.py            # LLM prompt templates
│   │   └── __init__.py
│   │
│   ├── main.py                    # FastAPI application entry point
│   ├── validate_env.py            # Environment variable validation
│   ├── verify_setup.py            # Setup verification script
│   ├── requirements.txt           # Python dependencies
│   ├── pyproject.toml            # UV package manager config
│   ├── uv.lock                   # Dependency lock file
│   ├── .env                      # Environment variables
│   ├── .gitignore
│   └── README.md
│
├── chatbot/                       # AI Chatbot Microservice (Port 8001)
│   ├── backend/
│   │   ├── langgraph_agent/      # LangGraph conversation agent
│   │   │   ├── state.py          # Conversation state definitions
│   │   │   │   • ChatState class
│   │   │   │   • Message models
│   │   │   │   • Interview parameters
│   │   │   │
│   │   │   ├── nodes.py          # LangGraph node functions
│   │   │   │   • intent_detection_node()
│   │   │   │   • normal_chat_node()
│   │   │   │   • setup_interview_node()
│   │   │   │   • contextual_help_node()
│   │   │   │
│   │   │   ├── graph.py          # LangGraph workflow definition
│   │   │   │   • create_graph()
│   │   │   │   • State transitions
│   │   │   │   • Conditional routing
│   │   │   │
│   │   │   ├── knowledge_base.py # RAG implementation
│   │   │   │   • Website content scraping
│   │   │   │   • Text chunking & embedding
│   │   │   │   • ChromaDB vector storage
│   │   │   │   • Semantic search
│   │   │   │
│   │   │   └── __init__.py
│   │   │
│   │   ├── database.py           # MongoDB client for chatbot
│   │   ├── main.py              # Chatbot FastAPI app
│   │   │   • POST /chat          # Main chat endpoint
│   │   │   • GET /sessions/{user_id}  # Get user sessions
│   │   │   • GET /history/{user_id}/{session_id}  # Get chat history
│   │   │   • DELETE /session/{user_id}/{session_id}  # Delete session
│   │   │   • POST /index-website  # Re-index website content
│   │   │
│   │   ├── page_capture.py       # Website scraping utility
│   │   ├── run_indexing.py       # Manual indexing script
│   │   ├── test_chatbot.py       # Chatbot test suite
│   │   ├── verify_chatbot.py     # Chatbot verification
│   │   ├── requirements.txt      # Chatbot dependencies
│   │   ├── .env                  # Chatbot environment vars
│   │   └── .env.example
│   │
│   ├── ARCHITECTURE.md           # Detailed chatbot architecture
│   ├── QUICKSTART.md            # Quick setup guide
│   └── README.md                # Chatbot documentation
│
├── frontend/                      # React Application (Port 5173)
│   ├── src/
│   │   ├── assets/               # Static assets (images, icons)
│   │   │
│   │   ├── components/           # Reusable UI components
│   │   │   ├── ui/              # Radix UI components
│   │   │   │   ├── button.jsx
│   │   │   │   ├── card.jsx
│   │   │   │   ├── dialog.jsx
│   │   │   │   └── ...
│   │   │   ├── Chatbot.jsx      # Floating chat widget
│   │   │   ├── Chatbot.css      # Chat widget styles
│   │   │   ├── Header.jsx       # Site header
│   │   │   ├── Footer.jsx       # Site footer
│   │   │   └── ...
│   │   │
│   │   ├── features/            # Feature-specific components
│   │   │   ├── auth/           # Authentication features
│   │   │   ├── interview/      # Interview features
│   │   │   └── dashboard/      # Dashboard features
│   │   │
│   │   ├── hooks/               # Custom React hooks
│   │   │   ├── useAuth.js      # Authentication hook
│   │   │   ├── useInterview.js # Interview hook
│   │   │   └── ...
│   │   │
│   │   ├── layout/              # Layout components
│   │   │   ├── RootLayout.jsx  # Main layout wrapper
│   │   │   ├── AuthLayout.jsx  # Auth pages layout
│   │   │   └── DashboardLayout.jsx  # Dashboard layout
│   │   │
│   │   ├── lib/                 # Utility libraries
│   │   │   └── utils.js        # Helper functions
│   │   │
│   │   ├── pages/               # Page components
│   │   │   ├── Home.jsx        # Landing page
│   │   │   ├── Login.jsx       # Login page
│   │   │   ├── Signup.jsx      # Registration page
│   │   │   ├── Dashboard.jsx   # User dashboard
│   │   │   ├── TestPage.jsx    # MCQ test page
│   │   │   ├── MockPage.jsx    # Mock interview page
│   │   │   └── ...
│   │   │
│   │   ├── services/            # API service layer
│   │   │   ├── api.js          # Axios instance
│   │   │   ├── authService.js  # Auth API calls
│   │   │   ├── botService.js   # Interview API calls
│   │   │   └── chatService.js  # Chatbot API calls
│   │   │
│   │   ├── store/               # Redux store
│   │   │   ├── store.js        # Store configuration
│   │   │   ├── slices/         # Redux slices
│   │   │   │   ├── authSlice.js
│   │   │   │   ├── interviewSlice.js
│   │   │   │   └── chatSlice.js
│   │   │   └── index.js
│   │   │
│   │   ├── main.jsx            # App entry point
│   │   └── styles.css          # Global styles
│   │
│   ├── public/                  # Public static files
│   ├── index.html              # HTML template
│   ├── package.json            # NPM dependencies
│   ├── vite.config.js          # Vite configuration
│   ├── tailwind.config.js      # Tailwind CSS config
│   ├── components.json         # shadcn/ui config
│   ├── .env                    # Frontend environment vars
│   └── .gitignore
│
├── index_website.py             # Website indexing CLI tool
├── test_knowledge.py           # Chatbot knowledge testing
├── DASHBOARD_FIX_NOTE.js       # Dashboard fix notes
├── INDEX_WEBSITE.bat           # Windows batch script
├── INSTALL_REPORTLAB.bat       # ReportLab installer
├── README.md                   # Main project README (this file)
├── .gitignore
└── LICENSE
```



## 🤖 Chatbot Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                          USER INTERFACE                          │
│                         (React Frontend)                         │
│                                                                   │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  Floating Chat Widget (Chatbot.jsx)                    │    │
│  │  • Message display                                      │    │
│  │  • Input textarea                                       │    │
│  │  • Session management                                   │    │
│  │  • Interview launch button                              │    │
│  └────────────────────────────────────────────────────────┘    │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            │ HTTP POST /chat
                            │ {user_id, message, session_id}
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                       CHATBOT BACKEND                            │
│                      (FastAPI + LangGraph)                       │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    main.py (API)                          │  │
│  │  • /chat endpoint                                         │  │
│  │  • Load conversation state                                │  │
│  │  • Invoke LangGraph                                       │  │
│  │  • Save to MongoDB                                        │  │
│  └─────────────────────┬────────────────────────────────────┘  │
│                        │                                         │
│                        ▼                                         │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              LangGraph Workflow (graph.py)                │  │
│  │                                                            │  │
│  │    ┌─────────────────────────────────────────┐           │  │
│  │    │    Intent Detection Node                 │           │  │
│  │    │  • Classify user message                 │           │  │
│  │    │  • Route to appropriate mode             │           │  │
│  │    └──────────┬──────────────────────────────┘           │  │
│  │               │                                            │  │
│  │      ┌────────┴────────┬──────────────┐                  │  │
│  │      │                 │              │                   │  │
│  │      ▼                 ▼              ▼                   │  │
│  │  ┌────────┐      ┌─────────┐    ┌──────────┐            │  │
│  │  │ Normal │      │  Setup  │    │   Help   │            │  │
│  │  │  Chat  │      │Interview│    │Contextual│            │  │
│  │  │  Node  │      │   Node  │    │   Node   │            │  │
│  │  └───┬────┘      └────┬────┘    └────┬─────┘            │  │
│  │      │                │              │                   │  │
│  │      │                │              │                   │  │
│  │      └────────┬───────┴────────┬─────┘                  │  │
│  │               │                │                          │  │
│  │               ▼                ▼                          │  │
│  │      ┌─────────────┐  ┌──────────────┐                  │  │
│  │      │  RAG Search │  │Multi-turn Q&A│                  │  │
│  │      │ (ChromaDB)  │  │  State Mgmt  │                  │  │
│  │      └─────────────┘  └──────────────┘                  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │           Groq LLM (nodes.py)                              │  │
│  │  • Intent classification                                  │  │
│  │  • Response generation                                    │  │
│  │  • Context understanding                                  │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────┬──────────────────────────┬───────────────────┘
                 │                          │
                 ▼                          ▼
    ┌──────────────────────┐    ┌────────────────────────┐
    │   ChromaDB           │    │   MongoDB              │
    │   (Vector Store)     │    │   (Chat History)       │
    │                      │    │                        │
    │  • Website content   │    │  • Messages            │
    │  • Text embeddings   │    │  • Sessions            │
    │  • Semantic search   │    │  • Conversation state  │
    └──────────────────────┘    └────────────────────────┘
```

### Conversation Flow

#### 1. Normal Chat (RAG-based)
```
User: "How do I upload my resume?"
    ↓
Intent Detection → "normal"
    ↓
Search ChromaDB for relevant content
    ↓
Retrieve top matching documents
    ↓
Generate response using context + Groq
    ↓
Return answer: "To upload your resume, go to..."
```

#### 2. Interview Setup (Multi-turn Dialogue)
```
User: "I want to start an interview"
    ↓
Intent Detection → "setup"
    ↓
Check current setup_step in state
    ↓
Ask next question in sequence:
  Step 1: "Would you like MCQ or Mock interview?"
  Step 2: "What type? (Technical/Behavioral/HR/Mixed)"
  Step 3: "What role are you preparing for?"
  Step 4: "What difficulty level? (Easy/Medium/Hard)"
  Step 5: "How many questions?"
  Step 6: "Any target companies? (e.g., FAANG)"
  Step 7: "Ready to start?"
    ↓
Collect answer → Save to state.interview_params
    ↓
Move to next step
    ↓
When complete (all steps done):
  Return interview_params + should_launch_interview=true
```

#### 3. Contextual Help During Interview
```
User is in interview with question: "Explain REST API"
User asks in chat: "What is REST?"
    ↓
Intent Detection → "help"
    ↓
Get current_question from state
    ↓
Search knowledge base + use interview context
    ↓
Generate helpful explanation (no direct answer)
    ↓
Return: "REST stands for Representational State Transfer..."
```





## ⚙️ Installation & Setup

### Prerequisites

- **Python**: 3.9 or higher
- **Node.js**: 16.x or higher
- **MongoDB**: Atlas account (free tier works)
- **Groq**: Free API key from [console.groq.com](https://console.groq.com/keys)

### Step 1: Clone the Repository

```bash
git clone https://github.com/prathamj560-del/Interview-Bot.git
cd Interview-Bot
```

### Step 2: Backend Setup (Main API)

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies using uv (recommended)
pip install uv
uv sync

# Or install with pip
pip install -r requirements.txt

# Create .env file
cp .env.example .env
```

Edit `backend/.env`:
```env
MONGODB_URL="mongodb+srv://username:password@cluster.mongodb.net/"
GROQ_API_KEY="your-groq-api-key"
MONGODB_DATABASE_NAME="InterviewBot"
JWT_SECRET_KEY="your-secret-key-minimum-32-characters-long"
JWT_ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Step 3: Chatbot Backend Setup

```bash
cd ../chatbot/backend

# Install chatbot dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
```

Edit `chatbot/backend/.env`:
```env
GROQ_API_KEY="your-groq-api-key"
MONGODB_URL="mongodb+srv://username:password@cluster.mongodb.net/"
MONGODB_DATABASE_NAME="InterviewBot"
WEBSITE_BASE_URL="http://localhost:5173"
```

**Important**: Index website content (one-time setup)
```bash
# Make sure frontend is running first, then:
python -m langgraph_agent.knowledge_base
```

### Step 4: Frontend Setup

```bash
cd ../../frontend

# Install dependencies
npm install

# Create .env file
cp .env.example .env
```

Edit `frontend/.env`:
```env
VITE_BASE_URL="http://localhost:8000"
VITE_CHATBOT_URL="http://localhost:8001"
```

### Step 5: Running the Application

You need **three terminals** running simultaneously:

**Terminal 1 - Main Backend:**
```bash
cd backend
uv run uvicorn main:app --reload --port 8000
# Or with regular Python:
# uvicorn main:app --reload --port 8000
```
Backend runs at: `http://localhost:8000`

**Terminal 2 - Chatbot Backend:**
```bash
cd chatbot/backend
python main.py
```
Chatbot runs at: `http://localhost:8001`

**Terminal 3 - Frontend:**
```bash
cd frontend
npm run dev
```
Frontend runs at: `http://localhost:5173`

### Step 6: Verify Setup

Visit `http://localhost:5173` in your browser. You should see the InterviewBot landing page.

---




## 🔧 Configuration

### Environment Variables

#### Backend `.env`
```env
# MongoDB Configuration
MONGODB_URL="mongodb+srv://username:password@cluster.mongodb.net/"
MONGODB_DATABASE_NAME="InterviewBot"

# LLM API (Groq — free key at console.groq.com)
GROQ_API_KEY="your-groq-api-key"

# JWT Configuration
JWT_SECRET_KEY="your-very-long-secret-key-minimum-32-characters"
JWT_ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Optional: CORS Origins
CORS_ORIGINS="http://localhost:5173,http://localhost:3000"
```

#### Chatbot Backend `.env`
```env
# LLM API (Groq — free key at console.groq.com)
GROQ_API_KEY="your-groq-api-key"

# MongoDB Configuration
MONGODB_URL="mongodb+srv://username:password@cluster.mongodb.net/"
MONGODB_DATABASE_NAME="InterviewBot"

# Website Configuration
WEBSITE_BASE_URL="http://localhost:5173"

# ChromaDB Configuration (optional)
CHROMA_DB_PATH="./chroma_db"
```

#### Frontend `.env`
```env
# API Endpoints
VITE_BASE_URL="http://localhost:8000"
VITE_CHATBOT_URL="http://localhost:8001"

# Optional: Analytics
VITE_GA_TRACKING_ID="your-google-analytics-id"
```


---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute

1. **Report Bugs**: Open an issue with detailed reproduction steps
2. **Suggest Features**: Share your ideas for new features
3. **Improve Documentation**: Help make docs clearer
4. **Write Code**: Submit pull requests for bug fixes or features
5. **Test**: Help test new features and report issues

### Contribution Process

1. **Fork the repository**
```bash
git clone https://github.com/yourusername/Interview-Bot.git
cd Interview-Bot
```

2. **Create a feature branch**
```bash
git checkout -b feature/AmazingFeature
```

3. **Make your changes**
```bash
# Write code
# Add tests
# Update documentation
```

4. **Commit your changes**
```bash
git add .
git commit -m 'Add some AmazingFeature'
```

5. **Push to the branch**
```bash
git push origin feature/AmazingFeature
```

6. **Open a Pull Request**
- Go to GitHub repository
- Click "New Pull Request"
- Describe your changes
- Wait for review## 👥 Author

<table>
<tr>
<td align="center">

<h3>Pratham Jain</h3>
<p>
<a href="mailto:prathamj560@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white" /></a>
<a href="https://www.linkedin.com/in/pratham-jain-377875292/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white" /></a>
<a href="https://github.com/prathamj560-del"><img src="https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white" /></a>
</p>
</td>
</tr>
</table>
