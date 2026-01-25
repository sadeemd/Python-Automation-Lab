# Day 9 — Split + Clean Text File (data.txt → cleaned.txt)

## Overview
This lab cleans a simple text file that contains `name, age` records.
Some lines may have extra spaces, so the goal is to normalize the data into a clean format like:

ali,20
sara,30

This is a common automation task when dealing with messy text inputs.

---

## Files
- `data.txt` → input file (raw text with extra spaces)
- `split_clean.py` → script that cleans and formats the data
- `cleaned.txt` → output file (generated after running)

---

## Folder Structure
your_lab_folder/
│
├─ data.txt
├─ split_clean.py
└─ cleaned.txt   (created after running)

---

## What This Script Does
✅ Reads each line from `data.txt`  
✅ Splits the line by comma `,`  
✅ Removes extra spaces using `strip()`  
✅ Keeps only valid lines with exactly 2 parts (name + age)  
✅ Writes cleaned output into `cleaned.txt`  
✅ Prints the output path after saving

---

## How It Works
- The script uses the same folder of the script:
  - `BASE_DIR = Path(__file__).resolve().parent`

- It reads raw input:
  - `data.txt`

- Cleans each line:
  - `line.split(",")` → splits into parts
  - `strip()` → removes spaces from both sides

Example:
"  ali , 20 "  →  ["ali", "20"]

- Writes final result as:
  name,age

---

## How To Run
Open terminal in the same folder and run:

python split_clean.py

---

## Example Input (data.txt)
  ali , 20
 sara, 30

---

## Example Output (cleaned.txt)
ali,20  
sara,30  

---

## Output Message (Terminal)
Saved: .../cleaned.txt

---

## Notes
- Extra spaces are removed automatically.
- Lines that do not contain exactly one comma (2 parts) are ignored safely.

---

## Mini Challenge (Optional)
Upgrade the script to:
- Skip lines with non-numeric age values
- Convert the output into CSV with a header:
  name,age
- Save a report file showing how many lines were processed vs accepted
