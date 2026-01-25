# Day 3 — HTTP Check (Status Code + Response Time)

## Overview
This lab checks a list of URLs and generates a CSV report that contains:
- HTTP status code (example: 200, 301, 403, 404, 500)
- Response time in milliseconds (ms)

The script reads URLs from `urls.txt`, sends an HTTP request with a User-Agent header, then saves results into `http_report.csv`.

---

## Files
- `urls.txt` → input list of URLs (one URL per line)
- `http_check.py` → script that performs HTTP checks
- `http_report.csv` → output report (generated after running)

---

## Folder Structure
your_lab_folder/
│
├─ urls.txt
├─ http_check.py
└─ http_report.csv   (created after running)

---

## What This Script Does
✅ Reads URLs from `urls.txt`  
✅ Ignores:
- empty lines
- comment lines starting with `#`  
✅ Sends HTTP request using `urllib.request`  
✅ Measures response time in milliseconds  
✅ Writes results to `http_report.csv` with columns:
- url
- status_code
- ms  
✅ Handles common failures safely:
- HTTPError → saves real status code (403/404/500)
- URLError → saves FAIL

---

## How It Works
- The script uses the same folder of the script:
  BASE_DIR = Path(__file__).resolve().parent

- Input file:
  urls.txt

- Output file:
  http_report.csv

- It adds a browser-like header:
  User-Agent: Mozilla/5.0

- Timeout:
  timeout = 5 seconds

Output format:
url,status_code,ms

---

## How To Run
Open terminal inside the lab folder and run:

python http_check.py

---

## Example Input (urls.txt)
https://www.google.com  
https://www.youtube.com  
https://www.microsoft.com  

---

## Example Output (http_report.csv)
url,status_code,ms  
https://www.google.com,200,120  
https://www.youtube.com,200,180  
https://www.microsoft.com,301,95  

---

## Terminal Output
Saved: .../http_report.csv

---

## Notes
- This lab tests HTTP response (not ping).
- Some websites may block requests and return 403.
- FAIL means the connection failed (DNS / timeout / blocked).

---

## Mini Challenge (Optional)
Upgrade the script to:
- Save the error type in a new column (example: HTTPError / URLError)
- Increase timeout for slow websites
- Print summary counts:
  - how many 200
  - how many FAIL
  - how many other codes
