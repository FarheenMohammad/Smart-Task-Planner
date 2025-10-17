# backend/app.py
import os
from flask import Flask, request, jsonify
from planner.planner_service import PlannerService
from db import init_db, get_session
from models import Plan

app = Flask(__name__)

# initialize db (sqlite)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./plans.db")
init_db(DATABASE_URL)

service = PlannerService()

@app.route("/api/plan", methods=["POST"])
def create_plan():
    data = request.get_json() or {}
    try:
        plan_obj = service.generate_plan(data)
        # save to DB
        session = get_session()
        p = Plan(goal=plan_obj["goal"], tasks=plan_obj["tasks"])
        session.add(p)
        session.commit()
        plan_obj["plan_id"] = p.id
        return jsonify(plan_obj), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/plan/<int:plan_id>", methods=["GET"])
def get_plan(plan_id):
    session = get_session()
    p = session.query(Plan).get(plan_id)
    if not p:
        return jsonify({"error": "Not found"}), 404
    return jsonify({
        "plan_id": p.id,
        "goal": p.goal,
        "tasks": p.tasks,
        "created_at": p.created_at.isoformat()
    }), 200

if __name__ == "__main__":
    app.run(debug=True, port=int(os.getenv("PORT", 5000)))
