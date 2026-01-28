# nhc.py
from dns import resolve

def main():
    domain = input("Enter domain (e.g., google.com): ").strip()
    if not domain:
        print("Empty domain.")
        return

    try:
        ip = resolve(domain)
        print(f"{domain} -> {ip}")
    except Exception as e:
        print(f"Failed to resolve '{domain}': {e}")

if __name__ == "__main__":
    main()
