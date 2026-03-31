# incidents.py
# Incident type definitions and NIST-based response checklists
# Each incident type contains a list of response steps
# organised by NIST IR phases:
# 1. Preparation
# 2. Detection & Analysis
# 3. Containment
# 4. Eradication
# 5. Recovery
# 6. Post-Incident Activity

INCIDENTS = {
    "phishing": {
        "name": "Phishing Attack",
        "severity": "HIGH",
        "description": "A deceptive email or message designed to "
                       "trick users into revealing credentials or "
                       "downloading malicious content.",
        "steps": [
            # Detection & Analysis
            {
                "phase": "Detection & Analysis",
                "action": "Identify and quarantine the suspicious email"
            },
            {
                "phase": "Detection & Analysis",
                "action": "Extract and document email headers, "
                          "sender address, and embedded URLs"
            },
            {
                "phase": "Detection & Analysis",
                "action": "Check URLs and attachments against "
                          "threat intelligence sources (e.g. VirusTotal)"
            },
            {
                "phase": "Detection & Analysis",
                "action": "Identify all recipients of the phishing email"
            },
            # Containment
            {
                "phase": "Containment",
                "action": "Block the malicious sender domain at "
                          "the email gateway"
            },
            {
                "phase": "Containment",
                "action": "Remove the phishing email from all "
                          "affected mailboxes"
            },
            {
                "phase": "Containment",
                "action": "Reset credentials of any users who clicked "
                          "links or submitted information"
            },
            # Eradication
            {
                "phase": "Eradication",
                "action": "Scan affected systems for malware or "
                          "persistence mechanisms"
            },
            {
                "phase": "Eradication",
                "action": "Revoke and reissue any compromised tokens "
                          "or session cookies"
            },
            # Recovery
            {
                "phase": "Recovery",
                "action": "Restore affected accounts and verify "
                          "normal access"
            },
            {
                "phase": "Recovery",
                "action": "Enable MFA on affected accounts if "
                          "not already active"
            },
            # Post-Incident
            {
                "phase": "Post-Incident Activity",
                "action": "Document timeline and findings in an "
                          "incident report"
            },
            {
                "phase": "Post-Incident Activity",
                "action": "Conduct phishing awareness training "
                          "for affected users"
            }
        ]
    },

    "ransomware": {
        "name": "Ransomware Attack",
        "severity": "CRITICAL",
        "description": "Malicious software that encrypts files and "
                       "demands payment for decryption keys.",
        "steps": [
            # Detection & Analysis
            {
                "phase": "Detection & Analysis",
                "action": "Identify the affected systems and scope "
                          "of encryption"
            },
            {
                "phase": "Detection & Analysis",
                "action": "Identify the ransomware variant using "
                          "file extensions or ransom note"
            },
            {
                "phase": "Detection & Analysis",
                "action": "Check for available decryptors at "
                          "nomoreransom.org"
            },
            # Containment
            {
                "phase": "Containment",
                "action": "Immediately isolate affected systems "
                          "from the network"
            },
            {
                "phase": "Containment",
                "action": "Disable shared drives and network shares "
                          "to prevent spread"
            },
            {
                "phase": "Containment",
                "action": "Preserve memory dumps and disk images "
                          "for forensic analysis"
            },
            # Eradication
            {
                "phase": "Eradication",
                "action": "Identify and remove the ransomware "
                          "infection vector"
            },
            {
                "phase": "Eradication",
                "action": "Scan all systems for additional malware "
                          "or backdoors"
            },
            # Recovery
            {
                "phase": "Recovery",
                "action": "Restore systems from verified clean backups"
            },
            {
                "phase": "Recovery",
                "action": "Verify integrity of restored data before "
                          "reconnecting to network"
            },
            {
                "phase": "Recovery",
                "action": "Reset all credentials across affected systems"
            },
            # Post-Incident
            {
                "phase": "Post-Incident Activity",
                "action": "Document full attack timeline and "
                          "impact assessment"
            },
            {
                "phase": "Post-Incident Activity",
                "action": "Report incident to relevant authorities "
                          "if required (e.g. CERT NZ)"
            }
        ]
    },

    "brute_force": {
        "name": "Brute Force Attack",
        "severity": "MEDIUM",
        "description": "Repeated login attempts to gain unauthorised "
                       "access to an account or system.",
        "steps": [
            # Detection & Analysis
            {
                "phase": "Detection & Analysis",
                "action": "Identify the targeted account or system "
                          "from SIEM alerts"
            },
            {
                "phase": "Detection & Analysis",
                "action": "Review authentication logs to determine "
                          "attack origin and scope"
            },
            {
                "phase": "Detection & Analysis",
                "action": "Check if any login attempts were successful"
            },
            # Containment
            {
                "phase": "Containment",
                "action": "Block the source IP address at the firewall"
            },
            {
                "phase": "Containment",
                "action": "Lock the targeted account temporarily"
            },
            {
                "phase": "Containment",
                "action": "Implement account lockout policy if "
                          "not already in place"
            },
            # Eradication
            {
                "phase": "Eradication",
                "action": "Verify no unauthorised access was achieved"
            },
            {
                "phase": "Eradication",
                "action": "Review and tighten password policies"
            },
            # Recovery
            {
                "phase": "Recovery",
                "action": "Unlock the account and reset credentials"
            },
            {
                "phase": "Recovery",
                "action": "Enable MFA on the targeted account"
            },
            # Post-Incident
            {
                "phase": "Post-Incident Activity",
                "action": "Document the incident and update "
                          "detection rules in SIEM"
            }
        ]
    },

    "data_exfiltration": {
        "name": "Data Exfiltration",
        "severity": "CRITICAL",
        "description": "Unauthorised transfer of data from an "
                       "organisation to an external destination.",
        "steps": [
            # Detection & Analysis
            {
                "phase": "Detection & Analysis",
                "action": "Identify the source system and user "
                          "involved in the transfer"
            },
            {
                "phase": "Detection & Analysis",
                "action": "Determine what data was transferred "
                          "and its sensitivity level"
            },
            {
                "phase": "Detection & Analysis",
                "action": "Identify the external destination "
                          "IP or domain"
            },
            # Containment
            {
                "phase": "Containment",
                "action": "Block outbound traffic to the "
                          "identified destination"
            },
            {
                "phase": "Containment",
                "action": "Isolate the source system from the network"
            },
            {
                "phase": "Containment",
                "action": "Suspend the involved user account "
                          "pending investigation"
            },
            # Eradication
            {
                "phase": "Eradication",
                "action": "Determine the exfiltration method "
                          "and close the vector"
            },
            {
                "phase": "Eradication",
                "action": "Review DLP policies and tighten "
                          "data transfer controls"
            },
            # Recovery
            {
                "phase": "Recovery",
                "action": "Restore normal operations after "
                          "confirming threat is contained"
            },
            {
                "phase": "Recovery",
                "action": "Notify affected parties if personal "
                          "data was involved (Privacy Act 2020)"
            },
            # Post-Incident
            {
                "phase": "Post-Incident Activity",
                "action": "Report to CERT NZ if required"
            },
            {
                "phase": "Post-Incident Activity",
                "action": "Conduct full forensic review and "
                          "document findings"
            }
        ]
    }
}
