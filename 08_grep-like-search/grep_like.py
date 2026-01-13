from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
notes_path = BASE_DIR / "notes.txt"
report_path = BASE_DIR / "grep_report.txt"

keyword = "ERROR"

matches = []
for i, line in enumerate(notes_path.open("r", encoding="utf-8"), start=1):
    if keyword in line:
        matches.append(f"{i}: {line.strip()}")

lines = []
lines.append(f"Report time: {datetime.now().isoformat(timespec='seconds')}")
lines.append(f"Keyword: {keyword}")
lines.append(f"Matches: {len(matches)}")
lines.append("-" * 30)
lines.extend(matches if matches else ["No matches found."])

report_path.write_text("\n".join(lines), encoding="utf-8")

print("\n".join(matches) if matches else "No matches found.")
print("Saved report:", report_path.name)
