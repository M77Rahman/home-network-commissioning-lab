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

## Service impact assessment
- Internet access remained available.
- DNS resolution remained available.
- Diagnostic visibility for gateway ping/traceroute was restricted.

## Scope
- Network segment: Guest Wi-Fi network
- Affected diagnostics: ICMP to gateway and traceroute path visibility
- Unaffected service: End-user internet and DNS access
