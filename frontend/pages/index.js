"use client";
import { useState } from "react";

export default function Home() {
  const [goal, setGoal] = useState("");
  const [plan, setPlan] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    const res = await fetch("http://localhost:8000/plan", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ goal }),
    });
    const data = await res.json();
    setPlan(data.plan);
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-500 to-purple-600 text-white flex flex-col items-center p-8">
      <h1 className="text-4xl font-bold mb-6">Smart Task Planner 🧠</h1>
      <form onSubmit={handleSubmit} className="flex gap-2 mb-6">
        <input
          type="text"
          value={goal}
          onChange={(e) => setGoal(e.target.value)}
          placeholder="e.g., Launch my app in 2 weeks"
          className="text-black rounded-lg p-2 w-72"
        />
        <button className="bg-yellow-400 text-black px-4 py-2 rounded-lg shadow-md hover:bg-yellow-300">
          Plan
        </button>
      </form>
      {plan && (
        <div className="bg-white text-black rounded-lg p-4 w-3/4 shadow-md">
          <h2 className="font-semibold mb-2">Generated Plan:</h2>
          <pre className="whitespace-pre-wrap">{plan}</pre>
        </div>
      )}
    </div>
  );
}
