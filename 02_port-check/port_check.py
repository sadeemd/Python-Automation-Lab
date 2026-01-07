'''
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
'''            
#------------------------------------
import socket
import csv
from pathlib import Path

PORTS=[80,443]; TIMEOUT=2

def check(host: str, port: int):
    try:
        socket.create_connection((host, port), timeout=TIMEOUT).close()
        return "OK", "OPEN"
    except Exception as e:
        return "FAIL", str(e)

BASE_DIR = Path(__file__).resolve().parent
hosts_FILE = BASE_DIR / "hosts.txt"
report_FILE = BASE_DIR / "ports_report.csv"

with hosts_FILE.open("r", encoding="utf-8") as f:
    hosts = [s.strip() for s in f if s.strip() and not s.strip().startswith("#")]

with report_FILE.open("w", encoding="utf-8", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["host", "port", "status", "details"])
    for h in hosts:
        for p in PORTS:
            status, details = check(h, p)
            writer.writerow([h, p, status, details])