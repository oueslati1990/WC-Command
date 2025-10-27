#!/usr/bin/env python3
"""
ccwc - A Python implementation of the Unix wc (word count) command
"""

import sys
import argparse


def count_bytes(content):
    """
    Count the number of bytes in the content.

    Args:
        content: bytes object containing the file content

    Returns:
        int: number of bytes
    """
    
    pass


def count_lines(content):
    """
    Count the number of lines (newline characters) in the content.

    Args:
        content: bytes object containing the file content

    Returns:
        int: number of lines
    """
    
    pass


def count_words(content):
    """
    Count the number of words in the content.

    Args:
        content: bytes object containing the file content

    Returns:
        int: number of words
    """
    
    pass


def count_characters(content):
    """
    Count the number of characters (not bytes) in the content.

    Args:
        content: bytes object containing the file content

    Returns:
        int: number of characters
    """
    
    pass


def read_file(filename):
    """
    Read file content in binary mode.

    Args:
        filename: path to the file to read

    Returns:
        bytes: file content as bytes
    """
    with open(filename, 'rb') as f:
        return f.read()


def main():
    """
    Main function to parse arguments and execute the appropriate counting operation.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='ccwc - count bytes, lines, words, and characters in files'
    )

    # Add optional flags
    parser.add_argument('-c', '--bytes', action='store_true',
                        help='count bytes')
    parser.add_argument('-l', '--lines', action='store_true',
                        help='count lines')
    parser.add_argument('-w', '--words', action='store_true',
                        help='count words')
    parser.add_argument('-m', '--chars', action='store_true',
                        help='count characters')

    # Add filename argument (optional, for stdin support later)
    parser.add_argument('filename', nargs='?', default=None,
                        help='file to analyze (if not provided, reads from stdin)')

    # Parse the arguments
    args = parser.parse_args()

    print(f"Arguments received:")
    print(f"  Bytes flag (-c): {args.bytes}")
    print(f"  Lines flag (-l): {args.lines}")
    print(f"  Words flag (-w): {args.words}")
    print(f"  Chars flag (-m): {args.chars}")
    print(f"  Filename: {args.filename}")


if __name__ == '__main__':
    main()
