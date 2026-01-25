from pathlib import Path
from datetime import datetime
import socket

# ----------------------------
# Port Check (Test Version)
# ----------------------------

BASE_DIR = Path(__file__).resolve().parent
REPORT_PATH = BASE_DIR / "port_report.txt"

# (host, port) test list
TARGETS = [
    ("google.com", 80),
    ("google.com", 443),
    ("example.com", 80),
    ("localhost", 80),
]

TIMEOUT_SEC = 2

lines = []
lines.append("PORT CHECK REPORT")
lines.append(f"Time: {datetime.now().isoformat(timespec='seconds')}")
lines.append("-" * 50)

open_count = 0
for host, port in TARGETS:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT_SEC)

    try:
        result = s.connect_ex((host, port))  # 0 means open
        if result == 0:
            lines.append(f"[OPEN]  {host:<15}:{port}")
            open_count += 1
        else:
            lines.append(f"[CLOSED] {host:<15}:{port}")
    except Exception as e:
        lines.append(f"[ERROR] {host:<15}:{port} -> {e}")
    finally:
        s.close()

lines.append("-" * 50)
lines.append(f"Open ports: {open_count}/{len(TARGETS)}")

REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")

print("Port report saved to:", REPORT_PATH)
