#!/usr/bin/python3

import time
from datetime import datetime


def write_to_file(filename):
    """
    Writes lines to a file, each line containing a sequence number and a timestamp.

    Args:
    filename (str): The name of the file to write to.

    This function opens a file in write mode, which means it will overwrite the existing file
    if it already exists. It writes 26 lines to the file, each with a unique number and the
    current timestamp. There is a 1-second pause between each write.
    """
    with open(filename, 'w') as file:
        for i in range(26):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # looks like 2023-12-15 17:55:33
            line = f"Write Line: {i} {timestamp}\n"
            print(line.strip())
            file.write(line)
            time.sleep(1)  # Pause for 1 second between writes for demonstration purposes.


def append_to_file(filename):
    """
    Appends lines to a file, each line containing a sequence number and a timestamp.

    Args:
    filename (str): The name of the file to append to.

    This function opens a file in append mode. If the file does not exist, it gets created.
    It appends 26 lines to the file, each with a unique number and the current timestamp.
    There is a 1-second pause between each append.
    """
    with open(filename, 'a') as file:
        for i in range(26):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            line = f"Append Line: {i} {timestamp}\n"
            print(line.strip())
            file.write(line)
            time.sleep(1)


def read_from_file(filename):
    """
    Reads lines from a file and prints them to the console.

    Args:
    filename (str): The name of the file to read from.

    This function opens a file in read mode and reads all its lines into a list. It then
    iterates over the list, printing each line with its line number. There is a 1-second
    pause between printing each line.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            print(f"{i}: {line.strip()}")
            time.sleep(1)


def main():
    """
    Main function to demonstrate file operations.

    This function demonstrates writing to, appending to, and reading from files.
    It uses two files, 'file1.txt' and 'file2.txt', to showcase these operations.
    """
    write_to_file("file1.txt")
    append_to_file("file2.txt")
    read_from_file("file1.txt")
    read_from_file("file2.txt")

    """ 
    4.3 Add an infinite loop to your code.
    while True:
        write_to_file("file1.txt")
        append_to_file("file2.txt")
    """
    exit(1)


if __name__ == "__main__":
    main()
