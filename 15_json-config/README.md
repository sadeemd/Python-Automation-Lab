# Day 15 - Read Settings from JSON (config.json)

## Goal
Load program settings from a JSON file instead of hardcoding them in the Python script.

## Files
- `config.json` : Contains hosts and ports
- `checker.py` : Reads the JSON file and prints the loaded settings

## Example config.json
```json
{
  "hosts": ["google.com"],
  "ports": [80, 443]
}
