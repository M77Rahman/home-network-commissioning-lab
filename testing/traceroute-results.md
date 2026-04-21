# Traceroute Results

## Traceroute test to public domain
- Command: `traceroute google.com`
- Target: `google.com`
- Target IP used: `142.250.151.139`
- First responding hop: `10.104.64.2`
- Later hops: `* * *`
- Test completion: Stopped manually after repeated non-responses

```text
traceroute to google.com (142.250.151.139), 64 hops max
  1  10.104.64.2  ... ms  ... ms  ... ms
  2  * * *
  3  * * *
  4  * * *
  ...
```

## Traceroute interpretation
- The first hop responded from the local network.
- Repeated later-hop non-responses are consistent with filtered or non-responsive intermediate devices.
- Combined with successful ping and DNS results, this does not indicate that the internet was offline.
