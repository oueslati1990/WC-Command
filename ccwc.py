#!/usr/bin/env python3
"""
ccwc - A Python implementation of the Unix wc (word count) command
"""

import sys
import argparse


def count_bytes(content: bytes):
    """
    Count the number of bytes in the content.

    Args:
        content: bytes object containing the file content

    Returns:
        int: number of bytes
    """
    # len() on bytes gives us the byte count
    return len(content)


def count_lines(content: bytes):
    """
    Count the number of lines (newline characters) in the content.

    Args:
        content: bytes object containing the file content

    Returns:
        int: number of lines
    """
    lines = content.count(b"\n")

    return lines 


def count_words(content: bytes):
    """
    Count the number of words in the content.

    Args:
        content: bytes object containing the file content

    Returns:
        int: number of words
    """
    words = content.split()
    
    return len(words)


def count_characters(content: bytes):
    """
    Count the number of characters (not bytes) in the content.

    Args:
        content: bytes object containing the file content

    Returns:
        int: number of characters

    Raises:
        UnicodeDecodeError: if content cannot be decoded as UTF-8
    """
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        # Try with error handling - replace invalid chars
        text = content.decode("utf-8", errors="replace")

    return len(text)


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

    # Read the file content
    try:
        if args.filename:
            content = read_file(args.filename)
        else:
            # Read from stdin in binary mode
            content = sys.stdin.buffer.read()
    except FileNotFoundError:
        print(f"ccwc: {args.filename}: No such file or directory", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"ccwc: {args.filename}: Permission denied", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"ccwc: {args.filename}: {e}", file=sys.stderr)
        sys.exit(1)

    # Process based on which flag was provided
    # Default behavior: show lines, words, and bytes (like wc)
    if not (args.bytes or args.lines or args.words or args.chars):
        args.lines = True
        args.words = True
        args.bytes = True

    # Collect results in the correct order (lines, words, bytes/chars)
    results = []

    if args.lines:
        results.append(str(count_lines(content)))

    if args.words:
        results.append(str(count_words(content)))

    if args.bytes:
        results.append(str(count_bytes(content)))

    if args.chars:
        results.append(str(count_characters(content)))

    # Format output like wc: counts followed by filename (if provided)
    output = " ".join(results)
    if args.filename:
        output += f" {args.filename}"
    print(output)
        


if __name__ == '__main__':
    main()
