# 03_http-check (HTTP Status + Response Time)

A simple Python lab that checks a list of URLs and generates a CSV report containing:
- HTTP status code (e.g., 200, 301, 403, 404, 500)
- Response time in milliseconds (ms)

## Files
- `urls.txt` : Input list of URLs (one URL per line)
- `http_check.py` : Script that performs the checks
- `http_report.csv` : Output report (generated after running the script)

## Requirements
- Python 3.x (no external libraries required)

## Setup
1) Put your URLs in `urls.txt` (one per line).
2) Run the script:
   ```bash
   python http_check.py
