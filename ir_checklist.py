# ir_checklist.py
# Incident Response Checklist Tool
# Day 2: Added checklist generation logic

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
            "status": "Pending",  # Default status for all steps
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

    print(f"\n{'='*60}")
    print(f"  Total steps: {len(checklist)}")
    print("="*60 + "\n")


# ─────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────

if __name__ == "__main__":
    # Show available incident types
    show_incident_types()

    # Prompt user to select an incident type
    print("Enter incident type to generate checklist: ", end="")
    incident_type = input().strip().lower()

    # Generate and display checklist
    checklist = generate_checklist(incident_type)
    if checklist:
        print_checklist(checklist, incident_type)
```
