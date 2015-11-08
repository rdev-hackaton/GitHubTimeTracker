#!/usr/bin/env python
import sys
from random import choice

from time_tracker.utils import parse_time_entry

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        content = f.read()

    # Add a cool "little big detail"
    message = choice([
        "Add more tests",
        "Fixes #9001",
        "Fixes infinite loop"
        "Flake8",
        "Hotfix",
        "Initial commit",
        "Optimize the Foobar class",
        "Reduce the potential yak shaving",
        "Y2K protection",
    ])

    if not parse_time_entry(content):
        print("Please include the amount of time "
              "spent on this commit in the commit message.")
        print("E.g. \":clock1: 5m | {}\"".format(message))
        print("Failed to commit.")
        sys.exit(1)
