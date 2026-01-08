from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
URLS_FILE = BASE_DIR / "urls.txt"
REPORT_FILE = BASE_DIR / "http_report.csv"

with URLS_FILE.open("r", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]

headers = {"User-Agent": "Mozilla/5.0"}

with REPORT_FILE.open("w", encoding="utf-8") as out:
    out.write("url,status_code,ms\n")

    for url in urls:
        t0 = time.time()
        try:
            req = Request(url, headers=headers)
            with urlopen(req, timeout=5) as r:
                code = r.getcode()
            ms = int((time.time() - t0) * 1000)
            out.write(f"{url},{code},{ms}\n")

        except HTTPError as e:
            # هذا هم status_code حقيقي (مثل 403/404/500)
            ms = int((time.time() - t0) * 1000)
            out.write(f"{url},{e.code},{ms}\n")

        except URLError:
            ms = int((time.time() - t0) * 1000)
            out.write(f"{url},FAIL,{ms}\n")

print(f"Saved: {REPORT_FILE}")
