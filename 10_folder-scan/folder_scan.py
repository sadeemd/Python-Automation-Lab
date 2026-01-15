from pathlib import Path
from datetime import datetime

def human_size(num_bytes: int) -> str:
    units = ["B", "KB", "MB", "GB"]
    size = float(num_bytes)
    for u in units:
        if size < 1024 or u == units[-1]:
            return f"{size:.1f} {u}"
        size /= 1024

# ✅ هذا يخلي الحفظ داخل نفس فولدر السكربت 100%
p = Path(__file__).resolve().parent
report_file = p / "folder_report.txt"

files = []
for f in p.iterdir():
    if f.is_file() and f.name != report_file.name:
        files.append((f.name, f.stat().st_size))

files.sort(key=lambda x: x[1], reverse=True)

lines = []
lines.append(f"Folder: {p}")
lines.append(f"Report time: {datetime.now().isoformat(timespec='seconds')}")
lines.append("-" * 60)
lines.append(f"{'File Name':40} {'Size':>15}")
lines.append("-" * 60)

for name, size in files:
    lines.append(f"{name:40} {human_size(size):>15}")

lines.append("-" * 60)
lines.append(f"Total files: {len(files)}")

print("\n".join(lines))
report_file.write_text("\n".join(lines), encoding="utf-8")

print("\n✅ Report saved here:")
print(report_file)
