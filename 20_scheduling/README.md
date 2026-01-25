# Day 20 — Scheduling (Windows Only)

## Goal
Run multiple Python scripts automatically every day on Windows using one runner file.

This lab demonstrates how to:
- Run multiple scripts using one `.bat` file
- Generate reports (`.txt`) automatically
- Store a log file for troubleshooting
- Schedule the runner daily using Windows Task Scheduler

## Folder Structure
Put all files in the same folder:

20_scheduling/
- daily_run.bat
- dns_check.py
- port_check.py
- README.md

## What Each File Does

dns_check.py:
- Checks DNS resolution for a list of domains (example: google.com)
- Creates a report file named: dns_report.txt

port_check.py:
- Checks if some ports are open/closed for selected hosts
- Creates a report file named: port_report.txt

daily_run.bat:
- Runs both scripts automatically in order
- Saves all output into a log file named: daily_log.txt
- Ensures it runs from the correct folder to avoid path errors

## How to Run (Manual)
1) Double-click: daily_run.bat
2) Wait until it finishes
3) You will see: Done + generated reports

## Expected Output Files
After running daily_run.bat, you should get:
- dns_report.txt
- port_report.txt
- daily_log.txt

## Scheduling with Windows Task Scheduler (Daily Run)
1) Open Task Scheduler
2) Click Create Basic Task
3) Name it: Daily Python Reports
4) Trigger: Daily
5) Choose your preferred time (example: 09:00 PM)
6) Action: Start a program
7) Browse and select daily_run.bat
8) Finish

Now the scripts will run automatically every day.

## Troubleshooting
If you get: "python is not recognized"
Edit daily_run.bat and replace:
python dns_check.py
with your full Python path, for example:
"C:\Users\LOQ\AppData\Local\Programs\Python\Python312\python.exe" dns_check.py

## Deliverable
A working daily automation setup that runs two scripts, creates reports, and logs results automatically.
