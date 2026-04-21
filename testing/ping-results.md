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
