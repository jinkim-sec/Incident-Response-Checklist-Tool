# ir_checklist.py
# Incident Response Checklist Tool
# Day 4: Added CSV report generation

import csv
from datetime import datetime
from incidents import INCIDENTS


# ─────────────────────────────────────────
# Display available incident types
# ─────────────────────────────────────────

def show_incident_types():
    """
    Display all available incident types with their
    severity level and description.
    """
    print("\n" + "="*60)
    print("       INCIDENT RESPONSE CHECKLIST TOOL")
    print("="*60)
    print("\nAvailable incident types:\n")

    for key, incident in INCIDENTS.items():
        print(f"  [{key}]")
        print(f"  Name     : {incident['name']}")
        print(f"  Severity : {incident['severity']}")
        print(f"  Info     : {incident['description']}")
        print()


# ─────────────────────────────────────────
# Generate checklist for selected incident
# ─────────────────────────────────────────

def generate_checklist(incident_type):
    """
    Generate a NIST-based response checklist for the
    selected incident type.
    Groups steps by NIST IR phase and assigns a unique
    step number to each action.
    Returns a list of checklist item dicts.
    """
    if incident_type not in INCIDENTS:
        print(f"\n[ERROR] Unknown incident type: '{incident_type}'")
        print(f"Available types: {list(INCIDENTS.keys())}")
        return []

    incident = INCIDENTS[incident_type]
    checklist = []

    print(f"\n[✓] Generating checklist for: {incident['name']}")
    print(f"    Severity: {incident['severity']}")

    for i, step in enumerate(incident["steps"], start=1):
        checklist.append({
            "step": i,
            "phase": step["phase"],
            "action": step["action"],
            "status": "Pending",
            "completed_at": None
        })

    return checklist


# ─────────────────────────────────────────
# Print checklist to terminal
# ─────────────────────────────────────────

def print_checklist(checklist, incident_type):
    """
    Display the generated checklist in a formatted
    terminal output grouped by NIST IR phase.
    Shows completion status and timestamp for each step.
    """
    if not checklist:
        return

    incident = INCIDENTS[incident_type]

    print("\n" + "="*60)
    print(f"  {incident['name'].upper()} — RESPONSE CHECKLIST")
    print("="*60)

    current_phase = None
    for item in checklist:
        if item["phase"] != current_phase:
            current_phase = item["phase"]
            print(f"\n  📋 {current_phase}")
            print(f"  {'-'*40}")

        status_icon = "✅" if item["status"] == "Completed" else "⬜"
        print(f"  {status_icon} Step {item['step']:02d}: {item['action']}")

        if item["completed_at"]:
            print(f"           Completed at: {item['completed_at']}")

    completed = len([i for i in checklist if i["status"] == "Completed"])
    total = len(checklist)
    percentage = (completed / total * 100) if total > 0 else 0

    print(f"\n{'='*60}")
    print(f"  Progress : {completed}/{total} steps completed "
          f"({percentage:.0f}%)")
    print("="*60 + "\n")


# ─────────────────────────────────────────
# Progress tracking - mark step as complete
# ─────────────────────────────────────────

def mark_step_complete(checklist, step_number):
    """
    Mark a specific checklist step as completed.
    Records the completion timestamp automatically.
    Returns True if successful, False if step not found
    or already completed.
    """
    for item in checklist:
        if item["step"] == step_number:
            if item["status"] == "Completed":
                print(f"[WARNING] Step {step_number} is already completed.")
                return False

            item["status"] = "Completed"
            item["completed_at"] = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            print(f"[✓] Step {step_number:02d} marked as completed.")
            return True

    print(f"[ERROR] Step {step_number} not found in checklist.")
    return False


# ─────────────────────────────────────────
# Progress tracking - interactive session
# ─────────────────────────────────────────

def run_interactive_session(checklist, incident_type):
    """
    Run an interactive checklist session where the analyst
    can mark steps as completed one by one.
    Type 'done' to exit the session at any time.
    Type 'status' to view current progress.
    """
    print("\n[*] Starting interactive checklist session...")
    print("    Commands:")
    print("    - Enter step number to mark as complete")
    print("    - 'status' to view current progress")
    print("    - 'done' to finish session\n")

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "done":
            print("\n[*] Session ended.")
            print_checklist(checklist, incident_type)
            break

        elif command == "status":
            print_checklist(checklist, incident_type)

        elif command.isdigit():
            step_number = int(command)
            mark_step_complete(checklist, step_number)

        else:
            print("[ERROR] Invalid command. Enter a step number, "
                  "'status', or 'done'.")


# ─────────────────────────────────────────
# Report generation
# ─────────────────────────────────────────

def save_report(checklist, incident_type, filename=None):
    """
    Export the completed checklist to a timestamped CSV report.
    Includes incident metadata, step details, completion status,
    and a summary of overall progress.
    If no filename is provided, one is auto-generated with
    the current timestamp.
    """
    if not checklist:
        print("[WARNING] No checklist data to save.")
        return

    incident = INCIDENTS[incident_type]

    # Auto-generate filename if not provided
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ir_report_{incident_type}_{timestamp}.csv"

    # Calculate progress summary
    completed = len([i for i in checklist if i["status"] == "Completed"])
    total = len(checklist)
    percentage = (completed / total * 100) if total > 0 else 0

    fieldnames = [
        "incident_type", "incident_name", "severity",
        "step", "phase", "action",
        "status", "completed_at"
    ]

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for item in checklist:
            writer.writerow({
                "incident_type": incident_type,
                "incident_name": incident["name"],
                "severity": incident["severity"],
                "step": item["step"],
                "phase": item["phase"],
                "action": item["action"],
                "status": item["status"],
                "completed_at": item["completed_at"] or "N/A"
            })

    print(f"\n[✓] Report saved: {filename}")
    print(f"    Progress: {completed}/{total} steps completed "
          f"({percentage:.0f}%)")


# ─────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────

if __name__ == "__main__":
    # Show available incident types
    show_incident_types()

    # Prompt user to select an incident type
    print("Enter incident type to generate checklist: ", end="")
    incident_type = input().strip().lower()

    # Generate checklist
    checklist = generate_checklist(incident_type)

    if checklist:
        # Display full checklist
        print_checklist(checklist, incident_type)

        # Start interactive tracking session
        run_interactive_session(checklist, incident_type)

        # Save report after session ends
        save_report(checklist, incident_type)
```
