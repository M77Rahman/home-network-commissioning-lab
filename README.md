# Home Network Commissioning and Troubleshooting Lab

## 1. Project Overview
This repository is an apprenticeship portfolio project showing how I document, test, and troubleshoot a home/guest Wi-Fi network in a structured way.

Key project folders:
- [`network-map/`](network-map/) — topology and device context
- [`testing/`](testing/) — captured baseline test evidence
- [`troubleshooting/`](troubleshooting/) — issue analysis and resolution notes
- [`customer-docs/`](customer-docs/) — customer-facing and handover documents
- [`scripts/`](scripts/) — simple command-runner script for baseline checks

## 2. Why I Built It
I built this project to practice apprentice-level network engineering habits:
- follow a repeatable commissioning-style process,
- verify connectivity with evidence,
- avoid assumptions during troubleshooting,
- communicate clearly to technical and non-technical readers.

## 3. Tools Used
- Command-line checks: `ping`, `nslookup`, `traceroute`/`tracert`
- Interface/route checks by platform (Windows, macOS, Linux)
- Python helper script: `scripts/basic_connectivity_check.py` (built-in libraries only)
- Markdown documentation

## 4. Network Topology
| Component | Role | Notes |
|---|---|---|
| Network gateway/router | Default gateway and internet access | Private details masked |
| MacBook Air | Main test device | Used for connectivity, DNS and traceroute tests |
| Wi-Fi network | Local wireless access | Tested for baseline connectivity |
| DNS resolver | Name resolution | Tested using nslookup |

## 5. Testing Completed
Evidence captured in:
- [`testing/baseline-tests.md`](testing/baseline-tests.md)
- [`testing/ping-results.md`](testing/ping-results.md)
- [`testing/dns-tests.md`](testing/dns-tests.md)
- [`testing/traceroute-results.md`](testing/traceroute-results.md)

## 6. Test Summary
| Test | Expected Result | Actual Result | Outcome |
|---|---|---|---|
| Check local IP configuration | Device receives valid IP settings | IP, gateway, and DNS details confirmed | Pass |
| Ping default gateway | Gateway responds or filtering is identified | ICMP traffic appeared filtered | Pass |
| Ping public IP | Internet path reachable | Public IP test completed successfully | Pass |
| DNS lookup | Domain resolves successfully | DNS response confirmed | Pass |
| Traceroute | Network path partially visible | First hop visible, later hops filtered | Pass |

## 7. Troubleshooting Scenario
### Issue
Gateway ping and traceroute results suggested that some diagnostic traffic was not responding as expected.

### Checks Performed
1. Checked local IP address, default route and DNS settings.
2. Tested the default gateway using ping.
3. Tested internet access using a public IP address.
4. Tested domain connectivity using google.com.
5. Tested DNS resolution using nslookup.
6. Ran traceroute to observe the network path.

### Finding
The internet connection and DNS resolution were working, but ICMP/traceroute responses appeared to be filtered on the guest Wi-Fi network.

### Resolution / Recommendation
No outage was identified. The result was documented as diagnostic traffic filtering. A user should not assume the network is down based only on failed ping/traceroute results.

### What I Learned
A structured process prevents guessing and helps separate real connectivity faults from blocked diagnostic traffic.

## 8. Customer Handover
- [`customer-docs/customer-summary.md`](customer-docs/customer-summary.md)
- [`customer-docs/customer-handover-note.md`](customer-docs/customer-handover-note.md)
- [`customer-docs/handover-guide.md`](customer-docs/handover-guide.md)

## 9. What This Demonstrates
This project demonstrates that I can:
- Follow a structured commissioning-style checklist
- Document network topology and IP addressing basics
- Run and interpret connectivity and DNS tests
- Troubleshoot faults logically instead of guessing
- Record findings clearly for technical review
- Explain outcomes in a customer-friendly way

## 10. What I Learned
- Baseline evidence is essential before making conclusions.
- Failed gateway ping does not always mean service outage.
- DNS and internet checks should be validated separately.
- Clear written records improve troubleshooting quality.

## 11. Future Improvements
- Add additional sanitized baseline runs for comparison.
- Add a short validation checklist to confirm document consistency.
- Extend checks with Wi-Fi quality metrics.
