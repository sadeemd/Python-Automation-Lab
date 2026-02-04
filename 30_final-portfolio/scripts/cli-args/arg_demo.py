import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument("--name", help="Your name")

    args = parser.parse_args()

    if not args.name:
        args.name = input("Enter your name: ").strip()

    message = f"Hello {args.name}"

    # ----- paths -----
    # scripts/cli-args/
    script_dir = Path(__file__).resolve().parent

    # 30_final-portfolio/reports/
    reports_dir = script_dir.parents[1] / "reports"

    if not reports_dir.exists():
        print("ERROR: reports folder not found.")
        return

    # ----- save report -----
    report_file = reports_dir / "cli_args_report.txt"
    report_file.write_text(message, encoding="utf-8")

    # ----- display -----
    print(message)
    print(f"Saved report: {report_file}")


if __name__ == "__main__":
    main()
