# Home Network Commissioning and Troubleshooting Lab

## Overview
This repository is a practical lab project I built to support my application for a **Virgin Media O2 Network Engineer Apprenticeship**.

It demonstrates a clear, repeatable workflow for:
- documenting network addressing and topology,
- capturing baseline connectivity and DNS evidence,
- analysing a real troubleshooting scenario,
- communicating outcomes in both technical and customer-friendly formats.

## Why I built this project
I built this project to practice core network engineering habits in a structured way and create evidence of my process. The focus was to improve at:
- accurate network documentation,
- disciplined end-to-end testing,
- DNS and connectivity troubleshooting,
- professional handover communication.

## Role alignment (Virgin Media O2 Network Engineer Apprentice)
This project aligns with apprentice-level expectations by demonstrating:
- foundational networking (IP addressing, gateway, DNS checks),
- practical test execution and evidence capture,
- structured troubleshooting from symptom to root cause,
- clear customer and handover communication,
- secure handling of sensitive network details.

## Repository contents
- `network-map/` — Device inventory, topology notes, and commissioning notes.
- `testing/` — Captured baseline test evidence (ping, DNS, traceroute, environment summary).
- `troubleshooting/` — Documented guest Wi-Fi diagnostic-filtering scenario with RCA and resolution report.
- `customer-docs/` — Customer summary and handover guidance.
- `scripts/` — Python helper script for running core network checks.

## Captured baseline evidence
The project includes captured baseline evidence showing:
- gateway ping failure with filter message,
- successful public IP and domain reachability,
- successful DNS resolution,
- traceroute first-hop response with later-hop non-response,
- final interpretation that internet/DNS were operational while diagnostic traffic was filtered.

## Troubleshooting scenario
A full troubleshooting case is documented for **diagnostic traffic filtering on a guest Wi-Fi network**, including:
- fault description and symptoms,
- evidence summary,
- diagnosis and root cause,
- recommendations and customer communication notes.

## Tools used
- Markdown documentation for structured records.
- Standard network commands (`ping`, `nslookup`, `traceroute`/`tracert`, interface/route checks).
- Python 3 helper script (`scripts/network_test.py`) using only built-in libraries.

## Security and privacy notes
- Private/internal addressing is masked in summary/customer-facing sections.
- Only necessary technical detail is included in evidence sections.
- No credentials or customer-identifying details are stored.

## What I learned
- How to build a consistent baseline test sequence.
- How to distinguish diagnostic filtering from real service outage.
- How to document results clearly for both technical and non-technical audiences.

## Future improvements
- Add additional sanitized evidence samples for repeat runs.
- Add lightweight validation checks for documentation consistency.
- Extend testing to include Wi-Fi quality metrics and packet capture references.
This repository is a practical lab project I built to support my application for a **Virgin Media O2 Network Engineer Apprenticeship**. It is designed to show how I approach home network commissioning, baseline verification, fault investigation, and clear documentation.

The project focuses on repeatable steps:
- map the network and record addressing details,
- run end-to-end connectivity and DNS checks,
- investigate a fault methodically,
- document actions and outcomes clearly,
- communicate findings in both technical and customer-friendly formats.

## Why I built this project
I built this project to practice core network engineering habits in a structured way and create evidence of my process. I wanted to improve at:
- accurate network addressing documentation,
- collecting real test evidence instead of assumptions,
- troubleshooting DNS and connectivity issues step-by-step,
- writing notes that are useful for handover and customer communication.

## Role alignment (Virgin Media O2 Network Engineer Apprentice)
This lab aligns with apprentice-level expectations by demonstrating:
- **Foundational network knowledge** (IP addressing, gateway and DNS checks).
- **Practical testing discipline** (baseline tests, ping, traceroute, DNS lookups).
- **Troubleshooting mindset** (fault scenario, root-cause analysis, resolution report).
- **Professional communication** (technical records plus customer-facing summaries).
- **Secure network awareness** (safe handling of sensitive network details).

I have kept the scope realistic for apprenticeship level and focused on learning-oriented, hands-on practice.

## Tools used
- Markdown files for structured technical records and reports.
- Standard command-line network tools:
  - `ip` / `ipconfig`
  - `ping`
  - `traceroute` / `tracert`
  - `nslookup`
- Python helper script (`scripts/network_test.py`) to run baseline commands and gather real output for documentation.

## Network tests performed
The testing workflow is documented in the `testing/` folder and includes:
1. Local addressing checks (interface details, routes, gateway).
2. Ping tests to:
   - default gateway,
   - public IP endpoint,
   - public domain.
3. Traceroute tests for path visibility and latency observation.
4. DNS tests for resolver behavior and domain resolution consistency.

All templates use placeholders so only real command output is recorded.

## Fault scenario
The `troubleshooting/` folder contains a structured incident workflow:
- `fault-scenario.md` — what was reported, impact, and scope.
- `root-cause-analysis.md` — evidence, analysis, and confirmed cause.
- `resolution-report.md` — actions taken, validation, and outcome.

This keeps troubleshooting traceable from first symptom to service restoration.

## Skills demonstrated
- Network addressing and inventory documentation.
- End-to-end connectivity testing and interpretation.
- DNS troubleshooting using repeatable checks.
- Methodical fault isolation and root-cause reporting.
- Clear record-keeping for handover and audit trail.
- Customer communication through concise, non-technical summaries.

## Security notes
This project is built with secure network awareness in mind:
- Use placeholders where sensitive values may appear.
- Avoid sharing private IP plans, MAC addresses, serials, or credentials publicly.
- Redact customer-identifiable information before publishing evidence.
- Keep troubleshooting outputs factual and limited to what is needed.

## What I learned
From building this lab, I improved my ability to:
- document network addressing more accurately,
- run tests in a consistent end-to-end sequence,
- separate DNS issues from general connectivity issues,
- explain technical actions clearly for both engineers and customers,
- keep troubleshooting records professional and reproducible.

## Future improvements
- Add sample sanitized test runs to demonstrate completed workflows.
- Add a simple checklist for commissioning sign-off.
- Expand DNS troubleshooting with `dig` and comparison across resolvers.
- Add basic Wi-Fi quality checks and interference notes.
- Introduce versioned incident templates for multiple fault scenarios.
