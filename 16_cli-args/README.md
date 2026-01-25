# Day 16 — Argparse Demo (Command Line Arguments)

## Overview
This lab demonstrates how to use Python `argparse` to accept command-line arguments.

The script prints a greeting message:
- If you provide `--name` from the terminal → it uses it directly
- If you don’t provide `--name` → it asks you to type your name manually

---

## Files
- `arg_demo.py` — main script

---

## What This Script Does
✅ Creates a command-line argument: `--name`  
✅ Reads user input if `--name` is missing  
✅ Prints: `Hello <name>`

---

## How It Works
The script uses:

- `argparse.ArgumentParser()` to define arguments
- `parser.add_argument("--name", help="Your name")` to create an optional argument
- `parser.parse_args()` to read arguments from the terminal

Logic:
- If `--name` is not provided:
  - the script asks you to type the name using `input()`

---

## How To Run

### ✅ Option 1: Run with command-line argument
Open terminal in the same folder and run:

python arg_demo.py --name Sadeem

Expected output:
Hello Sadeem

---

### ✅ Option 2: Run without argument (interactive)
python arg_demo.py

It will ask:
Enter your name:

Then output:
Hello <your_name>

---

## Notes
- `--name` is optional, not required.
- This technique is useful in automation scripts because it lets you run programs with different inputs without editing the code.

---

## Mini Challenge (Optional)
Upgrade the script:
- Add another argument like `--age`
- Print a full message:
  Hello Sadeem, you are 30 years old.
- Make `--name` required using:
  required=True
