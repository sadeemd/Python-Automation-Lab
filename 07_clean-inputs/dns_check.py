from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
config_path = BASE_DIR / "config.txt"
report_path = BASE_DIR / "loaded_domains_report.txt"

domains = []
for line in config_path.open("r", encoding="utf-8"):
    s = line.strip()
    if s and not s.startswith("#"):
        domains.append(s)

lines = []
lines.append(f"Report time: {datetime.now().isoformat(timespec='seconds')}")
lines.append(f"Loaded domains: {len(domains)}")
lines.append("-" * 30)
lines.extend(domains)

report_path.write_text("\n".join(lines), encoding="utf-8")

print("Loaded:", len(domains))
print("Saved report:", report_path.name)
