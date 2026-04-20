# Baseline Tests

## Purpose
Record standard baseline checks before troubleshooting.

## Test Environment
- Date/Time: [Placeholder]
- Tester: [Placeholder]
- Test Device: [Placeholder]
- Connection Type: [Placeholder]

## Baseline Test Plan
1. Verify local IP configuration.
2. Ping default gateway.
3. Ping public DNS (e.g., 8.8.8.8).
4. Resolve and ping a public domain.
5. Run traceroute to a public domain.
6. Verify DNS lookup timing/consistency.

## Commands Used
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

## Baseline Status
- [ ] Completed successfully
- [ ] Issues detected (see troubleshooting folder)
