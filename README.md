# Home Network Commissioning and Troubleshooting Lab

## Overview

This repository is a practical lab project I built to support my application for a Virgin Media O2 Network Engineer Apprenticeship.

It demonstrates a clear, repeatable workflow for:

- documenting network addressing and topology
- capturing baseline connectivity and DNS evidence
- analysing a troubleshooting scenario
- communicating outcomes in both technical and customer-friendly formats

## Why I Built This Project

I built this project to practise core network engineering habits in a structured way and create evidence of my process. The focus was to improve at:

- accurate network documentation
- disciplined end-to-end testing
- DNS and connectivity troubleshooting
- professional handover communication

## Role Alignment

This project aligns with apprentice-level expectations by demonstrating:

- foundational networking, including IP addressing, gateway, and DNS checks
- practical test execution and evidence capture
- structured troubleshooting from symptom to root cause
- clear customer and handover communication
- secure handling of sensitive network details

## Repository Contents

- [`network-map/`](network-map/) — Device inventory, topology notes, and commissioning notes
- [`testing/`](testing/) — Captured baseline test evidence including ping, DNS, traceroute, and environment summary
- [`troubleshooting/`](troubleshooting/) — Documented guest Wi-Fi diagnostic-filtering scenario with RCA and resolution report
- [`customer-docs/`](customer-docs/) — Customer summary and handover guidance
- [`scripts/`](scripts/) — Python helper script for running core network checks

## Captured Baseline Evidence

The project includes captured baseline evidence showing:

- gateway ping failure with filter message
- successful public IP and domain reachability
- successful DNS resolution
- traceroute first-hop response with later-hop non-response
- final interpretation that internet and DNS were operational while diagnostic traffic was filtered

## Troubleshooting Scenario

A full troubleshooting case is documented for diagnostic traffic filtering on a guest Wi-Fi network, including:

- fault description and symptoms
- evidence summary
- diagnosis and root cause
- recommendations and customer communication notes

## Tools Used

- Markdown documentation for structured records
- Standard network commands: `ping`, `nslookup`, `traceroute` / `tracert`, interface and route checks
- Python 3 helper script using built-in libraries

## Security and Privacy Notes

- Private/internal addressing is masked in summary and customer-facing sections
- Only necessary technical detail is included in evidence sections
- No credentials or customer-identifying details are stored

## What I Learned

- How to build a consistent baseline test sequence
- How to distinguish diagnostic filtering from a real service outage
- How to document results clearly for technical and non-technical audiences

## Future Improvements

- Add additional sanitised evidence samples for repeat runs
- Add a lightweight commissioning sign-off checklist
- Extend testing to include Wi-Fi quality metrics and packet capture references
