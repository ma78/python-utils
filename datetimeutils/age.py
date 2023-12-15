#!/usr/bin/python3 -u

"""
Convert elapsed time to short, printable format
"""

from datetime import datetime

import argparse
import sys


###
# GLOBALS
###

DATE_FORMAT = "%Y-%m-%d %H:%M:%S %Z"


###
# MAIN METHOD
###


def main():
    """Main method"""
    args = check_args()

    # Grab time values
    timestamp = datetime.strptime(args.timestamp, DATE_FORMAT)
    present = datetime.today()

    # Render age as simple string value
    age = convert_age(present - timestamp)
    print(age)


def convert_age(age, always_show_minutes=False):
    """Renders time difference (age) as short, printable string"""

    # Handle days differently
    if age.days:
        return convert_age_days(age, always_show_minutes)

    # Extract time units
    hours = age.seconds // 3600
    minutes = (age.seconds // 60) % 60
    seconds = age.seconds - (minutes * 60)

    if hours:
        return f"{hours}h{minutes}m"

    # Return seconds if less than a minute
    if age.seconds < 60:
        return f"0m{age.seconds}s" if always_show_minutes else f"{age.seconds}s"

    # Return minutes and seconds
    return f"{minutes}m{seconds}s"


def convert_age_days(age, always_show_minutes=False):
    """Handles time ranges in days"""
    if not age.days:
        sys.exit("error: elapsed time less than one day")

    # Extract time units
    hours = age.seconds // 3600
    minutes = (age.seconds // 60) % 60

    if age.days > 9:
        return f"{age.days}d"

    if always_show_minutes:
        return f"{age.days}d{hours}h{minutes}m"

    # Return just days and hours
    return f"{age.days}d{hours}h"


def check_args():
    """Process cli args"""
    script_name = sys.argv[0]

    # Setup parser
    parser = argparse.ArgumentParser(description=f"example: {script_name} -t '2023-09-14 14:23:00 AEST'")

    # Must escape % characters for use with help string
    help_str = "timestamp, format: " + DATE_FORMAT.replace(r"%", r"%%")

    # Set timestamp arg
    parser.add_argument("-t", required=True, dest="timestamp", help=help_str)

    return parser.parse_args()


####
# MAIN
####

# Invoke main method
if __name__ == "__main__":
    main()
