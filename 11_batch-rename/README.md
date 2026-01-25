# Day 11 — Rename Files Using Mapping (rename_map.txt)

## Overview
This lab automates renaming multiple files using a simple mapping file.

Instead of renaming files manually, you write rename rules inside `rename_map.txt`
and run `rename_files.py`. The script will rename files safely and print what happened.

---

## Files
- `rename_files.py` → reads mapping rules and renames files
- `rename_map.txt` → contains rename rules (old name => new name)
- Example test files:
  - `old1.txt`
  - `old2.log`

---

## Folder Structure
your_lab_folder/
│
├─ rename_files.py
├─ rename_map.txt
├─ old1.txt
└─ old2.log

After running, the renamed files will appear:
- `new1.txt`
- `new2.log`

---

## Mapping File Format (rename_map.txt)
Each rename rule must be written like this:

old_name.ext => new_name.ext

You can also add comments using `#`.

Example:
```txt
# Rename Mapping File
old1.txt => new1.txt
old2.log => new2.log
