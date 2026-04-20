# Baseline Tests

## Purpose
Record baseline network checks before any troubleshooting changes are made.

## Test environment
- Date/time: [Placeholder]
- Tester: [Placeholder]
- Test device: [Placeholder]
- Connection type: [Placeholder]

## Baseline test plan
1. Verify local IP configuration.
2. Ping the default gateway.
3. Ping a public IP endpoint (for example, `8.8.8.8`).
4. Resolve and ping a public domain.
5. Run traceroute/tracert to a public domain.
6. Verify DNS lookup consistency.

## Commands used
```bash
# Linux/macOS examples
ip a
ip route
ping -c 4 <default-gateway>
ping -c 4 8.8.8.8
ping -c 4 bbc.co.uk
traceroute bbc.co.uk
nslookup bbc.co.uk

# Windows examples
ipconfig /all
ping <default-gateway>
ping 8.8.8.8
ping bbc.co.uk
tracert bbc.co.uk
nslookup bbc.co.uk
```

## Baseline status
- [ ] Completed successfully
- [ ] Issues detected (see `troubleshooting/`)
