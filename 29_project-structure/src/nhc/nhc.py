from pathlib import Path
from datetime import datetime
import csv

from dns import dns_check
from ports import port_check


def ensure_reports_dir() -> Path:
    # reports folder is at: 29_nhc/reports
    # this file is at: 29_nhc/src/nhc/nhc.py
    root = Path(__file__).resolve().parents[2]  # go up: nhc -> src -> 29_nhc
    reports = root / "reports"
    reports.mkdir(exist_ok=True)
    return reports


def save_csv_report(rows, out_path: Path) -> None:
    if not rows:
        return

    # collect all keys to make stable header
    keys = set()
    for r in rows:
        keys.update(r.keys())
    fieldnames = sorted(keys)

    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def run():
    # Targets (simple demo)
    dns_targets = ["google.com", "openai.com"]
    port_targets = [
        ("8.8.8.8", 53),      # DNS service (may be blocked)
        ("google.com", 443),  # HTTPS
    ]

    results = []

    # DNS checks
    for host in dns_targets:
        results.append(dns_check(host))

    # Port checks
    for host, port in port_targets:
        results.append(port_check(host, port))

    # Save report
    reports_dir = ensure_reports_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_file = reports_dir / f"nhc_report_{ts}.csv"
    save_csv_report(results, out_file)

    # Print summary
    ok_count = sum(1 for r in results if r.get("ok"))
    total = len(results)
    print(f"Done. Success: {ok_count}/{total}")
    print(f"Report: {out_file}")


if __name__ == "__main__":
    run()
