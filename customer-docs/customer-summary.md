# Customer Summary

## Overview
This document explains the recent guest Wi-Fi test results in plain language.

## What was checked
We checked:
- connection to the local network gateway,
- connection to public internet services,
- website name lookups (DNS),
- route visibility using traceroute.

## What was found
- A ping test to the local gateway was blocked.
- A traceroute test showed only the first step, with later steps hidden.
- Internet tests to external services were successful.
- DNS lookup tests were successful.

## Why this did **not** mean internet service was down
Some guest Wi-Fi networks intentionally limit diagnostic tools such as ping and traceroute for security reasons.

That means:
- certain technical tests can look "failed" or "incomplete", while
- normal internet access still works.

In this case, internet and DNS checks succeeded, so there was no full service outage.

## Final status
- Guest Wi-Fi internet service: **Operational**
- DNS/name lookup service: **Operational**
- Diagnostic tool visibility (ping/traceroute): **Partially filtered by design**

## What to do if you notice real connection issues
1. Reconnect your device to Wi-Fi.
2. Test more than one website/app.
3. Restart the affected device.
4. If only one device is affected, test with another device.
5. If all devices are affected, contact support and report:
   - when the issue started,
   - which devices are affected,
   - what still works and what does not.

## When to escalate
Escalate to network support if any of the following happen:
- websites/apps fail across multiple devices,
- DNS lookups fail (for example, websites cannot be found),
- internet access is unavailable for more than 15 minutes after basic checks,
- repeated intermittent drops affect normal use.

## Privacy note
Sensitive network values are masked in customer-facing documents.
