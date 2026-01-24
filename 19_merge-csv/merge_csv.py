import csv
from pathlib import Path

# نفس مكان الملف الحالي
BASE_DIR = Path(__file__).resolve().parent

INPUT_DIR = BASE_DIR / "multi_reports"
OUTPUT_FILE = BASE_DIR / "merged.csv"

files = sorted(INPUT_DIR.glob("*.csv"))

all_rows = []
all_fields = set()

for f in files:
    with f.open("r", newline="", encoding="utf-8") as h:
        reader = csv.DictReader(h)
        for row in reader:
            # إذا تريد تعرف كل صف من أي ملف إجا
            row["source_file"] = f.name

            all_rows.append(row)
            all_fields.update(row.keys())

if not all_rows:
    print("No rows found. Make sure multi_reports has CSV files with data.")
else:
    fieldnames = sorted(all_fields)

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as out:
        w = csv.DictWriter(out, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(all_rows)

    print("Merged files:", len(files))
    print("Total rows:", len(all_rows))
    print("Saved:", OUTPUT_FILE)
