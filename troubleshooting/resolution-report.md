# Resolution Report

## Resolution summary
No break/fix repair was required. Test results were reviewed and interpreted as expected behaviour for a filtered guest Wi-Fi network.

## Actions taken
1. Compared gateway, public IP, and public domain ping results.
2. Verified DNS resolution with `nslookup google.com`.
3. Reviewed traceroute pattern (first hop response, later-hop `* * *`).
4. Correlated findings with guest-network diagnostic traffic filtering.
5. Documented outcome and guidance for future troubleshooting.

## Retest results
- Ping to `10.104.64.1`: still filtered (100% loss, "Communication prohibited by filter").
- Ping to `8.8.8.8`: successful (0% packet loss).
- Ping to `google.com`: successful (0% packet loss).
- `nslookup google.com`: successful using DNS server `185.228.168.85`.
- `traceroute google.com`: first hop visible, later hops masked as `* * *`.

## Recommendation
- Keep current guest-network filtering if it matches security policy.
- Update operational runbooks to note that ICMP/traceroute filtering can affect diagnostics even when user connectivity works.
- When troubleshooting guest SSIDs, use multiple checks and avoid conclusions based on one tool.

## Customer communication note
The guest network internet service is operational. Some diagnostic tools are intentionally restricted by network policy, which is why certain ping/traceroute results appear blocked.
