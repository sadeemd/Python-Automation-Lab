# Day 17 — Safe Write (tmp then replace)

## Overview
This lab demonstrates **safe file writing** using an **atomic replace** technique.
Instead of writing directly to the final file, we:

1. Write the content to a temporary file (`out.tmp`)
2. Replace the final file (`out.txt`) using `replace()`

This approach helps prevent **file corruption** if the program crashes or stops during writing.

---

## Files
- `safe_write.py` — Main script
- `out.tmp` — Temporary file (created during execution)
- `out.txt` — Final output file (created/updated safely)

---

## How It Works
### Why write to a temp file?
If you write directly to `out.txt` and something fails mid-write, the file may become incomplete.

Using a temp file ensures:
- The final file is replaced **only after** the new content is fully written
- You either keep the old file OR get the new file completely (no partial content)

---

## Code Explanation
The script uses the folder of `safe_write.py` as the output location:

- `BASE_DIR = Path(__file__).resolve().parent`  
This ensures the output files are saved in the **same folder** as the script.

Then it writes safely:

- Write to `out.tmp`
- Replace `out.txt` using `tmp.replace(final)`

---

## Run the Script
Open terminal in the project folder and run:

```bash
python safe_write.py
