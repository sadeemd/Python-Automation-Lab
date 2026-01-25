# Day 6 — Log Counter (OK / FAIL) + Summary Report

## Overview
This lab reads a log file line-by-line and counts how many lines contain:
- `-> OK`
- `-> FAIL`

Then it writes the final results into a summary file and prints them to the terminal.

This is a common automation task for monitoring scripts and IT reporting.

---

## Files
- `log_count.py` → main script
- `run_sample.txt` → input log file
- `summary.txt` → output summary file (generated after running)

---

## Folder Structure
your_lab_folder/
│
├─ run_sample.txt
├─ log_count.py
└─ summary.txt   (created after running)

---

## What This Script Does
✅ Reads `run_sample.txt` safely (UTF-8, ignores bad characters)  
✅ Counts:
- lines containing `-> OK`
- lines containing `-> FAIL`  
✅ Writes results into `summary.txt`  
✅ Prints results in the terminal

---

## How It Works
- The script uses the same folder where it exists:
  - `BASE_DIR = Path(__file__).resolve().parent`

- It defines:
  - `log_file = run_sample.txt`
  - `summary_file = summary.txt`

- It loops over each line and increases counters:
  - `ok += 1` when line contains `-> OK`
  - `fail += 1` when line contains `-> FAIL`

- Finally it saves:
  OK lines: X  
  FAIL lines: Y

---

## How To Run
Open terminal in the lab folder and run:

python log_count.py

---

## Example Input (run_sample.txt)
[2026-01-11 10:00:01] youtube.com -> OK  
[2026-01-11 10:00:05] google.com -> FAIL -> timeout  
[2026-01-11 10:00:10] 1.1.1.1 -> OK  
[2026-01-11 10:00:12] test.com -> FAIL -> dns error  

---

## Example Output (Terminal)
OK lines: 2  
FAIL lines: 2  

---

## Output File (summary.txt)
OK lines: 2  
FAIL lines: 2  

---

## Notes
- This lab is useful for:
  - simple monitoring scripts
  - log analysis
  - counting success/failure results quickly
- The script uses `errors="ignore"` to avoid crashing on weird characters in logs.

---

## Mini Challenge (Optional)
Upgrade the script to:
- Count total lines scanned
- Calculate success rate:
  success_rate = OK / (OK + FAIL)
- Save a timestamp inside `summary.txt`
- Export results to CSV
