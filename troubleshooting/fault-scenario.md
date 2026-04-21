# Fault Scenario

## Scenario title
Diagnostic traffic filtering on a guest Wi-Fi network

## Reported issue
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
- The issue affected diagnostic visibility, not end-user connectivity.

## Scope
- Network segment: Guest Wi-Fi
- Primary affected diagnostics: ICMP echo to gateway and multi-hop traceroute visibility
- Unaffected services: External IP reachability and DNS name resolution
