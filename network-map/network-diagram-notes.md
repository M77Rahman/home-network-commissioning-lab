# Network Diagram Notes

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