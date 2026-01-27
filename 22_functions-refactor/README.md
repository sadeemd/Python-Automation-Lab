# Day 22 — Functions (Reusable Code) | `nhc.py`

## Goal
Build a small reusable function to clean a list of text items instead of repeating the same filtering logic.

## What this script does
The function `clean_items(items)` returns a cleaned list by applying these rules:
- Trim spaces using `strip()`
- Remove empty lines
- Ignore comments (any line that starts with `#` after trimming)

## Files
- `nhc.py`

## How to Run
From the folder that contains `nhc.py`:
```bash
python nhc.py
