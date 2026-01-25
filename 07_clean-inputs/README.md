# Day 7 — Clean Inputs (Ignore Comments) + Generate Report

## Overview
This lab reads a list of domains from `config.txt`, cleans the input lines, ignores empty lines and comment lines, then generates a report file.

This is a common automation pattern when dealing with config files:
- remove spaces
- ignore comments
- load only valid entries
- generate a clean output report

---

## Files
- `config.txt` → input list (domains + optional comments)
- `dns_check.py` → script that reads and cleans inputs
- `loaded_domains_report.txt` → output report (generated after running)

---

## Folder Structure
your_lab_folder/
│
├─ config.txt
├─ dns_check.py
└─ loaded_domains_report.txt   (created after running)

---

## What This Script Does
✅ Reads `config.txt` line by line  
✅ Removes extra spaces using `strip()`  
✅ Ignores:
- empty lines
- comment lines that start with `#`  
✅ Builds a clean list of domains  
✅ Generates a report file that includes:
- report time
- number of loaded domains
- the final domain list  
✅ Saves report into `loaded_domains_report.txt`  
✅ Prints summary in the terminal

---

## How It Works
- The script always runs using the same folder where it exists:
  - `BASE_DIR = Path(__file__).resolve().parent`

- Input file:
  - `config.txt`

- Output file:
  - `loaded_domains_report.txt`

- Cleaning logic:
  - `s = line.strip()` → remove spaces
  - if `s` is not empty and does not start with `#`, then it is a valid domain

- Report format example:
  Report time: 2026-01-13T01:42:59  
  Loaded domains: 2  
  ------------------------------  
  google.com  
  youtube.com  

---

## How To Run
Open terminal in the same folder and run:

python dns_check.py

---

## Example Input (config.txt)
# comment  
google.com  
youtube.com  

---

## Example Output (Terminal)
Loaded: 2  
Saved report: loaded_domains_report.txt  

---

## Output File (loaded_domains_report.txt)
Report time: 2026-01-13T01:42:59  
Loaded domains: 2  
------------------------------  
google.com  
youtube.com  

---

## Notes
- This pattern is useful for:
  - reading safe configuration lists
  - preparing domain lists for network scripts
  - filtering noisy input files

---

## Mini Challenge (Optional)
Upgrade the lab:
- Validate domains (skip invalid formats)
- Remove duplicates automatically
- Save results as CSV instead of TXT
- Add a line counter: processed lines vs loaded domains
