import React from "react";
import PlannerForm from "./components/PlannerForm";

export default function App(){
  return (
    <div className="min-h-screen bg-slate-50 py-10">
      <div className="max-w-3xl mx-auto bg-white rounded-2xl shadow p-6">
        <header className="mb-4">
          <h1 className="text-2xl font-bold text-brand-700">Smart Task Planner</h1>
          <p className="text-slate-600">Enter a goal and get a plan with tasks, dependencies and timelines.</p>
        </header>
        <PlannerForm />
      </div>
    </div>
  );
}
