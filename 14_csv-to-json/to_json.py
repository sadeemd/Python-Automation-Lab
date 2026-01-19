import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

csv_file = BASE_DIR / "report.csv"
json_file = BASE_DIR / "report.json"

rows = []

with csv_file.open("r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

with json_file.open("w", encoding="utf-8") as out:
    json.dump(rows, out, indent=2, ensure_ascii=False)

print("Converted CSV to JSON successfully.")
print("Input:", csv_file.name)
print("Output:", json_file.name)
print("Rows:", len(rows))
