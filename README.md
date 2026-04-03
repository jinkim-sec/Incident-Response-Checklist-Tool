# Incident Response Checklist Tool

A Python tool that generates NIST-based incident response
checklists for common cybersecurity incidents. Analysts can
work through each step interactively, track progress in
real time, and export a completed report to CSV.
Built as part of a cybersecurity learning portfolio to
demonstrate incident response concepts used in real-world
SOC environments.

## Features
- Generates structured checklists based on the NIST IR framework
- Supports four incident types: phishing, ransomware,
  brute force, and data exfiltration
- Interactive step-by-step checklist session
- Tracks completion status and timestamps for each step
- Displays real-time progress percentage
- Exports completed checklist to a timestamped CSV report
- Input validation with clear error messages

## Requirements
- Python 3.x
- No external libraries required

## Usage
```bash
python ir_checklist.py
```

Select an incident type when prompted:

Available types: phishing, ransomware, brute_force, data_exfiltration

## Supported Incident Types

| Type | Name | Severity |
|------|------|----------|
| `phishing` | Phishing Attack | HIGH |
| `ransomware` | Ransomware Attack | CRITICAL |
| `brute_force` | Brute Force Attack | MEDIUM |
| `data_exfiltration` | Data Exfiltration | CRITICAL |

## Interactive Commands

| Command | Action |
|---------|--------|
| `1`, `2`, `3`... | Mark step number as completed |
| `status` | View current progress |
| `done` | End session and save report |

## Example Output
============================================================
INCIDENT RESPONSE CHECKLIST TOOL
Available incident types:
[phishing]
Name     : Phishing Attack
Severity : HIGH
Info     : A deceptive email or message designed to trick
users into revealing credentials or downloading
malicious content.
Enter incident type: phishing
[✓] Generating checklist for: Phishing Attack
Severity: HIGH
============================================================
PHISHING ATTACK — RESPONSE CHECKLIST
📋 Detection & Analysis
⬜ Step 01: Identify and quarantine the suspicious email
⬜ Step 02: Extract and document email headers, sender
address, and embedded URLs
...
============================================================
Progress : 0/13 steps completed (0%)
[*] Starting interactive checklist session...
Commands:
- Enter step number to mark as complete
- 'status' to view current progress
- 'done' to finish and save report
Enter command: 1
[✓] Step 01 marked as completed.
Enter command: done
[*] Session ended.
============================================================
Progress : 1/13 steps completed (8%)
[✓] Report saved: ir_report_phishing_20251101_142500.csv
Progress: 1/13 steps completed (8%)

## NIST IR Phases Covered

Each checklist follows the NIST incident response lifecycle:

1. **Detection & Analysis** — Identify and assess the incident
2. **Containment** — Limit the spread and impact
3. **Eradication** — Remove the threat from the environment
4. **Recovery** — Restore normal operations
5. **Post-Incident Activity** — Document and improve

## Project Structure
incident-response-checklist/
│
├── ir_checklist.py        # Main script
├── incidents.py           # Incident type definitions
├── requirements.txt       # Dependencies
├── README.md
├── .gitignore
└── LICENSE

## Key Concepts Demonstrated
- NIST incident response framework
- Structured incident handling methodology
- Progress tracking and status management
- Automated report generation
- Input validation and error handling

## Disclaimer
This tool is for educational purposes only.
Checklists are based on general best practices and should
be adapted to your organisation's specific policies and
procedures.

## Author
Jin Hyuck Kim
github.com/[jinkim-sec]
