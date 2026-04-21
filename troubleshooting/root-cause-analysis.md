# Root Cause Analysis

## Problem statement
Gateway and traceroute diagnostics appeared degraded on guest Wi-Fi, while internet and DNS checks succeeded.

## Tests performed
1. `ping -c 4 10.104.64.1`
2. `ping -c 4 8.8.8.8`
3. `ping -c 4 google.com`
4. `nslookup google.com`
5. `traceroute google.com`

## Evidence summary
- Gateway ping returned 100% packet loss with `Communication prohibited by filter`.
- Public IP ping returned 0% packet loss.
- Public domain ping returned 0% packet loss.
- DNS lookup succeeded using `185.228.168.85`.
- Traceroute showed first-hop response followed by repeated `* * *`.

## Diagnosis
The observed pattern is consistent with policy-based filtering on the guest Wi-Fi segment:
- ICMP diagnostic traffic to gateway can be blocked.
- Traceroute probes can be filtered or unanswered after early hops.
- End-user connectivity can still work while these diagnostics are partially restricted.

## Root cause
Guest-network filtering controls limited diagnostic ICMP/traceroute visibility without interrupting internet or DNS service.

## Lessons learned
- Use multiple checks before concluding service impact.
- A gateway ping failure alone is not enough to declare outage.
- Record filtering behavior clearly in troubleshooting notes.
