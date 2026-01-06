import socket
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DOMAINS_FILE = BASE_DIR / "domains.txt"
REPORT_FILE = BASE_DIR / "report.csv"

with DOMAINS_FILE.open("r", encoding="utf-8") as f:
    domains = [s.strip() for s in f if s.strip() and not s.strip().startswith("#")]

with REPORT_FILE.open("w", encoding="utf-8", newline="") as out:
    out.write("domain,status,ip_or_error\n")
    for d in domains:
        try:
            ip = socket.gethostbyname(d)
            out.write(f"{d},OK,{ip}\n")
        except Exception as e:
            out.write(f'{d},FAIL,"{e}"\n')
