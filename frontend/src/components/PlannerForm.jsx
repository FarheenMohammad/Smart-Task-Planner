import React, { useState } from "react";

export default function PlannerForm() {
  const [goal, setGoal] = useState("Launch a product in 2 weeks");
  const [deadline, setDeadline] = useState("");
  const [teamSize, setTeamSize] = useState(3);
  const [plan, setPlan] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function submit() {
    setLoading(true);
    setError(null);
    setPlan(null);
    try {
      const res = await fetch("/api/plan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ goal, deadline: deadline || undefined, team_size: Number(teamSize) })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Unknown error");
      setPlan(data);
    } catch (err) {
      setError(String(err));
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <div className="grid gap-2">
        <label className="text-sm font-medium text-slate-700">Goal</label>
        <textarea value={goal} onChange={(e) => setGoal(e.target.value)} rows={3}
          className="w-full p-2 border rounded" />
        <div className="flex gap-2">
          <div>
            <label className="text-sm text-slate-600">Deadline (optional)</label>
            <input type="date" value={deadline} onChange={(e) => setDeadline(e.target.value)}
              className="p-2 border rounded block" />
          </div>
          <div>
            <label className="text-sm text-slate-600">Team size</label>
            <input type="number" value={teamSize} min={1} onChange={(e)=>setTeamSize(e.target.value)}
              className="p-2 border rounded w-24" />
          </div>
        </div>
        <div className="flex gap-2">
          <button onClick={submit} className="px-4 py-2 rounded bg-brand-500 text-white">Generate Plan</button>
          <button onClick={()=>{ setGoal("Launch a product in 2 weeks"); setDeadline(""); setTeamSize(3);}} className="px-4 py-2 rounded border">Reset</button>
        </div>
      </div>

      {loading && <p className="mt-4 text-slate-500">Generating plan…</p>}
      {error && <p className="mt-4 text-red-600">{error}</p>}

      {plan && (
        <div className="mt-6">
          <h2 className="text-lg font-semibold text-slate-700">Plan</h2>
          {plan.at_risk && <div className="text-sm text-red-600">Plan is at risk of missing the deadline.</div>}
          <div className="mt-3 space-y-3">
            {plan.tasks.map((t) => (
              <div key={t.id} className="p-3 border rounded shadow-sm">
                <div className="flex justify-between items-start">
                  <div>
                    <div className="font-semibold text-slate-800">{t.title}</div>
                    <div className="text-sm text-slate-600">{t.description}</div>
                    <div className="mt-1 text-xs text-slate-500">
                      Role: {t.recommended_role} • Est: {t.estimated_hours} hrs • Duration: {t.duration_days} day(s)
                    </div>
                  </div>
                  <div className="text-right text-xs">
                    <div>Start: <span className="font-medium text-slate-700">{t.start_date}</span></div>
                    <div>End: <span className="font-medium text-slate-700">{t.end_date}</span></div>
                    <div className="mt-1 text-slate-500">Deps: {(t.dependencies||[]).join(", ") || "—"}</div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

    </div>
  );
}
