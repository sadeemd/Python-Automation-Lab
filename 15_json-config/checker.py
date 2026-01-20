import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
config_path = BASE_DIR / "config.json"

if not config_path.exists():
    print("config.json not found!")
    raise SystemExit

with config_path.open("r", encoding="utf-8") as f:
    cfg = json.load(f)

hosts = cfg.get("hosts", [])
ports = cfg.get("ports", [])

print("Hosts:", hosts)
print("Ports:", ports)
