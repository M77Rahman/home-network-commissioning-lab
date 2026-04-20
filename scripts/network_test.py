#!/usr/bin/env python3
"""
Basic network test helper script.

This script is intentionally simple and beginner-friendly. It runs a small
set of commands and prints output so you can copy real results into the
`testing/` markdown files.
"""

from __future__ import annotations

import platform
import subprocess
from typing import List


def run_command(command: List[str]) -> None:
    """Run a command and print output safely."""
    print(f"\n$ {' '.join(command)}")
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False)
    except FileNotFoundError:
        print("Command not found on this system.")
        return

    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip())


def main() -> None:
    system = platform.system().lower()

    print("Home Network Commissioning Lab - Basic Test Runner")
    print("Copy relevant output into the markdown files in testing/.")

    if "windows" in system:
        commands = [
            ["ipconfig", "/all"],
            ["ping", "-n", "4", "8.8.8.8"],
            ["nslookup", "bbc.co.uk"],
            ["tracert", "bbc.co.uk"],
        ]
    else:
        commands = [
            ["ip", "a"],
            ["ip", "route"],
            ["ping", "-c", "4", "8.8.8.8"],
            ["nslookup", "bbc.co.uk"],
            ["traceroute", "bbc.co.uk"],
        ]

    for command in commands:
        run_command(command)


if __name__ == "__main__":
    main()
