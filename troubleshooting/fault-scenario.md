# Fault Scenario

## Scenario title
Diagnostic traffic filtering on a guest Wi-Fi network

## Reported issue
Gateway ping on the guest Wi-Fi test segment returned 100% packet loss, which could appear to indicate a connectivity issue.

## Symptoms observed
- `ping -c 4 10.104.64.1`: 100% packet loss
- Diagnostic message: `Communication prohibited by filter`
- `ping -c 4 8.8.8.8`: success, 0% packet loss
- `ping -c 4 google.com`: success, 0% packet loss
- `nslookup google.com`: successful via DNS server `185.228.168.85`
- `traceroute google.com`: first hop responded, later hops showed `* * *`
During baseline diagnostics on the guest Wi-Fi segment, the default-gateway ping test failed, which could be interpreted as a connectivity issue.

## Symptoms observed
- Ping to default gateway `10.104.64.1` returned **100% packet loss**.
- Ping output included: **"Communication prohibited by filter"**.
- Ping to `8.8.8.8` succeeded with **0% packet loss**.
- Ping to `google.com` succeeded with **0% packet loss**.
- `nslookup google.com` succeeded using DNS server `185.228.168.85`.
- `traceroute google.com` reached the first hop, then later hops showed `* * *`.

## Service impact assessment
- Internet access remained available.
- DNS resolution remained available.
- Diagnostic visibility for gateway ping/traceroute was restricted.

## Scope
- Network segment: Guest Wi-Fi network
- Affected diagnostics: ICMP to gateway and traceroute path visibility
- Unaffected service: End-user internet and DNS access
- The issue affected diagnostic visibility, not end-user connectivity.

## Scope
- Network segment: Guest Wi-Fi
- Primary affected diagnostics: ICMP echo to gateway and multi-hop traceroute visibility
- Unaffected services: External IP reachability and DNS name resolution
## Scenario Title
[Placeholder: short title of the fault]

## Business/Customer Impact
[Placeholder: what the user could not do and why it matters]

## Symptoms Reported
- [Placeholder symptom 1]
- [Placeholder symptom 2]
- [Placeholder symptom 3]

## Scope
- Affected Devices: [Placeholder]
- Affected Services: [Placeholder]
- Start Time: [Placeholder]
- Severity: [Low/Medium/High]

## Initial Checks Performed
- [Placeholder check 1]
- [Placeholder check 2]
- [Placeholder check 3]
