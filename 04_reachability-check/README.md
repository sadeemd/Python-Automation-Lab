# Day 4 — DNS Resolve Checker (Reachability - Resolve Only)

## Overview
This lab checks **DNS resolution** (not a real ping).

It reads a list of hosts from `hosts.txt`, then tries to resolve each host using:
`socket.gethostbyname()`

Finally, it saves a CSV report showing whether each host resolves successfully.

---

## Files
- `hosts.txt` → input targets (one host per line)
- `ping_like.py` → script that resolves hosts using DNS
- `REPORT_FILE.csv` → output report (generated after running)

---

## Folder Structure
your_lab_folder/
│
├─ hosts.txt
├─ ping_like.py
└─ REPORT_FILE.csv   (created after running)

---

## What This Script Does
✅ Reads hosts from `hosts.txt`  
✅ Ignores:
- empty lines
- comment lines that start with `#`  
✅ Tries to resolve each host with `socket.gethostbyname()`  
✅ Writes results into `REPORT_FILE.csv` with columns:
- host
- resolves (YES / NO)

---

## How It Works
- The script uses the same folder of the script:
  `BASE_DIR = Path(__file__).resolve().parent`

- Input file:
  `hosts.txt`

- Output file:
  `REPORT_FILE.csv`

- For each host:
  - If DNS resolves → writes `YES`
  - If DNS fails → writes `NO`

Important note:
This lab checks **resolution only**.
It does not test network reachability (ICMP ping).

---

## How To Run
Open terminal inside the lab folder and run:

python ping_like.py

---

## Example Input (hosts.txt)
8.8.8.8  
1.1.1.1  
youtube.com  
microsoft.com  
facebook.com  

---

## Example Output (REPORT_FILE.csv)
host,resolves  
8.8.8.8,YES  
1.1.1.1,YES  
youtube.com,YES  
microsoft.com,YES  
facebook.com,YES  

---

## Notes
- `socket.gethostbyname()` resolves domains to an IP address.
- If the input is already an IP (مثل 8.8.8.8) غالباً يرجعه نفسه ويكون YES.
- This is useful for:
  - checking DNS issues quickly
  - validating domain lists
  - pre-check before real network tests

---

## Mini Challenge (Optional)
Upgrade the script to:
- Save the resolved IP in the report (host, ip, resolves)
- Add a timeout using socket settings
- Count how many YES/NO and print summary at the end
