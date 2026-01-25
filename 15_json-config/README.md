# Day 15 — Read Settings from JSON (config.json)

## Overview
This lab demonstrates how to load program settings from a **JSON configuration file** instead of hardcoding values inside the Python script.

The script reads `config.json`, extracts:
- `hosts` (list of hostnames)
- `ports` (list of ports)

Then prints them to confirm everything loaded correctly.

---

## Files
- `config.json` — contains settings (hosts + ports)
- `checker.py` — reads JSON file and prints loaded values

---

## Folder Structure
your_lab_folder/
│
├─ config.json
└─ checker.py

---

## What This Script Does
✅ Checks if `config.json` exists  
✅ Loads JSON content using `json.load()`  
✅ Reads:
- `hosts`
- `ports`
✅ Prints the loaded settings

---

## Example config.json
```json
{
  "hosts": ["google.com"],
  "ports": [80, 443]
}
