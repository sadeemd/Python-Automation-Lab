# Day 18 — Simple Delay/Timer (Countdown)

This lab demonstrates a simple countdown timer using Python’s `time.sleep()` function.
Delays are very common in automation scripts (e.g., waiting before retrying a request, giving time for a file to appear, or pacing operations).

---

## Files

- `timer.py` → countdown timer script (no input files required)

---

## What This Script Does

✅ Counts down from 5 to 1  
✅ Prints a message every second  
✅ Prints `"GO"` at the end

---

## Code Overview

The script runs a loop:

- `range(5, 0, -1)` means:
  - start at **5**
  - stop before **0**
  - step **-1** (count down)

Then it waits 1 second between each print using:

- `time.sleep(1)`

---

## How to Run

From the terminal inside the lab folder:

```bash
python timer.py
