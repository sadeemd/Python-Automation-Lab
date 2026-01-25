# Day 12 — Backup Before Editing (input.txt → input.bak)

## Overview
This lab demonstrates a critical safety practice in automation and IT work:

✅ Always create a backup copy **before editing or replacing a file**.

Instead of risking data loss by modifying the original file directly, the script creates a safe backup first.

---

## Files
- `input.txt` → original input file
- `rotate_log.py` → script that creates a backup
- `input.bak` → backup file (created after running)

---

## Folder Structure
your_lab_folder/
│
├─ input.txt
└─ rotate_log.py

After running, you will get:

your_lab_folder/
└─ input.bak

---

## What This Script Does
✅ Finds the lab folder automatically  
✅ Checks if `input.txt` exists  
✅ Creates a full backup copy: `input.bak`  
✅ Prints messages showing progress and paths

---

## How It Works
- The script uses:
  - `BASE_DIR = Path(__file__).resolve().parent`
  so it always runs safely using the same folder where the script is located.

- It looks for:
  - `input.txt`

- If the file exists:
  - Reads its content
  - Writes the same content to:
    - `input.bak`

- If the file does not exist:
  - Prints:
    input.txt not found!

---

## How To Run
Open terminal in the same folder and run:

python rotate_log.py

---

## Example Output
Running in: ...  
Looking for: .../input.txt  
Backup created: .../input.bak  

---

## Notes
- This approach protects you from mistakes or accidental overwrites.
- You can apply the same idea before:
  - cleaning data files
  - editing configs
  - updating logs
  - replacing any important text files

---

## Mini Challenge (Optional)
Upgrade the script to:
- Add timestamp to backup name (example: input_2026-01-25.bak)
- Create backups for multiple files in a folder
- Backup only if the content changed
