from pathlib import Path
import csv

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "report.csv"
HTML_PATH = BASE_DIR / "report.html"

ok = 0
fail = 0
missing = 0

with CSV_PATH.open("r", newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        status = (row.get("status") or "").strip().upper()
        if status == "OK":
            ok += 1
        elif status == "":
            missing += 1
        else:
            fail += 1

total = ok + fail + missing
ok_pct = (ok / total * 100) if total else 0
fail_pct = (fail / total * 100) if total else 0

html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Daily Report</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <h1>Daily Report</h1>
  <p><strong>TOTAL</strong>: {total}</p>
  <p><strong>OK</strong>: {ok} ({ok_pct:.1f}%)</p>
  <p><strong>FAIL</strong>: {fail} ({fail_pct:.1f}%)</p>
  {"<p><strong>MISSING_STATUS</strong>: " + str(missing) + "</p>" if missing else ""}
</body>
</html>
"""

HTML_PATH.write_text(html, encoding="utf-8")
print(f"{HTML_PATH.name} created")
