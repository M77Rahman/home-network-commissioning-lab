# Fault Scenario

## Scenario title
Diagnostic traffic filtering on guest Wi-Fi network

## Reported issue
A connectivity check appeared to fail because pings to the local default gateway were blocked on the guest Wi-Fi segment.

## Customer/user impact
- Internet browsing and normal DNS resolution were still working.
- Network diagnostics looked inconsistent, which created uncertainty during testing.
- No full service outage was observed.

## Symptoms observed
- Ping to default gateway `10.104.64.1` returned 100% packet loss.
- Ping output included: **"Communication prohibited by filter"**.
- Ping to public IP `8.8.8.8` succeeded with 0% packet loss.
- Ping to `google.com` succeeded with 0% packet loss.
- `nslookup google.com` succeeded using DNS server `185.228.168.85`.
- `traceroute google.com` reached the first hop, then later hops showed `* * *`.

## Scope
- Affected network: Guest Wi-Fi (segmented/filtered network)
- Affected protocols: Diagnostic ICMP/traceroute visibility
- Not affected: General internet connectivity and DNS lookups

## Initial assessment
The behaviour suggested a policy/filtering condition on the guest network rather than a total connectivity failure.
