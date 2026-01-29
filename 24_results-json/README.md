# Day 24 — Collect Results and Save JSON (results.json)

This lab demonstrates how to collect results into a list of dictionaries (dicts) and export them to a JSON file.

Folder Structure:
24_results-json/
- nhc.py
- domains.txt (or hosts.txt)
- results.json (generated after running)

Input Files:
Option 1: domains.txt (one domain per line)
example.com
google.com
openai.com

Option 2: hosts.txt (IP + domain)
0.0.0.0 ads.example.com
127.0.0.1 example.com

The script automatically uses domains.txt if it exists; otherwise it uses hosts.txt.

What nhc.py Does:
- Reads domains.txt or hosts.txt from the same folder as nhc.py
- Ignores empty lines and # comments
- Extracts domain names (supports hosts format)
- Removes duplicates while preserving order
- Builds results as a list of dicts like:
  [{"item":"example.com","status":"OK"}]
- Saves output to results.json

How to Run (Windows PowerShell):
cd "d:\courses\En + Ai + Github\Chat GPT course\Python-Automation-Lab\24_results-json"
python nhc.py

Output:
After running, results.json will be created in the same folder.

Notes:
The "status" field is a placeholder for now; later you can replace it with real checks (DNS/HTTP/etc.).
