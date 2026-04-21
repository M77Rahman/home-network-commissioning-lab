# Ping Results

## Test 1: Default gateway
- Command: `ping -c 4 10.104.64.1`
- Result summary:
  - 4 packets transmitted
  - 0 packets received
  - 100% packet loss
  - Message observed: `Communication prohibited by filter`

```text
PING 10.104.64.1 (10.104.64.1): 56 data bytes
ping: sendto: Communication prohibited by filter
ping: sendto: Communication prohibited by filter
ping: sendto: Communication prohibited by filter
ping: sendto: Communication prohibited by filter

--- 10.104.64.1 ping statistics ---
4 packets transmitted, 0 packets received, 100.0% packet loss
```

## Test 2: Public IP
- Command: `ping -c 4 8.8.8.8`
- Result summary:
  - 4 packets transmitted
  - 4 packets received
  - 0% packet loss
  - Average latency: 11.675 ms

```text
--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 10.958/11.675/12.540/0.563 ms
```

## Test 3: Public domain
- Command: `ping -c 4 google.com`
- Result summary:
  - 4 packets transmitted
  - 4 packets received
  - 0% packet loss
  - Average latency: 11.190 ms

```text
--- google.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 10.614/11.190/11.927/0.511 ms
```

## Ping interpretation
- Public IP and domain reachability were successful.
- Gateway ICMP response was blocked on this guest network segment.
- These results support connectivity with filtered diagnostics, not a full outage.
## Test Environment

- Device used: MacBook Air
- Connection type: Wi-Fi
- Active interface: `en0`
- Private IP address: `10.104.70.xxx`
- Network type: Guest Wi-Fi network

## Test 1: Default Gateway Ping

Command used:

```bash
ping -c 4 10.104.64.1

Result summary:

Packets transmitted: 4
Packets received: 0
Packet loss: 100%
Message observed: Communication prohibited by filter

Conclusion:

The test device attempted to reach the default gateway using ICMP ping, but the response showed that ICMP traffic was blocked by network filtering.

This means gateway reachability could not be confirmed using ping on this guest Wi-Fi network. It does not automatically prove the gateway was offline. It suggests the network may block ICMP traffic as part of its security or guest network policy.

Test 2: External IP Address Ping

Command used:

ping -c 4 8.8.8.8

Result summary:

Packets transmitted: 4
Packets received: 4
Packet loss: 0%
Average latency: 11.675 ms

Conclusion:

The test device successfully reached an external IP address. This confirmed that internet connectivity was working independently of DNS name resolution.

Test 3: External Domain Ping

Command used:

ping -c 4 google.com

Result summary:

Packets transmitted: 4
Packets received: 4
Packet loss: 0%
Average latency: 11.190 ms

Conclusion:

The test device successfully reached an external domain. This confirmed that general internet connectivity and DNS-backed domain access were working at the time of testing.

Overall Ping Test Conclusion

The ping tests showed that external connectivity was working, because both 8.8.8.8 and google.com responded successfully.

The failed default gateway ping did not prove a full network fault. The Communication prohibited by filter message suggests ICMP traffic to the gateway was blocked by network filtering.


Then save it.

## Why replace this one?

Because the current file includes:

- duplicate sections
- broken markdown code blocks
- instructions meant for other files
- DNS and traceroute notes in the wrong file
- “Next step” text that should not be in GitHub

So for this file: **yes, replace the whole thing**.

After saving, run:

```bash
cat testing/ping-results.md
