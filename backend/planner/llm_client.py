# backend/planner/llm_client.py
import os
import json
from typing import Optional

# Try to use openai if OPENAI_API_KEY is provided, else fallback to a deterministic mock
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_KEY:
    import openai
    openai.api_key = OPENAI_KEY

class LLMClient:
    def __init__(self, model: str = "gpt-4o-mini"):
        self.model = model

    def call(self, prompt: str, max_tokens: int = 800, temperature: float = 0.2) -> str:
        if OPENAI_KEY:
            resp = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role":"system","content":"You are a senior product manager; output only JSON."},
                          {"role":"user","content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return resp["choices"][0]["message"]["content"]
        else:
            # Mock deterministic response for offline demo — returns JSON array string
            # This mock creates 4 tasks appropriate to the example goal.
            # NOTE: for real usage provide OPENAI_API_KEY environment variable.
            mock = [
                {
                    "id": "t1",
                    "title": "Define MVP scope",
                    "description": "List core features to ship in first release and cut non-essentials.",
                    "recommended_role": "PM",
                    "estimated_hours": 8,
                    "dependencies": []
                },
                {
                    "id": "t2",
                    "title": "Design UI/UX for MVP",
                    "description": "Create wireframes and clickable prototype for core flows.",
                    "recommended_role": "Designer",
                    "estimated_hours": 16,
                    "dependencies": ["Define MVP scope"]
                },
                {
                    "id": "t3",
                    "title": "Implement backend APIs",
                    "description": "Create product endpoints and database models for MVP.",
                    "recommended_role": "Backend Engineer",
                    "estimated_hours": 24,
                    "dependencies": ["Define MVP scope"]
                },
                {
                    "id": "t4",
                    "title": "Integrate frontend and QA",
                    "description": "Connect frontend to APIs, run acceptance tests, fix bugs.",
                    "recommended_role": "Fullstack / QA",
                    "estimated_hours": 16,
                    "dependencies": ["Design UI/UX for MVP", "Implement backend APIs"]
                }
            ]
            return json.dumps(mock)
