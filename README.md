# Smart Task Planner

An AI-powered planner that breaks user goals into actionable tasks with dependencies and time estimates.

## Features
• AI-driven reasoning (OpenAI GPT-4o / Ollama)
• FastAPI backend with structured API
• Next.js frontend + TailwindCSS UI
• Optional SQLite persistence
• Docker-ready environment

## Setup
1. Backend  
   `cd backend`  
   `pip install -r requirements.txt`  
   `uvicorn app.main:app --reload`

2. Frontend  
   `cd frontend`  
   `npm install`  
   `npm run dev`

### Example
Input: “Build portfolio website in 1 week”  
Output: 8-task breakdown with start/end dates.
