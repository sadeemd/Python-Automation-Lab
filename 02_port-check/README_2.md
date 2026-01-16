# Port Check (TCP)

Simple TCP port checker that reads hosts from 'hosts.txt' and generates 'ports_report.csv'.

## Files
- 'hosts.txt': list of hosts (one per line). Lines starting with '#' are ignored.
- 'port_check.py': runs the checks for ports 80 and 443 and writes a CSV report.

## Run
```bash
python port_check.py
