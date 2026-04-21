# Root Cause Analysis

## Problem statement
Gateway ICMP and traceroute outputs on the guest Wi-Fi network suggested possible packet loss, while internet and DNS tests were successful.

## Tests performed
1. `ping 10.104.64.1`
2. `ping 8.8.8.8`
3. `ping google.com`
4. `nslookup google.com`
5. `traceroute google.com`

## Evidence summary
- `ping 10.104.64.1`: **100% packet loss**.
- Ping diagnostic message: **"Communication prohibited by filter"**.
- `ping 8.8.8.8`: **0% packet loss**.
- `ping google.com`: **0% packet loss**.
- `nslookup google.com`: successful via `185.228.168.85`.
- `traceroute google.com`: first hop responded; subsequent hops showed `* * *`.

## Diagnosis
The pattern is consistent with policy-based filtering on the guest Wi-Fi network:
- ICMP diagnostic traffic may be blocked or rate-limited for specific paths.
- Traceroute visibility may be reduced because intermediate devices can drop or deprioritise probe responses.
- End-to-end internet connectivity can still work even when diagnostic replies are filtered.

## Root cause
Guest Wi-Fi security controls filtered diagnostic ICMP/traceroute traffic, resulting in misleading diagnostic outputs despite working internet and DNS services.

## Lessons learned
- Use multiple tests before concluding a network fault.
- A failed gateway ping alone is not enough to declare service failure.
- Record filtering behaviour clearly to prevent unnecessary escalation.
## Problem Statement
[Placeholder: concise technical problem statement]

## Evidence Collected
- Test Results Referenced: [Placeholder]
- Logs/Outputs: [Placeholder]
- Device/Config Checks: [Placeholder]

## Analysis
### What Worked
- [Placeholder]

### What Failed
- [Placeholder]

### Why It Failed
[Placeholder: explain the technical reason in simple terms]

## Root Cause
[Placeholder: single clear root cause statement]

## Preventive Actions
- [Placeholder action 1]
- [Placeholder action 2]
