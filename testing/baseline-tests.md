# Baseline Tests

## Purpose
Record baseline network checks before any troubleshooting changes are made.

## Test environment
- Date/time: Captured during baseline troubleshooting session
- Tester: Apprentice lab user
- Test device: MacBook Air
- Connection type: Wi-Fi
- Active interface: en0
- Private IP: 10.104.70.xxx
- Default gateway: 10.104.64.x
- DNS servers: 185.228.168.85, 185.228.169.85
- Network type: Guest Wi-Fi network

## Baseline test plan
1. Verify local IP configuration.
2. Ping the default gateway.
3. Ping a public IP endpoint (`8.8.8.8`).
4. Resolve and ping a public domain (`google.com`).
5. Run traceroute to `google.com`.
6. Verify DNS lookup consistency with `nslookup`.

## Commands used
```bash
ip a
ip route
ping -c 4 10.104.64.1
ping -c 4 8.8.8.8
ping -c 4 google.com
traceroute google.com
nslookup google.com
```

## Baseline status
- [x] Completed successfully
- [x] Issues detected (gateway ping and traceroute visibility filtered)

## Summary conclusion
- Internet connectivity was working.
- DNS resolution was working.
- Gateway ping and traceroute behavior were likely affected by guest-network filtering.
- This baseline does not indicate a full network outage.
