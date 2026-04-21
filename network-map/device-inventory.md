# Device Inventory

## Purpose
Record the devices and addressing context used during this lab evidence capture.

## Privacy note
Sensitive identifiers (full private IP, MAC address, exact site details) are intentionally masked.

## Recorded inventory
| Device Name | Device Type | Connection | IP Address | MAC Address | Location | Notes |
|---|---|---|---|---|---|---|
| MacBook Air | Client test device | Wi-Fi | 10.104.70.xxx | Masked | Lab environment | Baseline and troubleshooting tests run from this device |
| Guest Wi-Fi Gateway | Gateway/router | Wi-Fi upstream | 10.104.64.x | Not captured | Lab environment | Gateway diagnostics showed filtered ICMP behavior |

## Commissioning Notes
- The test device received a private client IP address.
- DNS server assignment was present on the guest Wi-Fi network.
- A default route was present for outbound traffic.
- External connectivity checks succeeded.
- ICMP/traceroute diagnostic filtering was observed.

## Inventory status
- Router/gateway context documented
- End-user test device documented
- Additional endpoint inventory was not captured in this evidence set
Document all known network devices (wired and wireless) with clear ownership and addressing details.

## Privacy note
If this repository is shared publicly, redact sensitive values before publishing (for example: full MAC addresses, serial numbers, and exact private IP plans).

## Inventory
## Instructions
List every device connected to the network, both wired and wireless.

## Inventory Table
| Device Name | Device Type | Connection (Wired/Wi-Fi) | IP Address | MAC Address | Owner/Location | Notes |
|---|---|---|---|---|---|---|
| [e.g., VM Hub 5] | [Router] | [Wired] | [192.168.x.x] | [AA:BB:CC:DD:EE:FF] | [Living Room] | [Main gateway] |
| [Add row] | [Add row] | [Add row] | [Add row] | [Add row] | [Add row] | [Add row] |

## Checklist
- [ ] Router/gateway documented
- [ ] Access points documented (if applicable)
- [ ] End-user devices documented
- [ ] IoT/smart home devices documented
- [ ] Access points documented (if any)
- [ ] End-user devices documented
- [ ] Smart/home IoT devices documented

# Device Inventory

| Device | Connection Type | Private IP | Purpose | Notes |
|---|---|---|---|---|
| Network gateway/router | Wi-Fi | 10.104.64.x | Default gateway | Routes traffic from the local network to the internet |
| MacBook Air | Wi-Fi | 10.104.70.xxx | Test device | Used to run ping, traceroute and DNS tests |

## Key Network Details

- Active network interface: `en0`
- Test device private IP: `10.104.70.xxx`
- Default gateway: `10.104.64.x`
- DNS servers: `185.228.168.85`, `185.228.169.85`
- Network type: Guest Wi-Fi network

## Privacy Notes

Sensitive details such as MAC addresses, full device identifiers and exact personal device names have been removed or masked.
