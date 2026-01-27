# nhc.py  (Day 22)

def clean_items(items):
    # ترجع قائمة بعد التنظيف: strip + حذف الفارغ + حذف التعليقات
    return [s.strip() for s in items if s.strip() and not s.strip().startswith("#")]

# قائمة داخل الكود (بدون ملف)
domains = [
    " google.com  ",
    "",
    "# comment line",
    "openai.com",
    "  example.org ",
    "   # another comment",
    "github.com",
]

print(clean_items(domains))
