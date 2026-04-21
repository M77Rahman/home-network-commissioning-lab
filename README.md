# Home Network Commissioning and Troubleshooting Lab

## Overview

This repository is a practical networking lab project built to support my application for a Network Engineer Apprenticeship.

The project demonstrates a structured approach to documenting a small network, capturing baseline connectivity evidence, investigating a troubleshooting scenario, and communicating the outcome clearly for both technical and non-technical audiences.

It focuses on apprentice-level network engineering skills, including:

- Network topology documentation
- IP addressing and gateway checks
- DNS and connectivity testing
- Traceroute interpretation
- Structured troubleshooting
- Root cause analysis
- Customer-friendly handover notes
- Secure handling of sensitive network details

## Why I Built This Project

I built this project to make my networking knowledge more practical and job-relevant.

The Virgin Media O2 Network Engineer Apprenticeship involves installing, testing, troubleshooting, and explaining network services to customers. This project helped me practise a similar style of thinking on a smaller home-network scale.

The aim was not to claim professional telecoms experience, but to show that I can:

- Follow a clear testing process
- Capture and organise technical evidence
- Investigate faults logically
- Document findings accurately
- Explain technical outcomes in plain language

## Role Alignment

This project is relevant to network engineering because it shows a basic commissioning and troubleshooting workflow.

It demonstrates:

- Foundational understanding of IP addressing, gateway, and DNS checks
- Practical use of common network commands
- End-to-end connectivity testing
- Evidence capture and interpretation
- Structured fault investigation
- Customer-facing communication
- Awareness of security and privacy when documenting network information

    
Network Topology
Component	Role	Notes
Home router	Default gateway and internet access	Private details masked
Laptop	Main test device	Used for connectivity and DNS tests
Wi-Fi network	Local wireless access	Tested for stability and connectivity
DNS resolver	Name resolution	Tested using command-line tools

Sensitive details such as private IP ranges, Wi-Fi names, device identifiers, and public IP information have been masked or removed where appropriate.

Testing Completed

The lab includes baseline checks for:

Local IP configuration
Default gateway reachability
Public IP reachability
DNS resolution
Traceroute path visibility
Basic interpretation of filtered or blocked diagnostic traffic
Test Summary
Test	Expected Result	Actual Result	Outcome
Check local IP configuration	Device receives valid IP settings	IP, gateway, and DNS details confirmed	Pass
Ping default gateway	Gateway responds or blocks ICMP consistently	Result recorded and interpreted	Pass
Ping public IP	Internet path is reachable	Public IP test completed successfully	Pass
DNS lookup	Domain resolves successfully	DNS response confirmed	Pass
Traceroute	Network path is at least partially visible	First-hop response recorded, later hops filtered or non-responsive	Pass
Troubleshooting Scenario

A troubleshooting scenario is documented for a device connected to Wi-Fi but experiencing website access issues.

The investigation followed a step-by-step process:

Confirmed Wi-Fi connection status
Checked local IP address, gateway, and DNS settings
Tested connectivity to the default gateway
Tested internet reachability using a public IP
Tested DNS resolution using a domain lookup
Compared results to identify whether the issue was local connectivity, internet access, or DNS-related
Recorded findings and recommended next steps

The scenario helped demonstrate the importance of separating:

Device connection issues
Local network issues
Internet reachability issues
DNS/name resolution issues
Diagnostic traffic filtering
Tools Used
Markdown for structured documentation
Git and GitHub for version control
Command-line networking tools:
ping
nslookup
tracert / traceroute
IP configuration checks
Python 3 helper script for basic connectivity checks
Customer Handover

The project includes a customer-friendly handover note explaining:

What checks were completed
What the results showed
Basic guidance for the user
When the issue should be escalated

This was included because network engineering is not only about technical testing. It also requires clear communication with customers and stakeholders.

Security and Privacy Notes

To keep the project safe and professional:

Private network details have been masked where appropriate
No Wi-Fi passwords or credentials are included
No customer-identifying information is stored
Public IP information has been removed or sanitised
The project focuses on process, evidence, and interpretation rather than exposing sensitive details
What I Learned

This project helped me improve my understanding of:

How to document a small network clearly
How to run a basic connectivity test sequence
How to interpret DNS and traceroute results
How to avoid guessing during troubleshooting
How to write technical notes in a clear and structured way
How to explain network outcomes to a non-technical user
What This Demonstrates

This project demonstrates that I can:

Follow a structured commissioning-style checklist
Document network topology and basic IP addressing
Run and interpret connectivity and DNS tests
Troubleshoot faults logically
Record findings clearly for technical review
Explain outcomes in a customer-friendly way
Handle network information responsibly
Future Improvements

Future improvements could include:

Adding more sanitised evidence samples from repeat test runs
Creating a lightweight commissioning sign-off checklist
Extending testing to include Wi-Fi quality metrics
Adding packet capture references for learning purposes
Expanding the troubleshooting section with more fault scenarios

```text
## Repository Structure

home-network-commissioning-lab/
│
├── README.md
├── network-map/
│   └── topology.md
├── testing/
│   └── connectivity-tests.md
├── troubleshooting/
│   └── troubleshooting-scenario.md
├── customer-docs/
│   └── customer-handover-note.md
└── scripts/
    └── basic_connectivity_check.py
