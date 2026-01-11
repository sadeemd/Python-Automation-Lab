from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
log_file = BASE_DIR / "run_sample.txt"
summary_file = BASE_DIR / "summary.txt"

ok = 0
fail = 0

with log_file.open("r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        if "-> OK" in line:
            ok += 1
        if "-> FAIL" in line:
            fail += 1

with summary_file.open("w", encoding="utf-8") as out:
    out.write(f"OK lines: {ok}\n")
    out.write(f"FAIL lines: {fail}\n")

print("OK lines:", ok)
print("FAIL lines:", fail)
