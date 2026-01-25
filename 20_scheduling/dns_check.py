from pathlib import Path
from datetime import datetime
import socket

# ----------------------------
# DNS Check (Test Version)
# ----------------------------

BASE_DIR = Path(__file__).resolve().parent
REPORT_PATH = BASE_DIR / "dns_report.txt"

DOMAINS = [
    "google.com",
    "youtube.com",
    "microsoft.com",
    "openai.com",
    "example.com",
]

lines = []
lines.append("DNS CHECK REPORT")
lines.append(f"Time: {datetime.now().isoformat(timespec='seconds')}")
lines.append("-" * 50)

ok_count = 0
for d in DOMAINS:
    try:
        ip = socket.gethostbyname(d)
        lines.append(f"[OK]   {d:<20} -> {ip}")
        ok_count += 1
    except Exception as e:
        lines.append(f"[FAIL] {d:<20} -> {e}")

lines.append("-" * 50)
lines.append(f"Resolved: {ok_count}/{len(DOMAINS)}")

REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")

print("DNS report saved to:", REPORT_PATH)
