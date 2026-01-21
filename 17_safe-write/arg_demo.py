import argparse

def main():
    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument("--name", help="Your name")

    args = parser.parse_args()

    if not args.name:
        args.name = input("Enter your name: ").strip()

    print("Hello", args.name)

if __name__ == "__main__":
    main()
