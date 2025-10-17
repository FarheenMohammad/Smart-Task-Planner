🧠 Smart Task Planner

Smart Task Planner is an AI-powered productivity assistant that breaks down any user-defined goal into a set of actionable tasks with timelines, dependencies, and progress tracking.
Powered by an LLM reasoning engine and a simple scheduling algorithm, it helps users transform vague goals into structured, achievable plans.

🚀 Features

📝 Goal-based task generation:
Enter a goal like “Launch mobile app in 2 weeks” — get an auto-generated list of subtasks with deadlines and dependencies.

⏳ Timeline estimation:
Tasks are scheduled based on logical dependencies and estimated effort.

🔗 Task dependencies:
Each generated task references its prerequisites (e.g., Design before Development).

🧮 AI + Deterministic Scheduling:
Combines LLM reasoning with a local scheduling model for reproducible timelines.

💾 Persistent Storage:
Stores all plans and tasks in a SQLite database using SQLAlchemy ORM.

🖥️ Interactive Frontend:
A clean, responsive React + Tailwind interface to submit goals and visualize plans.

⚙️ Extensible Architecture:
Modular backend with FastAPI, making it easy to integrate different LLMs (OpenAI, Anthropic, or local).

🧩 Tech Stack
Layer	Technology
Frontend	React, Tailwind CSS, Axios
Backend	FastAPI (Python 3.10+)
AI Engine	LLM API (e.g., GPT-4 or GPT-3.5)
Database	SQLite + SQLAlchemy ORM
Scheduling	Topological sorting + timeline estimation
Deployment	Docker / Uvicorn (local dev)


💡 Example Usage
Input

“Build a portfolio website in 1 week with a team of 2”

Output (Sample)
Task	Duration	Depends On	Start Date	End Date
Define project goals	1 day	—	Oct 17	Oct 17
Design UI mockups	1 day	Define project goals	Oct 18	Oct 18
Set up repo & frameworks	1 day	Define project goals	Oct 18	Oct 18
Develop frontend	2 days	Design UI mockups	Oct 19	Oct 20
Integrate backend	2 days	Develop frontend	Oct 21	Oct 22
Testing & bug fixes	1 day	Integrate backend	Oct 23	Oct 23
Deploy & review	1 day	Testing & bug fixes	Oct 24	Oct 24
🧠 How It Works

Input Parsing:
User submits a goal text + optional parameters (deadline, team size).

LLM Reasoning:
LLM generates subtasks, dependencies, and estimated durations.

Scheduling:
The planner assigns start/end dates using topological sorting and total duration constraints.

Storage & Retrieval:
Tasks are saved in SQLite for persistent access.

🧩 API Endpoints
Method	Endpoint	Description
POST	/api/plan	Generate task plan for given goal
GET	/api/plans	Retrieve all stored plans
GET	/api/plan/{id}	Get plan by ID
DELETE	/api/plan/{id}	Delete plan


🧪 Future Enhancements

✅ User login & authentication

✅ Export plan to PDF/Excel

✅ Gantt chart visualization

✅ Integration with Google Calendar

✅ Multi-user collaboration
