# Day 10 — Folder Scan Report (Pathlib + Sizes)

## Overview
This lab scans the current folder (the same folder where the script exists) and generates a clean report that includes:
- File names
- File sizes (B / KB / MB / GB)
- Sorting from largest to smallest
- Total number of files

The report is printed to the terminal and also saved into a text file: `folder_report.txt`.

---

## Files
- `folder_scan.py` — scans the folder and generates the report
- `folder_report.txt` — output report (created after running the script)

---

## What This Script Does
✅ Scans the script folder using `Path(__file__).resolve().parent`  
✅ Collects all files + sizes using `stat().st_size`  
✅ Converts size into human readable format (B / KB / MB / GB)  
✅ Sorts files from largest to smallest  
✅ Prints a formatted table  
✅ Saves the same output into `folder_report.txt`

---

## How It Works (Key Ideas)
- The script uses the same folder of the script itself:
  `p = Path(__file__).resolve().parent`

- It creates the report file path:
  `folder_report.txt`

- It skips saving the report file inside the scan results (so it doesn’t include itself).

- It formats sizes using a helper function:
  `human_size()`

---

## How To Run
Open terminal inside the lab folder and run:

python folder_scan.py

---

## Example Output (Terminal)
Folder: .../10_folder-scan  
Report time: 2026-01-15T17:42:19  
------------------------------------------------------------  
File Name                                           Size  
------------------------------------------------------------  
folder_scan.py                                    1.1 KB  
------------------------------------------------------------  
Total files: 1  

---

## Output File
After running, you will find:

folder_report.txt

It contains the same table printed in the terminal.

---

## Notes
- This lab is very useful for:
  - checking large files in a project folder
  - cleaning unnecessary files
  - quick folder reporting for IT tasks

---

## Mini Challenge (Optional)
Upgrade the script to:
- Scan only specific extensions (example: only `.py` files)
- Include folder sizes too (not only files)
- Export the report as CSV (file_name, size_bytes, size_human)
