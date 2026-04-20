# Traceroute Results

## Test Environment

- Device used: MacBook Air
- Connection type: Wi-Fi
- Active interface: `en0`
- Network type: Guest Wi-Fi network

## Traceroute Test: google.com

Command used:

```bash
traceroute google.com

Result summary:

Target domain: google.com
Target IP used by traceroute: 142.250.151.139
First responding hop: 10.104.64.2
Later hops: No response shown as * * *
Test stopped manually after repeated non-responses

Observed output summary:

traceroute: Warning: google.com has multiple addresses; using 142.250.151.139
traceroute to google.com (142.250.151.139), 64 hops max, 40 byte packets
1  10.104.64.2  11.794 ms  5.689 ms  5.727 ms
2  * * *
3  * * *
...

Conclusion:

The traceroute reached the first network hop, but later hops did not respond. This suggests that traceroute responses may be filtered by the guest Wi-Fi network or by upstream routers.

This does not mean the internet connection failed, because ping and DNS tests to google.com were successful.