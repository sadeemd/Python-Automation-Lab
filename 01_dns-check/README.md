# Day 1 — DNS Check (Resolve Domains → CSV Report)

## Overview
This lab checks whether a list of domains can be resolved to an IP address using DNS.

The script reads domains from `domains.txt`, tries to resolve each domain using:
`socket.gethostbyname()`

Then it generates a CSV report file: `report.csv` with the result of each domain.

---

## Files
- `dns_check.py` → reads domains and writes results to CSV
- `domains.txt` → input list of domains (one per line)
- `report.csv` → output report (generated after running)

---

## Folder Structure
your_lab_folder/
│
├─ dns_check.py
├─ domains.txt
└─ report.csv   (created after running)

---

## What This Script Does
✅ Reads domain names from `domains.txt`  
✅ Ignores:
- empty lines
- comment lines starting with `#`  
✅ Resolves each domain using `socket.gethostbyname()`  
✅ Writes results to `report.csv` with columns:
- domain
- status (OK / FAIL)
- ip_or_error (resolved IP or error message)

---

## How It Works
- The script runs using the same folder where it exists:
  BASE_DIR = Path(__file__).resolve().parent

- Input file:
  domains.txt

- Output file:
  report.csv

- Result logic:
  - If the domain resolves → status = OK and saves the IP
  - If it fails → status = FAIL and saves the error text

CSV format:
domain,status,ip_or_error

---

## How To Run
Open terminal inside the lab folder and run:

python dns_check.py

---

## Example Input (domains.txt)
google.com  
youtube.com  
microsoft.com  
facebook.com  

---

## Example Output (report.csv)
domain,status,ip_or_error  
google.com,OK,142.250.186.14  
youtube.com,OK,142.250.186.14  
microsoft.com,OK,20.81.111.85  
facebook.com,OK,157.240.229.35  

(Your IP results may differ depending on DNS.)

---

## Notes
- This lab checks DNS resolution only (not ping).
- Useful for:
  - quick DNS troubleshooting
  - validating domain lists
  - preparing targets for other network scripts

---

## Mini Challenge (Optional)
Upgrade the script to:
- Add a timeout / retry logic
- Save the date/time in the report
- Count how many OK vs FAIL and print summary at the end
- Use `socket.getaddrinfo()` to support IPv6 too
