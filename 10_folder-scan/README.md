# Day 10 — Folder Scan (Pathlib)

## Overview
This lab scans the current folder using Python `pathlib` and generates a clean report that includes:
- File names
- File sizes (B / KB / MB / GB)
- Sorting from largest to smallest
- Total number of files

The final output is printed to the terminal and also saved into a text file.

---

## Files
- `folder_scan.py` — scans the folder and creates the report
- `folder_report.txt` — generated output report after running the script

---

## What You Learn
- Working with files and folders using `pathlib.Path`
- Difference between `is_file()` and `is_dir()`
- Reading file metadata using `stat().st_size`
- Sorting results by file size
- Saving output to a report file

---

## How It Works
The script:
1) Scans the current folder (same folder as the script)
2) Collects all files and their sizes
3) Sorts them from largest to smallest
4) Prints a formatted table
5) Saves the same table to `folder_report.txt`

---

## Run the Script
Open a terminal in the lab folder and run:

```bash
python folder_scan.py
