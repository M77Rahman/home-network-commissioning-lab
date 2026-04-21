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
