# Resolution Report

## Resolution summary
No break/fix repair was required. The observed behaviour matches filtered diagnostic traffic on a guest Wi-Fi network.

## Actions taken
1. Validated local-gateway, public-IP, and public-domain ping outcomes.
2. Confirmed DNS resolution with `nslookup google.com`.
3. Reviewed traceroute response pattern.
4. Correlated all results with guest-network filtering policy behaviour.
5. Documented guidance for future diagnostics on filtered SSIDs.

## Retest results
- `ping 10.104.64.1`: **100% packet loss**, with **"Communication prohibited by filter"**.
- `ping 8.8.8.8`: **0% packet loss**.
- `ping google.com`: **0% packet loss**.
- `nslookup google.com`: successful using DNS server `185.228.168.85`.
- `traceroute google.com`: first hop visible, later hops displayed `* * *`.

## Recommendation
- Keep filtering policy in place if it is required by guest-network security design.
- Add a troubleshooting note in runbooks: ICMP/traceroute filtering can affect diagnostic tests even when internet connectivity is working.
- When validating guest Wi-Fi, combine diagnostic results with practical service checks.

## Customer communication note
Internet and DNS services are operational on the guest Wi-Fi network. Some diagnostic tools show blocked or partial results because filtering controls are applied by design.
