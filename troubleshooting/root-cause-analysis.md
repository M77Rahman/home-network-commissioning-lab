# Root Cause Analysis

## Problem statement
Diagnostic checks on the guest Wi-Fi network gave partial/blocked ICMP and traceroute responses, which could be misread as a network fault.

## Tests performed
1. Ping default gateway `10.104.64.1`.
2. Ping public IP `8.8.8.8`.
3. Ping public domain `google.com`.
4. Run `nslookup google.com`.
5. Run `traceroute google.com`.

## Evidence summary
- Gateway ping: **100% packet loss** with **"Communication prohibited by filter"**.
- Public IP ping (`8.8.8.8`): **0% packet loss**.
- Domain ping (`google.com`): **0% packet loss**.
- DNS lookup: successful via resolver `185.228.168.85`.
- Traceroute: first hop visible; later hops displayed `* * *`.

## Analysis and diagnosis
- End-to-end user connectivity was present (public IP and domain ping successful).
- DNS was functioning correctly (name resolution successful).
- The gateway ICMP response and traceroute visibility were filtered/limited by policy.
- This pattern is consistent with guest-network security controls that restrict diagnostic traffic.

## Root cause
Guest Wi-Fi filtering policy blocked or limited diagnostic ICMP/traceroute traffic, leading to failed/partial diagnostic results even though internet service remained available.

## Lessons learned
- Do not treat gateway ping failure alone as proof of an outage.
- Validate service using multiple test types (IP reachability, DNS, and application-level checks where possible).
- Document policy-driven filtering clearly to avoid false incident escalation.
