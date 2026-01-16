from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
map_file = BASE_DIR / "rename_map.txt"

for line in map_file.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#") or "=>" not in line:
        continue

    old, new = [x.strip() for x in line.split("=>", 1)]
    old_path = BASE_DIR / old
    new_path = BASE_DIR / new

    if old_path.exists() and not new_path.exists():
        old_path.rename(new_path)
        print(f"Renamed: {old} -> {new}")
    else:
        print(f"Skipped: {old} -> {new}")
