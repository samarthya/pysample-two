#!/usr/bin/env python3

"""Main executable
    Uses the capability of the function filler
"""
import argparse
import sys

import filer


def main(fpath: str, lin: int) -> None:
    """main

    Args:
        file_path (str): File path
        line_number (int): Line to read
    """
    fil = filer.Filer(fpath, 20)
    print("Line read : ", fil.read_line(lin))


if __name__ == "__main__":
    print(f"- Welcome - \nSystem Version :{sys.version}\n\n")
    parser = argparse.ArgumentParser(
        description='Parses the file and dumps a line')

    parser.add_argument('-f', '--file', help='Input file path', required=True)
    parser.add_argument('-l', '--lines', type=int,
                        help='Line to read from file', default=10)
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Turn on verbose mode')

    if len(sys.argv) < 3:
        parser.print_usage()
        sys.exit(1)

    args = parser.parse_args()

    print("Input file:", args.file)
    print("Number of lines:", args.lines)
    print("Verbose:", args.verbose)

    file_path = args.file
    line_number = args.lines
    main(file_path, line_number)
