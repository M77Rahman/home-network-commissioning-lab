# Network Diagram Notes

## Purpose
Capture the confirmed topology details used in this troubleshooting scenario.

## Physical topology notes
- Test device (MacBook Air) connected to guest Wi-Fi
- Guest Wi-Fi segment connected to gateway infrastructure
- Internet reachability verified from the client device

## Logical topology notes
- Client private IP range observed: 10.104.70.xxx
- Gateway range observed: 10.104.64.x
- DNS servers used: 185.228.168.85 and 185.228.169.85
- Guest segment applies filtering that affects some diagnostic protocols

## Commissioning Notes
- The client was assigned private addressing on the guest segment.
- DNS servers were assigned and used for successful name resolution.
- A default route was present and outbound traffic succeeded.
- Public internet reachability checks were successful.
- Gateway ICMP and traceroute visibility were partially filtered.

## Diagram checklist status
- Internet-to-gateway relationship identified
- Client-to-gateway guest Wi-Fi path identified
- Key addressing ranges recorded in masked form
Capture the notes required to produce a clear physical and logical network diagram.

## Physical topology

## Logical topology

## Diagram checklist
- [ ] Draw internet-to-gateway link
- [ ] Draw wired segments
- [ ] Draw Wi-Fi coverage areas
- [ ] Label key IP ranges and gateway addresses
## Objective

Capture the basic logical path between the test device, the local network gateway and the internet.

## Basic Network Path

```text
Internet
   |
Guest Wi-Fi network gateway
   |
Wi-Fi network
   |
MacBook Air test device
Logical Topology Notes
Network type: Guest Wi-Fi network
Connection type: Wi-Fi
Active interface: en0
Test device private IP: 10.104.70.xxx
Default gateway: 10.104.64.x
DNS servers: 185.228.168.85, 185.228.169.85
VLANs: Not identified during testing
DHCP range: Not confirmed
Observations

The test device was connected to a guest Wi-Fi network using interface en0.

The network provided a private IP address and DNS servers. The default route was visible, but ICMP ping to the gateway was filtered. External IP and domain connectivity still worked, so the filtering did not indicate a full connectivity failure.

Diagram To-Do
 Document internet to gateway path
 Document Wi-Fi connection to test device
 Label key IP ranges and gateway
 Create a clean diagram image for GitHub
