# Lab: Log Counter (OK / FAIL) + Summary File

This lab reads a log file line-by-line, counts how many lines contain `-> OK` and `-> FAIL`, then writes the results to a summary file and prints them to the terminal.

## Objective
- Parse a plain-text log file (`run_sample.txt`)
- Count occurrences of:
  - `-> OK`
  - `-> FAIL`
- Save the counts into `summary.txt`

## Project Files
- `log_count.py` — the Python script
- `run_sample.txt` — input log file
- `summary.txt` — output summary file (generated/overwritten)

## Input Format (run_sample.txt)
Each line can contain a timestamp and a target (domain/IP), followed by a status.
Example:
```txt
[2026-01-11 10:00:01] youtube.com -> OK
[2026-01-11 10:00:05] google.com -> FAIL -> timeout
