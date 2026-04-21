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
