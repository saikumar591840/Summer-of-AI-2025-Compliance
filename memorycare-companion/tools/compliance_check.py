"""Simple compliance checker for Summer of AI 2025 requirements."""
import os, json, sys

ROOT = os.path.dirname(os.path.dirname(__file__))

checks = {
    "assigned_courses_placeholder": True,  # Manual verification
    "individual_project": os.path.exists(os.path.join(ROOT, "server", "app.py")),
    "group_project": os.path.exists(os.path.join(ROOT, "client", "index.html")),
    "corpus_contribution": os.path.exists(os.path.join(ROOT, "corpus", "empathetic_dialogues.jsonl")) and os.path.exists(os.path.join(ROOT, "corpus", "routines.jsonl")),
}

score = sum(1 for k,v in checks.items() if v)
total = len(checks)
print("=== Summer of AI 2025 Compliance ===")
for k,v in checks.items():
    print(f"{k:25s}: {'PASS' if v else 'FAIL'}")
print(f"Overall: {score}/{total}")

# JSON output for tool integrations
print(json.dumps(checks))
