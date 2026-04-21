# Traceroute Results

## Traceroute to public domain
- Command: `traceroute google.com`
- Target: `google.com`
- Target IP used: `142.250.151.139`
- First responding hop: `10.104.64.2`
- Later hops: `* * *`
- Test completion: Stopped manually after repeated non-responses

```text
traceroute to google.com (142.250.151.139)
 1  10.104.64.2
 2  * * *
 3  * * *
 4  * * *
```

## Interpretation
- First-hop response confirmed local path visibility.
- Later-hop non-response is consistent with filtering or non-responsive intermediate devices.
- Combined with successful ping and DNS tests, this does not indicate internet outage.
