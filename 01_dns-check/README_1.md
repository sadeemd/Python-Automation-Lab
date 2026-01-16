# DNS Check — Domains Resolver Report

## Files
- `dns_check.py` — Reads `domains.txt`, resolves each domain to an IP, and writes results to `report.csv`. :contentReference[oaicite:0]{index=0}  
- `domains.txt` — List of domains to check (one per line). :contentReference[oaicite:1]{index=1}  
- `report.csv` — Output report: `domain,status,ip_or_error`.

## Input Format (`domains.txt`)
- One domain per line
- Empty lines are ignored
- Lines starting with `#` are ignored

Example:
```txt
google.com
youtube.com
microsoft.com
facebook.com
