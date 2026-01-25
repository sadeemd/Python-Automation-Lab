# Day 2 — Port Check (TCP 80/443) + CSV Report

## Overview
This lab performs a simple **TCP port check** for a list of hosts.

It reads hosts from `hosts.txt`, then checks connectivity for these ports:
- 80 (HTTP)
- 443 (HTTPS)

The script generates a CSV report file: `ports_report.csv`.

---

## Files
- `hosts.txt` → input list of hosts (one host per line)
- `port_check.py` → script that checks ports 80 and 443
- `ports_report.csv` → output report (generated after running)

---

## Folder Structure
your_lab_folder/
│
├─ hosts.txt
├─ port_check.py
└─ ports_report.csv   (created after running)

---

## What This Script Does
✅ Reads hosts from `hosts.txt`  
✅ Ignores:
- empty lines
- comment lines starting with `#`  
✅ Checks each host using TCP connection:
- port 80
- port 443  
✅ Writes results to `ports_report.csv` with columns:
- host
- port
- status (OK / FAIL)
- details (OPEN or error message)

---

## How It Works
- The script uses:
  BASE_DIR = Path(__file__).resolve().parent
So all files are read/written inside the same folder of the script.

- It checks ports with:
  socket.create_connection((host, port), timeout=2)

If connection succeeds:
- status = OK
- details = OPEN

If it fails:
- status = FAIL
- details = error message

---

## How To Run
Open terminal inside the lab folder and run:

python port_check.py

---

## Example Input (hosts.txt)
google.com  
youtube.com  
microsoft.com  
facebook.com  

---

## Example Output (ports_report.csv)
host,port,status,details  
google.com,80,OK,OPEN  
google.com,443,OK,OPEN  
youtube.com,80,OK,OPEN  
youtube.com,443,OK,OPEN  

(If a port is blocked or unreachable, it will show FAIL with the reason.)

---

## Notes
- This lab checks **TCP connectivity**, not ICMP ping.
- Useful for:
  - quick network checks
  - verifying if web ports are reachable
  - basic troubleshooting for servers/services

---

## Mini Challenge (Optional)
Upgrade the script to:
- Add more ports (example: 22, 53, 3306)
- Save response time (ms) for each connection
- Print a summary at the end (OK count vs FAIL count)
- Allow ports to be loaded from a config file
