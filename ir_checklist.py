# ir_checklist.py
# Incident Response Checklist Tool
# Day 1: Project setup and incident type definitions

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
# Entry point
# ─────────────────────────────────────────

if __name__ == "__main__":
    show_incident_types()
```

---

### requirements.txt
```
# No external dependencies required
# Built with Python 3.x standard library only
```
