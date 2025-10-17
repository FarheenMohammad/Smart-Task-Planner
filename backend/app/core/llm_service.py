import openai, os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_plan(goal: str):
    prompt = f"""
    You are an AI planner. Break this goal into actionable, ordered tasks with:
    - Task name
    - Dependency (if any)
    - Estimated completion time
    - Start and end date relative to today

    Goal: "{goal}"
    Return JSON format.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a meticulous task planner."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.5,
    )

    return response["choices"][0]["message"]["content"]
