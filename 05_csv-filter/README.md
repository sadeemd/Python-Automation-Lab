# Day 5 — CSV Filter (Keep Only OK Rows)

## Overview
This lab reads a CSV file and creates a new CSV file that contains only the rows where:

status = OK

This is a common automation task when you need to filter reports quickly and export the clean results.

---

## Files
- input.csv → input data
- csv_filter.py → script that filters the CSV rows
- filtered.csv → output file (generated after running)

---

## Folder Structure
your_lab_folder/
│
├─ input.csv
├─ csv_filter.py
└─ filtered.csv   (created after running)

---

## What This Script Does
✅ Reads input.csv using csv.DictReader()  
✅ Writes a new file filtered.csv using csv.DictWriter()  
✅ Keeps only rows where:
- status == "OK"  
✅ Saves the output in the same folder of the script  
✅ Prints the output file path after finishing

---

## How It Works
- The script uses the same directory where it is located:
  BASE_DIR = Path(__file__).resolve().parent

- Input file:
  input.csv

- Output file:
  filtered.csv

- Filtering rule:
  Only write the row when:
  row["status"] == "OK"

---

## How To Run
Open terminal inside the lab folder and run:

python csv_filter.py

---

## Example Input (input.csv)
item,status  
A,OK  
B,FAIL  
C,OK  
D,FAIL  

---

## Example Output (filtered.csv)
item,status  
A,OK  
C,OK  

---

## Terminal Output
Done: .../filtered.csv

---

## Notes
- The script keeps the same CSV header (columns).
- This lab can be adjusted easily to filter by other values like:
  FAIL / WARNING / SUCCESS

---

## Mini Challenge (Optional)
Upgrade the script to:
- Filter FAIL rows instead of OK
- Let the user choose the status using input()
- Count how many rows were saved and print the number
