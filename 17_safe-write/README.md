# Day 17 — Safe Write (Atomic Write using tmp then replace)

## Overview
This lab demonstrates **safe file writing** using an **atomic replace** technique.

Instead of writing directly to the final file, we:
1) Write the new content into a temporary file (`out.tmp`)
2) Replace the final file (`out.txt`) using `replace()`

This method helps prevent **file corruption** if the program stops or crashes أثناء الكتابة.

---

## Files
- `safe_write.py` — Main script
- `out.tmp` — Temporary file (created during run)
- `out.txt` — Final output file (created/updated safely)

---

## What This Script Does
✅ Creates a temporary file `out.tmp`  
✅ Writes content to it safely  
✅ Replaces `out.txt` in one step (atomic replace)  
✅ Prints a success message + the output file path

---

## How It Works
The script uses the same directory of the script to save files:

- `BASE_DIR = Path(__file__).resolve().parent`
This ensures all outputs appear **in the same folder where `safe_write.py` exists**.

Then:
- Write to temp file:
  - `tmp.write_text(content, encoding="utf-8")`
- Replace final file safely:
  - `tmp.replace(final)`

Atomic replace means:
- Either the old `out.txt` stays
- OR it becomes fully updated
(No half-written file)

---

## How To Run
Open terminal inside the lab folder and run:

python safe_write.py

---

## Example Output
Atomic write done ✅  
Saved: .../out.txt  

---

## Result File
After running, you will find:

- `out.txt` contains:
new content

---

## Mini Challenge (Optional)
Improve the script:
- Ask the user to type the content before saving
- Save a backup copy before replacing (example: out_backup.txt)
- Add timestamp to content (date/time)
