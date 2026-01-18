from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
numbers_file = BASE_DIR / "numbers.txt"

nums = [int(s.strip()) for s in numbers_file.open("r", encoding="utf-8") if s.strip()]

if not nums:
    print("File is empty. No numbers to analyze.")
    exit()

avg = sum(nums) / len(nums)

print("count", len(nums))
print("min", min(nums), "max", max(nums), "avg", avg)
