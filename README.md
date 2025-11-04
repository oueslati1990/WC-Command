# ccwc - Custom Word Count Command

A Python implementation of the Unix `wc` (word count) command-line tool. This project provides a cross-platform utility to count bytes, lines, words, and characters in text files.

## Description

`ccwc` is a command-line tool that mimics the functionality of the standard Unix `wc` command. It reads files (or standard input) and outputs various statistics about the content, including:

- Number of bytes
- Number of lines
- Number of words
- Number of characters (UTF-8 aware)

The tool handles binary file reading and UTF-8 decoding for accurate character counting across different encodings.

## Installation

### Prerequisites

- Python 3.7 or higher

### Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd WC-Command
```

2. Install the package:
```bash
pip install -e .
```

This will install `ccwc` as a command-line tool that you can run from anywhere.

### Alternative: Run directly without installation

You can also run the script directly with Python:
```bash
python3 ccwc.py [OPTIONS] [FILE]
```


## Usage

### Basic Syntax

```bash
ccwc [OPTIONS] [FILE]
```

### Available Flags

| Flag | Long Form | Description |
|------|-----------|-------------|
| `-c` | `--bytes` | Count the number of bytes |
| `-l` | `--lines` | Count the number of lines |
| `-w` | `--words` | Count the number of words |
| `-m` | `--chars` | Count the number of characters (UTF-8 aware) |

### Examples

**Count bytes in a file:**
```bash
ccwc -c test.txt
# Output: 342190 test.txt
```

**Count lines in a file:**
```bash
ccwc -l test.txt
# Output: 7145 test.txt
```

**Count words in a file:**
```bash
ccwc -w test.txt
# Output: 58164 test.txt
```

**Count characters in a file:**
```bash
ccwc -m test.txt
# Output: 339292 test.txt
```

**Default behavior (no flags) - shows lines, words, and bytes:**
```bash
ccwc test.txt
# Output: 7145 58164 342190 test.txt
```

**Read from standard input:**
```bash
cat test.txt | ccwc -l
# Output: 7145
```

**Combine multiple flags:**
```bash
ccwc -l -w test.txt
# Output: 7145 58164 test.txt
```

### Default Behavior

When no flags are specified, `ccwc` displays three counts in this order:
1. Number of lines
2. Number of words
3. Number of bytes

This matches the default behavior of the standard Unix `wc` command.
