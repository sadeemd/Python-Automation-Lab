from pathlib import Path
import csv

BASE_DIR = Path(__file__).resolve().parent
REPORT_PATH = BASE_DIR / "report.csv"

ok = 0
fail = 0
missing = 0

with REPORT_PATH.open("r", newline="", encoding="utf-8-sig") as f:
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

print(f"FILE: {REPORT_PATH.name}")
print(f"TOTAL: {total}")
print(f"OK:    {ok}  ({ok_pct:.1f}%)")
print(f"FAIL:  {fail}  ({fail_pct:.1f}%)")
if missing:
    print(f"MISSING_STATUS: {missing}")
