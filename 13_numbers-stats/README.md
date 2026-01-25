# Day 13 — Simple Number Statistics (numbers.txt → stats.py)

## Overview
This lab reads numbers from a text file (`numbers.txt`) and calculates basic statistics:
- Count
- Minimum
- Maximum
- Average (mean)

This is a common automation task when you need quick analysis from a simple data file.

---

## Files
- `numbers.txt` → input file (one number per line)
- `stats.py` → reads the file and prints statistics

---

## Folder Structure
your_lab_folder/
│
├─ numbers.txt
└─ stats.py

---

## What This Script Does
✅ Reads numbers from `numbers.txt`  
✅ Cleans empty lines safely  
✅ Converts text into integers  
✅ Calculates:
- count
- min
- max
- average  
✅ Prints the results in the terminal

---

## Example Input (numbers.txt)
10  
20  
30  

---

## How It Works
- The script finds the folder where it is running:
  - `BASE_DIR = Path(__file__).resolve().parent`

- Then it loads the file:
  - `numbers_file = BASE_DIR / "numbers.txt"`

- It reads the lines safely:
  - skips empty lines
  - converts to integers

- If the file is empty, it stops safely:
  File is empty. No numbers to analyze.

- Otherwise it prints results:
  count <N>
  min <min> max <max> avg <avg>

---

## How To Run
Open terminal in the same folder and run:

python stats.py

---

## Example Output
count 3  
min 10 max 30 avg 20.0  

---

## Notes
- Make sure every line in `numbers.txt` is a valid number.
- Empty lines are ignored automatically.

---

## Mini Challenge (Optional)
Upgrade the script to:
- Print the sum of numbers
- Print the median
- Save the results into a file like `stats_report.txt`
