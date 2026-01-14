from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
data_path = BASE_DIR / "data.txt"
cleaned_path = BASE_DIR / "cleaned.txt"

out = []
for line in data_path.open("r", encoding="utf-8"):
    parts = [p.strip() for p in line.split(",")]
    if len(parts) == 2:
        name, age = parts
        out.append(f"{name},{age}")

cleaned_path.write_text("\n".join(out), encoding="utf-8")
print("Saved:", cleaned_path)
