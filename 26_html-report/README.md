# Day 26 — Simple HTML Report

This task generates a simple **HTML report** (`report.html`) based on the summary numbers (OK/FAIL) from **Day 25** by reading `report.csv`.

The output HTML file is easy to open in a browser and share.

---

## Folder Structure

26_html-report/
├─ html_report.py
├─ report.csv
└─ report.html

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

python html_report.py

---

## Output

The script creates:

- `report.html`

Then prints a message like:

report.html created

Open `report.html` in any browser to view the report.

---

## Notes

- Any row where `status` is not exactly `OK` is counted as **FAIL**.
- Keep `report.csv` in the same folder as the script so the script can find it easily.
