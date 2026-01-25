# Day 18 — Simple Countdown Timer (time.sleep)

## Overview
This lab demonstrates a simple countdown timer using Python’s `time.sleep()` function.

Timers and delays are common in automation scripts (for example: waiting before retrying a request, giving time for a file to load, or pacing tasks).

---

## Files
- `timer.py` → countdown timer script (no input files required)

---

## What This Script Does
✅ Counts down from 5 to 1  
✅ Prints a message every 1 second  
✅ Prints `GO` at the end

---

## How It Works
The script uses a loop:

- `range(5, 0, -1)` means:
  - start at **5**
  - stop before **0**
  - step **-1** (counting down)

Then it pauses for 1 second between each step using:
- `time.sleep(1)`

---

## How To Run
Open terminal in the same folder, then run:

python timer.py

---

## Example Output
starting in 5  
starting in 4  
starting in 3  
starting in 2  
starting in 1  
GO  

---

## Mini Challenge (Optional)
Try improving the script:
- Allow the user to enter the number of seconds
- Print a nicer format like: `T-minus 5...`
- Add a short beep sound (optional)
