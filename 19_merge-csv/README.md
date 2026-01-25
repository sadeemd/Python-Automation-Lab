# Day 19 — Merge Multiple CSV Reports (multi_reports → merged.csv)

## Overview
This lab merges multiple CSV files from a folder into **one combined CSV file**.

You will put several CSV reports inside the `multi_reports/` folder, then run `merge_csv.py`.
The script will read all `*.csv` files, merge their rows, and generate a final output file: `merged.csv`.

It also adds a useful column called `source_file` to show which CSV file each row came from.

---

## Folder Structure
Make sure your project looks like this:

your_lab_folder/
│
├─ multi_reports/
│   ├─ report1.csv
│   ├─ report2.csv
│   └─ report3.csv
│
└─ merge_csv.py

After running the script, you will get:

your_lab_folder/
└─ merged.csv

---

## What The Script Does
- Reads all CSV files inside: `multi_reports/`
- Combines all rows into one file: `merged.csv`
- Collects all column names safely (even if some files have extra columns)
- Adds:
  - `source_file` → the file name for each row

---

## How To Run
Open terminal inside the lab folder, then run:

python merge_csv.py

---

## Output
The script will print a summary like:

Merged files: 3  
Total rows: 250  
Saved: .../merged.csv

And it will create:
- `merged.csv` (in the same directory as `merge_csv.py`)

---

## Example

### Input files inside `multi_reports/`

**report1.csv**
name,amount  
Ali,100  
Sara,200  

**report2.csv**
name,amount,category  
Omar,150,Food  

### Output: `merged.csv`
amount,category,name,source_file  
100,,Ali,report1.csv  
200,,Sara,report1.csv  
150,Food,Omar,report2.csv  

---

## Notes
- If the folder `multi_reports/` has no CSV files (or the files are empty), you will see:
  No rows found. Make sure multi_reports has CSV files with data.

- This script can handle CSV files with different columns because it builds the final header automatically.

---

## Mini Challenge (Optional)
Try enhancing the script to:
- Add a `merged_at` column with the current date/time
- Skip empty rows automatically
- Sort the output by a chosen column (example: amount or date)
