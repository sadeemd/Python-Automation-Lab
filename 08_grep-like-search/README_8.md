# Day 8 — Grep-like Text Search (with Line Numbers)

A small Python script that searches a text file for a keyword (like `grep`) and prints matching lines with their line numbers.  
It also saves the results into a simple report file for documentation and GitHub portfolio.

## Files
- `notes.txt` — input text file (logs/notes)
- `grep_like.py` — the script
- `grep_report.txt` — generated output report (created after running)

## What this lab practices
- Reading text files safely
- Searching for a substring (`keyword in line`)
- Getting line numbers using `enumerate(..., start=1)`
- Writing a clean report file (evidence/output)

## Requirements
- Python 3.8+

## Input format (`notes.txt`)
Put one message per line. Example:
```txt
ERROR: x
INFO: y
ERROR: z
