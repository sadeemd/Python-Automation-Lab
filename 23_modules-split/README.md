# Day 23 — Modules (dns.py + nhc.py)

## What it does
Splits the project into two Python modules: `dns.py` for DNS resolving and `nhc.py` as the main program that asks for a domain and prints its IP.

## Inputs
- Domain name from the user (example: `google.com`).

## Outputs
- Prints the resolved IPv4 address (example: `google.com -> 142.250.xxx.xxx`).
- If the domain is invalid or there is no internet, it prints an error message.

## How to run
1) Put these files in the same folder:
   - `dns.py`
   - `nhc.py`
   - `README.md`
2) Open terminal in that folder and run:
```bash
python nhc.py
