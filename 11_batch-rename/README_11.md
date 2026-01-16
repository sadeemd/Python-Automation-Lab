# Day 11 — Rename Files Using Mapping (NumPy Automation Lab)

This lab automates renaming multiple files based on a simple mapping file.

## Files
- `rename_map.txt` → contains the rename rules (old name => new name)
- `rename_files.py` → reads the mapping and renames files automatically
- Example test files: `old1.txt`, `old2.log`

---

## Mapping File Format (`rename_map.txt`)

Example:
```txt
# Rename Mapping File
old1.txt => new1.txt
old2.log => new2.log
