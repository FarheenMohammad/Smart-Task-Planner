# backend/tests/test_planner.py
import pytest
from planner.planner_service import PlannerService

def test_generate_plan_mock():
    svc = PlannerService()
    data = {"goal": "Launch a product in 2 weeks", "team_size": 3, "deadline": None}
    plan = svc.generate_plan(data)
    assert "tasks" in plan
    assert isinstance(plan["tasks"], list)
    # each task should have start_date and end_date
    for t in plan["tasks"]:
        assert "start_date" in t and "end_date" in t
