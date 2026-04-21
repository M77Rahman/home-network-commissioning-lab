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
# Baseline Network Tests

## Purpose

Record standard baseline checks before troubleshooting. These checks confirm the test device network configuration, internet connectivity, DNS resolution, and route visibility.

## Test Environment

- Date/Time: 20 April 2026
- Tester: Muhammad Emdadur Rahman
- Test device: MacBook Air
- Connection type: Wi-Fi
- Active interface: `en0`
- Private IP address: `10.104.70.xxx`
- Default gateway: `10.104.64.x`
- DNS servers: `185.228.168.85`, `185.228.169.85`
- Network type: Guest Wi-Fi network

## Commands Used

```bash
ifconfig
netstat -nr | grep default
scutil --dns
ipconfig getifaddr en0
ping -c 4 10.104.64.1
ping -c 4 8.8.8.8
ping -c 4 google.com
nslookup google.com
traceroute google.com
Baseline Test Summary
Test	Command	Result	Interpretation
IP configuration	ipconfig getifaddr en0	10.104.70.xxx	Test device had a valid private IP address
Default gateway check	netstat -nr | grep default	10.104.64.x via en0	Device had a default route through the Wi-Fi interface
DNS server check	scutil --dns	DNS servers detected	Device had reachable DNS servers configured
Default gateway ping	ping -c 4 10.104.64.1	100% packet loss / filtered	ICMP to gateway appeared blocked by network filtering
External IP ping	ping -c 4 8.8.8.8	0% packet loss	Internet connectivity to an external IP worked
External domain ping	ping -c 4 google.com	0% packet loss	External domain connectivity worked
DNS lookup	nslookup google.com	Successful	DNS resolution worked
Traceroute	traceroute google.com	First hop responded, later hops timed out	Traceroute replies appeared filtered after the first hop
Conclusion

The baseline tests showed that the device had working internet access and DNS resolution.

The failed gateway ping and partial traceroute did not indicate a full connectivity fault, because external IP and domain tests were successful. The results suggest that the guest Wi-Fi network filters some diagnostic traffic, such as ICMP or traceroute responses.

Baseline Status
 Completed successfully
 Filtering observed on gateway ping and traceroute
 Full outage detected
