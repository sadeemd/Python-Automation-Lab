# Lab: Clean Inputs (Ignore Comments) + Generate Report

This lab reads a list of domains from `config.txt`, cleans each line, ignores empty lines and comments, then generates a simple report file.

## Goal
- Build a clean list of domains from a text file.
- Ignore:
  - Empty lines
  - Comment lines that start with `#`
- Save the results into a report file.

## Project Files
- `config.txt` — input list (domains + optional comments)
- `dns_check.py` — script that reads and cleans inputs
- `loaded_domains_report.txt` — output report (generated)

## Example: config.txt
```txt
# comment
google.com
youtube.com
