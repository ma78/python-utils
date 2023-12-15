#!/usr/bin/python3 -u

"""
Sleep until specified timestamp
"""

from datetime import datetime

import argparse
import signal
import sys
import time


###
# GLOBALS
###

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


###
# MAIN METHOD
###


def main():
    """Main method"""
    args = check_args()

    # Grab time values
    timestamp = datetime.strptime(args.timestamp, DATE_FORMAT)
    present = datetime.today()

    # Check input
    if present > timestamp:
        print("error: timestamp value in the past")
        sys.exit(1)

    # Determine time in seconds between timestamp and present
    pending_time = timestamp - present

    # Sleep until required time
    sleep_until(pending_time.seconds)

    # Finished
    present = datetime.strftime(datetime.today(), DATE_FORMAT)
    print()
    print(" -> Done.")
    print(f" -> Current time: {present}")
    print()


def sleep_until(seconds):
    """Sleep until seconds run out"""
    print(f" -> sleeping ({seconds}s) ", end="")

    # Keep track of when to print newline
    marker = 0

    for i in range(seconds):
        print(".", end="")

        # Sleep 1 second
        time.sleep(1)

        # Update marker
        marker += 1

        if marker == 60:
            print()
            print(f" -> sleeping ({seconds - i - 1}s) ", end="")
            marker = 0

    return seconds


def check_args():
    """Process cli args"""
    script_name = sys.argv[0]

    # Setup parser
    parser = argparse.ArgumentParser(description=f"example: {script_name} -t '2023-09-14 14:23:00'")

    # Must escape % characters for use with help string
    help_str = "timestamp, format: " + DATE_FORMAT.replace(r"%", r"%%")

    # Set timestamp arg
    parser.add_argument("-t", required=True, dest="timestamp", help=help_str)

    return parser.parse_args()


# pylint: disable=W0613
def signal_handler(sig, frame):
    """Control signal handler"""
    print(" ")
    sys.exit(0)


# Set up Ctrl-C handler
signal.signal(signal.SIGINT, signal_handler)


####
# MAIN
####

# Invoke main method
if __name__ == "__main__":
    main()
