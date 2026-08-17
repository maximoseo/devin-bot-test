#!/usr/bin/env python3
"""Print a greeting along with the current UTC time."""

from datetime import datetime, timezone


def main() -> None:
    now = datetime.now(timezone.utc)
    print("Hello from Devin bot E2E test")
    print(f"Current UTC time: {now.strftime('%Y-%m-%d %H:%M:%S')} UTC")


if __name__ == "__main__":
    main()
