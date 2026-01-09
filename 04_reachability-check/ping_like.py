import socket
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
hosts_FILE = BASE_DIR / "hosts.txt"
REPORT_FILE = BASE_DIR / "REPORT_FILE.csv"

with hosts_FILE.open("r", encoding="utf-8") as f:
    hosts = [s.strip() for s in f if s.strip() and not s.strip().startswith("#")]

#hosts=[s.strip() for s in open("hosts.txt") if s.strip()]
with REPORT_FILE.open("w", encoding="utf-8") as out:
    out.write("host,resolves\n")
    for h in hosts:
        try:
            socket.gethostbyname(h)   # للـIP يرجع نفسـه
            out.write(f"{h},YES\n")
        except Exception:
            out.write(f"{h},NO\n")