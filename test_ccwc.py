#!/usr/bin/env python3
"""
Tests for ccwc - word count command implementation
Starting with byte count (-c flag)
"""

import subprocess


def run_ccwc(args):
    """
    Helper function to run ccwc.py with given arguments

    Args:
        args: list of command-line arguments

    Returns:
        tuple: (stdout, stderr, return_code)
    """
    cmd = ['python3', 'ccwc.py'] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def test_chars_count():
    """Test -m flag for char counting"""
    print("Testing: Char count with -m flag")

    stdout, stderr, returncode = run_ccwc(['-m','test.txt'])

    print(f" Output: {stdout}")
    print(f" Errors: {stderr}")
    print(f" Return code: {returncode}")

    # Check if command succeeded
    assert returncode == 0, f"Command failed with errors : {stderr}"

    # Check if output contains a number and filename
    assert 'test.txt' in stdout, f"Expected filename in output, got '{stdout}'"

    # Extract and verify we got a valid words count
    parts = stdout.split()
    assert len(parts) == 2, f"Expected '# filename' format, got '{stdout}'"

    chars_count = int(parts[0])
    print(f" Chars count : {chars_count}")

    # Verify it's a positive number
    assert chars_count > 0, f"Expected positive chars count, got {chars_count}"

    print("  ✓ Test passed!")

def test_words_count():
    """Test -w flag for word counting"""
    print("Testing: Word count with -w flag")

    stdout, stderr, returncode = run_ccwc(['-w', 'test.txt'])

    print(f" Output: {stdout}")
    print(f" Errors: {stderr}")
    print(f" Return code: {returncode}")

    # Check if command succeeded
    assert returncode == 0, f"Command failed with errors : {stderr}"

    # Check if output contains a number and filename
    assert 'test.txt' in stdout, f"Expected filename in output, got '{stdout}'"

    # Extract and verify we got a valid words count
    parts = stdout.split()
    assert len(parts) == 2, f"Expected '# filename' format, got '{stdout}'"

    words_count = int(parts[0])
    print(f" Words count : {words_count}")

    # Verify it's a positive number
    assert words_count > 0, f"Expected positive words count, got {words_count}"

    print("  ✓ Test passed!")


def test_lines_count():
    """Test -l flag for lines counting"""
    print("Testing: Lines count with -l flag")

    stdout, stderr, returncode = run_ccwc(['-l', 'test.txt'])

    print(f"  Output: {stdout}")
    print(f"  Errors: {stderr}")
    print(f"  Return code: {returncode}")

    # Check if command succeeded
    assert returncode == 0, f"Command failed with: {stderr}"

    # Check if output contains a number and filename
    assert 'test.txt' in stdout, f"Expected filename in output, got '{stdout}'"

    # Extract and verify we got a valid lines count
    parts = stdout.split()
    assert len(parts) == 2, f"Expected '# filename' format, got '{stdout}'"

    lines_count = int(parts[0])
    print(f"  Lines count: {lines_count}")

    # Verify it's a positive number
    assert lines_count > 0, f"Expected positive lines count, got {lines_count}"

    print("  ✓ Test passed!")

def test_byte_count():
    """Test -c flag for byte counting"""
    print("Testing: Byte count with -c flag")

    stdout, stderr, returncode = run_ccwc(['-c', 'test.txt'])

    print(f"  Output: {stdout}")
    print(f"  Errors: {stderr}")
    print(f"  Return code: {returncode}")

    # Check if command succeeded
    assert returncode == 0, f"Command failed with: {stderr}"

    # Check if output contains a number and filename
    assert 'test.txt' in stdout, f"Expected filename in output, got '{stdout}'"

    # Extract and verify we got a valid byte count
    parts = stdout.split()
    assert len(parts) == 2, f"Expected '# filename' format, got '{stdout}'"

    byte_count = int(parts[0])
    print(f"  Byte count: {byte_count}")

    # Verify it's a positive number
    assert byte_count > 0, f"Expected positive byte count, got {byte_count}"

    print("  ✓ Test passed!")

def test_default_behaviour():
    """Test default behaviour : lines, words, bytes count"""
    print("Testing: default behaviour with no flags")
    stdout, stderr, returncode = run_ccwc(['test.txt'])

    print(f"  Output: {stdout}")
    print(f"  Errors: {stderr}")
    print(f"  Return code: {returncode}")

    # Check if command succeeded
    assert returncode == 0, f"Test failed with errors : {stderr}"

    # Check if output contains a number and filename
    assert 'test.txt' in stdout, f"Expected filename in output, got '{stdout}'"

    # Extract and verify we got a valid byte count, words count and lines count
    parts = stdout.split()
    
    # Verify the format is correct 
    assert len(parts) == 4, f"Format not as expected"

    # byte count, words count and lines count must be positive
    lines_count = int(parts[0])
    words_count = int(parts[1])
    bytes_count = int(parts[2])
    assert lines_count >= 0, f"Number of lines should be positive, got {lines_count}"
    assert words_count >= 0, f"Number of words should be positive, got {words_count}"
    assert bytes_count >= 0, f"Number of bytes should be positive, got {bytes_count}"

    print("  ✓ Test passed!")

if __name__ == '__main__':
    print("=" * 50)
    print("Testing ccwc - Byte Count Feature")
    print("=" * 50)

    try:
        test_byte_count()
        test_chars_count()
        test_lines_count()
        test_words_count()
        test_default_behaviour()
        print("\n✓ All tests passed!")
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        exit(1)
