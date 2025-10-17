# backend/planner/planner_service.py
from .llm_client import LLMClient
from .schemas import PlanInput
from datetime import datetime, timedelta
import json, math, re
from typing import List, Dict

PROMPT_TEMPLATE = '''Break the following goal into a JSON array of tasks.
Each task must contain: id (short), title, description, estimated_hours (number), dependencies (list of titles), recommended_role.
Use the deadline and team size to reason about dates but output only tasks (we will schedule later).
Goal: "{goal}"
Deadline: "{deadline}"
Team size: {team_size}
Priority: {priority}
Respond ONLY with valid JSON array (no explanatory text).
'''

class PlannerService:
    def __init__(self, llm=None):
        self.llm = llm or LLMClient()

    def _parse_json_from_text(self, text: str):
        text = text.strip()
        try:
            return json.loads(text)
        except Exception:
            # try to extract JSON array substring
            m = re.search(r'\[.*\]', text, flags=re.S)
            if m:
                return json.loads(m.group(0))
            raise ValueError("Unable to parse JSON from LLM output")

    def _topological_sort(self, tasks: List[Dict]) -> List[Dict]:
        # Build mapping from title to task
        title_map = {t["title"]: t for t in tasks}
        visited = {}
        order = []

        def dfs(title):
            if title not in title_map:
                return
            if visited.get(title) == 1:
                raise ValueError("Cycle detected in dependencies")
            if visited.get(title) == 2:
                return
            visited[title] = 1
            for dep in title_map[title].get("dependencies", []):
                dfs(dep)
            visited[title] = 2
            order.append(title_map[title])

        for t in tasks:
            if visited.get(t["title"], 0) == 0:
                dfs(t["title"])
        return order

    def _schedule(self, tasks: List[Dict], team_size: int, deadline: str = None):
        # Convert estimated_hours -> duration in days assuming 8 hours/workday per person and full parallelism by team
        # We schedule tasks topologically; earliest start is project start (today) or computed from deps.
        project_start = datetime.utcnow().date()
        # If deadline provided, attempt to fit within it; else leave schedule relative to start.
        deadline_date = None
        if deadline:
            try:
                deadline_date = datetime.fromisoformat(deadline).date()
            except Exception:
                pass

        ordered = self._topological_sort(tasks)
        name_to_dates = {}
        for t in ordered:
            est_hours = float(t.get("estimated_hours", 8))
            # effective hours/day = 8 * team_size (simple model)
            hours_per_day = 8 * max(1, team_size)
            duration_days = max(1, math.ceil(est_hours / hours_per_day))
            # compute earliest start = max(end of dependencies, project_start)
            earliest = project_start
            for dep in t.get("dependencies", []):
                dep_dates = name_to_dates.get(dep)
                if dep_dates:
                    dep_end = datetime.fromisoformat(dep_dates["end_date"]).date()
                    if dep_end > earliest:
                        earliest = dep_end
            start_date = earliest
            end_date = start_date + timedelta(days=duration_days)
            # store as ISO strings
            t["start_date"] = start_date.isoformat()
            t["end_date"] = end_date.isoformat()
            t["duration_days"] = duration_days
            name_to_dates[t["title"]] = {"start_date": t["start_date"], "end_date": t["end_date"]}
        # check against deadline
        overall_end = max(datetime.fromisoformat(t["end_date"]).date() for t in ordered)
        at_risk = False
        if deadline_date and overall_end > deadline_date:
            at_risk = True
        return ordered, at_risk

    def generate_plan(self, data: dict) -> dict:
        inp = PlanInput(**data)
        prompt = PROMPT_TEMPLATE.format(goal=inp.goal, deadline=inp.deadline or "", team_size=inp.team_size or 1, priority=inp.priority)
        raw = self.llm.call(prompt)
        tasks = self._parse_json_from_text(raw)
        # Ensure fields & ids
        for i, t in enumerate(tasks):
            t.setdefault("id", f"t{i+1}")
            t.setdefault("dependencies", [])
            t.setdefault("estimated_hours", t.get("estimated_hours", 8))
            t.setdefault("recommended_role", t.get("recommended_role", "Contributor"))
        scheduled_tasks, at_risk = self._schedule(tasks, team_size=inp.team_size or 1, deadline=inp.deadline)
        result = {
            "goal": inp.goal,
            "tasks": scheduled_tasks,
            "created_at": datetime.utcnow().isoformat() + "Z",
            "at_risk": at_risk
        }
        return result
