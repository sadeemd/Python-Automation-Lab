# Day 14 — Convert CSV to JSON (report.csv → report.json)

## Overview
This lab converts a CSV file into a JSON file using Python.

CSV is common in reports and spreadsheets, while JSON is widely used in APIs and modern apps.
This script reads `report.csv` and exports the data into `report.json` in a clean structured format.

---

## Files
- `report.csv` → Input file (sample data)
- `to_json.py` → Python script that converts CSV to JSON
- `report.json` → Output file (generated after running)

---

## Folder Structure
your_lab_folder/
│
├─ report.csv
├─ to_json.py
└─ report.json   (created after running)

---

## What This Script Does
✅ Reads `report.csv` using `csv.DictReader()`  
✅ Converts each row into a Python dictionary  
✅ Stores all rows inside a list  
✅ Writes the list to `report.json` using `json.dump()`  
✅ Prints a summary (input name, output name, rows count)

---

## How It Works
- The script always uses the same folder where it exists:
  - `BASE_DIR = Path(__file__).resolve().parent`

- Input file:
  - `report.csv`

- Output file:
  - `report.json`

- It reads rows like this:
  - Each line becomes a dictionary:
    - `{"name": "...", "score": "...", "status": "..."}`

- It writes JSON with:
  - `indent=2` → pretty formatting
  - `ensure_ascii=False` → supports Arabic/Unicode characters

---

## How To Run
Open terminal in the same folder, then run:

python to_json.py

---

## Example Input (report.csv)
name,score,status  
Ali,85,pass  
Sara,72,pass  
Omar,49,fail  

---

## Example Output (report.json)
[
  {
    "name": "Ali",
    "score": "85",
    "status": "pass"
  }
]

---

## Output Summary (Terminal)
Converted CSV to JSON successfully.  
Input: report.csv  
Output: report.json  
Rows: 3  

---

## Notes
- This is a common automation task when preparing data for:
  - APIs
  - dashboards
  - web applications
- `DictReader` automatically uses the first row (header) as keys.

---

## Mini Challenge (Optional)
Upgrade the lab:
- Convert `score` from string to integer before saving
- Save a timestamp in the JSON output (example: `generated_at`)
- Filter only students with `status = pass`
