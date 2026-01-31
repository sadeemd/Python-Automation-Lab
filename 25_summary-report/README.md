# Day 25 — Summary Report (Counts)

This task reads a CSV report file and prints a quick summary by counting:
- **OK** rows
- **FAIL** rows (any status other than OK)

This is a useful step for tracking progress and preparing for dashboards later.

---

## Folder Structure

25_summary-report/
├─ summary_report.py
└─ report.csv

---

## Input (report.csv)

Your `report.csv` must include a column named **status**.

Minimal example:

status
OK
FAIL
OK

---

## How to Run

From inside the folder:

python summary_report.py

---

## Output

The script prints counts to the terminal, for example:

OK 7 FAIL 3

---

## Notes

- Any row where `status` is not exactly `OK` is counted as **FAIL**.
- Keep `report.csv` in the same folder as the script to avoid path issues.
