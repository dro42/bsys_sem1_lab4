#!/usr/bin/python3

import sys
import time


def main():
    """
    To run this script, use a command like python script.py 2, where 2 is the number of gigabytes of memory you want
    to allocate. This script will create a string occupying the specified amount of memory and then enter an infinite
    loop, printing "true" every second. Please be cautious with the value you provide as the command-line argument,
    as very large values can consume a significant amount of your system's memory and potentially lead to system
    instability. :return:
    """
    # Check if the command line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <memory_in_gb>")
        sys.exit(1)

    try:
        # Convert the first command-line argument to an integer
        gigabytes = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for memory size in GB.")
        sys.exit(1)

    # Allocate a string of 'gigabytes' GB in size
    some_str = ' ' * 1024 * 1024 * 1024 * gigabytes

    # Infinite loop
    while True:
        print("true")
        time.sleep(1)


if __name__ == "__main__":
    main()
