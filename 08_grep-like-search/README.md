# Day 8 — Grep-like Text Search (Line Numbers + Report)

## Overview
This lab builds a small Python tool that works like `grep`.

It searches inside a text file (`notes.txt`) for a keyword (example: `ERROR`),
prints matching lines with their line numbers, and saves a clean report into `grep_report.txt`.

---

## Files
- `notes.txt` → input text file (logs / notes)
- `grep_like.py` → searches for a keyword and collects matches
- `grep_report.txt` → output report (generated after running)

---

## Folder Structure
your_lab_folder/
│
├─ notes.txt
├─ grep_like.py
└─ grep_report.txt   (created after running)

---

## What This Script Does
✅ Reads `notes.txt` safely (UTF-8)  
✅ Searches for a keyword using: `if keyword in line`  
✅ Adds line numbers using: `enumerate(..., start=1)`  
✅ Collects all matches into a list  
✅ Creates a report that includes:
- report time
- keyword
- number of matches
- matching lines  
✅ Saves report into `grep_report.txt`  
✅ Prints the matches in the terminal + prints report filename

---

## How It Works
- The script uses the same folder of the script:
  - `BASE_DIR = Path(__file__).resolve().parent`

- It sets:
  - `keyword = "ERROR"`

- It loops with line numbers:
  - `enumerate(file, start=1)`

Example match format:
1: ERROR: x

---

## How To Run
Open terminal in the same folder and run:

python grep_like.py

---

## Example Input (notes.txt)
ERROR: x  
INFO: y  
ERROR: z  

---

## Example Output (Terminal)
1: ERROR: x  
3: ERROR: z  
Saved report: grep_report.txt  

---

## Example Output File (grep_report.txt)
Report time: 2026-01-13T18:58:40  
Keyword: ERROR  
Matches: 2  
------------------------------  
1: ERROR: x  
3: ERROR: z  

---

## Notes
- This lab is useful for:
  - scanning logs quickly
  - finding errors/warnings
  - building simple monitoring tools
- You can change the keyword anytime (example: `WARNING`, `FAILED`, `INFO`).

---

## Mini Challenge (Optional)
Upgrade the script to:
- Let the user choose the keyword using input()
- Support multiple keywords (ERROR + WARNING)
- Save results into CSV (line_number, message)
