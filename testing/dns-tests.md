# DNS Tests

## DNS lookup
## DNS lookup test
- Command: `nslookup google.com`
- DNS server used: `185.228.168.85`
- Resolution successful: Yes
- Example resolved IP: `142.251.29.138`

```text
Server:         185.228.168.85
Address:        185.228.168.85#53

Non-authoritative answer:
Name:   google.com
Address: 142.251.29.138
```

## Interpretation
- DNS resolution was working during baseline checks.
- Successful DNS lookup supports that internet service was available.
Server:		185.228.168.85
Address:	185.228.168.85#53

Non-authoritative answer:
Name:	google.com
Address: 142.251.29.138
```

## DNS interpretation
- DNS resolution was working during baseline testing.
- Name resolution success supports that internet service was available.
## Test Environment

- Device used: MacBook Air
- Connection type: Wi-Fi
- Active interface: `en0`
- DNS server used: `185.228.168.85`
- Network type: Guest Wi-Fi network

## DNS Test: google.com

Command used:

```bash
nslookup google.com

Result summary:

Domain tested: google.com
DNS server used: 185.228.168.85
Resolution successful: Yes
Example resolved IP address: 142.251.29.138

Observed output summary:

Server: 185.228.168.85
Address: 185.228.168.85#53

Non-authoritative answer:
Name: google.com
Address: 142.251.29.138

Conclusion:

DNS resolution was successful. The device was able to resolve google.com into IP addresses using the configured DNS server.

This confirmed that DNS was working during the baseline test.


Save it.

Then run:

```bash
cat testing/dns-tests.md
