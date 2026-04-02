# ir_checklist.py
# Incident Response Checklist Tool
# Day 3: Added progress tracking functionality

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
    # Validate incident type
    if incident_type not in INCIDENTS:
        print(f"\n[ERROR] Unknown incident type: '{incident_type}'")
        print(f"Available types: {list(INCIDENTS.keys())}")
        return []

    incident = INCIDENTS[incident_type]
    checklist = []

    print(f"\n[✓] Generating checklist for: {incident['name']}")
    print(f"    Severity: {incident['severity']}")

    # Assign step numbers and build checklist items
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

    # Group steps by NIST phase for cleaner output
    current_phase = None
    for item in checklist:
        # Print phase header when phase changes
        if item["phase"] != current_phase:
            current_phase = item["phase"]
            print(f"\n  📋 {current_phase}")
            print(f"  {'-'*40}")

        # Show status indicator
        status_icon = "✅" if item["status"] == "Completed" else "⬜"
        print(f"  {status_icon} Step {item['step']:02d}: {item['action']}")

        # Show completion timestamp if step is completed
        if item["completed_at"]:
            print(f"           Completed at: {item['completed_at']}")

    # Calculate and display progress
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

            # Mark as completed and record timestamp
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
            # Exit session and show final progress
            print("\n[*] Session ended.")
            print_checklist(checklist, incident_type)
            break

        elif command == "status":
            # Show current progress without exiting
            print_checklist(checklist, incident_type)

        elif command.isdigit():
            # Mark specified step as complete
            step_number = int(command)
            mark_step_complete(checklist, step_number)

        else:
            print("[ERROR] Invalid command. Enter a step number, "
                  "'status', or 'done'.")


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
```
