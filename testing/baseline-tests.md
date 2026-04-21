# Baseline Tests

## Purpose
Record baseline network checks before troubleshooting conclusions are made.

## Test environment
- Device: MacBook Air
- Connection type: Wi-Fi
- Active interface: en0
- Private IP: 10.104.70.xxx
- Default gateway (masked): 10.104.64.x
- DNS servers: 185.228.168.85, 185.228.169.85
- Network type: Guest Wi-Fi network

## Baseline test sequence
1. Verify local interface and routing context.
2. Ping default gateway.
3. Ping public IP (`8.8.8.8`).
4. Ping public domain (`google.com`).
5. Run `nslookup google.com`.
6. Run `traceroute google.com`.

## Commands run
```bash
ping -c 4 10.104.64.1
ping -c 4 8.8.8.8
ping -c 4 google.com
nslookup google.com
traceroute google.com
```

## Baseline conclusion
- Internet connectivity was working.
- DNS resolution was working.
- Gateway ping and traceroute visibility were likely affected by guest-network filtering.
- Results did not indicate a full network outage.
