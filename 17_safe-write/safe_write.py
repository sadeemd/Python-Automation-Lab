from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

tmp = BASE_DIR / "out.tmp"
final = BASE_DIR / "out.txt"

content = "new content"

# 1) Write to temp file inside the same folder
tmp.write_text(content, encoding="utf-8")

# 2) Replace final file atomically inside the same folder
tmp.replace(final)

print("Atomic write done ✅")
print("Saved:", final)
