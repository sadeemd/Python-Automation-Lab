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