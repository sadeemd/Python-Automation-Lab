import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input.csv"
OUTPUT_FILE = BASE_DIR / "filtered.csv"

with INPUT_FILE.open("r", newline="", encoding="utf-8") as f, \
     OUTPUT_FILE.open("w", newline="", encoding="utf-8") as out:

    r = csv.DictReader(f)
    w = csv.DictWriter(out, fieldnames=r.fieldnames)
    w.writeheader()

    for row in r:
        if row["status"] == "OK":
            w.writerow(row)

print("Done:", OUTPUT_FILE)
