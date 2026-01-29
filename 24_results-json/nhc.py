import json
from pathlib import Path


def read_items(path: Path) -> list[str]:
    items: list[str] = []

    text = path.read_text(encoding="utf-8", errors="ignore")
    for line in text.splitlines():
        line = line.strip()

        # ignore empty lines and comments
        if not line or line.startswith("#"):
            continue

        parts = line.split()

        # If hosts-like line: "IP domain"
        # Example: 0.0.0.0 example.com
        item = parts[1] if len(parts) >= 2 and parts[0].count(".") == 3 else parts[0]

        # remove optional port: example.com:443
        item = item.split(":")[0].strip()

        if item in {"localhost", "127.0.0.1"}:
            continue

        items.append(item)

    # deduplicate while preserving order
    seen = set()
    unique: list[str] = []
    for x in items:
        if x not in seen:
            unique.append(x)
            seen.add(x)

    return unique


def main():
    base_dir = Path(__file__).resolve().parent

    domains_file = base_dir / "domains.txt"
    hosts_file = base_dir / "hosts.txt"

    if domains_file.exists():
        input_file = domains_file
    elif hosts_file.exists():
        input_file = hosts_file
    else:
        print("ERROR: No input file found in the script folder.")
        print(f"Expected one of these files:\n- {domains_file}\n- {hosts_file}")
        print("\nCreate domains.txt (one domain per line) OR hosts.txt (IP domain).")
        return

    items = read_items(input_file)

    # Example output structure (replace status logic later if needed)
    results = [{"item": item, "status": "OK"} for item in items]

    out_file = base_dir / "results.json"
    out_file.write_text(
        json.dumps(results, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"Input : {input_file.name}")
    print(f"Items : {len(items)}")
    print(f"Saved : {out_file}")


if __name__ == "__main__":
    main()
