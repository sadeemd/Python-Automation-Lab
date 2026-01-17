from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

src = BASE_DIR / "input.txt"
bak = BASE_DIR / "input.bak"

print("Running in:", BASE_DIR)
print("Looking for:", src)

if src.exists():
    bak.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    print("Backup created:", bak)
else:
    print("input.txt not found!")
