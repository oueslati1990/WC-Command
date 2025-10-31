# WC Command - Key Features & Implementation Guide

## Project Overview
Build `ccwc` (Coding Challenges Word Count) - a Python implementation of the Unix `wc` command-line tool that counts bytes, lines, words, and characters in text files or standard input.

## Key Features to Implement

### 1. Command-Line Argument Parsing
**What it does:** Parse flags and file arguments from the command line
**Options to support:**
- `-c` : Count bytes
- `-l` : Count lines
- `-w` : Count words
- `-m` : Count characters (multibyte aware)
- No flags: Default behavior (show lines, words, and bytes)

**Example usage:**
```bash
python ccwc.py -c test.txt          # Output: 342190 test.txt
python ccwc.py -l test.txt          # Output: 7145 test.txt
python ccwc.py -w test.txt          # Output: 58164 test.txt
python ccwc.py -m test.txt          # Output: 339292 test.txt
python ccwc.py test.txt             # Output: 7145 58164 342190 test.txt
```

### 2. File Reading
**What it does:** Read content from a specified file path
**Key considerations:**
- Handle file not found errors gracefully
- Read file in binary mode for byte counting
- Read file with proper encoding for character counting

### 3. Standard Input (stdin) Support
**What it does:** Read from stdin when no filename is provided
**Example usage:**
```bash
cat test.txt | python ccwc.py -l   # Output: 7145
echo "hello world" | python ccwc.py -w  # Output: 2
```

### 4. Counting Functions

#### Byte Count (`-c`)
- Count total number of bytes in the file
- Simply get file size or length of binary content

#### Line Count (`-l`)
- Count number of newline characters (`\n`)
- Each newline represents end of a line

#### Word Count (`-w`)
- Count sequences of non-whitespace characters
- Words are separated by spaces, tabs, newlines

#### Character Count (`-m`)
- Count actual characters (not bytes)
- Handle multibyte UTF-8 characters correctly
- Example: "café" is 4 characters but 5 bytes

### 5. Output Formatting
**Format:** `[count] [filename]` or just `[count]` for stdin
**Examples:**
- Single flag: `342190 test.txt`
- Multiple values: `7145 58164 342190 test.txt`
- From stdin: `7145` (no filename)

**Important:** Values should be right-aligned with proper spacing

## Implementation Steps (Suggested Order)

### Step 1: Project Setup
- Create `ccwc.py` main script
- Set up basic command-line argument parsing
- Create helper function to read file content

### Step 2: Implement Byte Count (`-c`)
- Read file in binary mode
- Count total bytes
- Format and print output

### Step 3: Implement Line Count (`-l`)
- Count newline characters in file
- Handle both file and stdin input

### Step 4: Implement Word Count (`-w`)
- Split content by whitespace
- Count resulting words

### Step 5: Implement Character Count (`-m`)
- Read file with UTF-8 encoding
- Count characters (not bytes)
- Handle multibyte characters

### Step 6: Default Behavior
- When no flags provided, show lines, words, and bytes
- Format output correctly with all three values

### Step 7: Standard Input Support
- Detect when no filename is provided
- Read from `sys.stdin`
- Format output without filename

### Step 8: Testing & Error Handling
- Test with various file types and sizes
- Handle errors (file not found, permission denied)
- Test with stdin piping
- Test with multibyte characters

## Python Concepts You'll Learn

1. **Command-line argument parsing** - Using `sys.argv` or `argparse` module
2. **File I/O** - Reading files in binary and text mode
3. **String manipulation** - Splitting text, counting characters
4. **Standard input/output** - Reading from `sys.stdin`
5. **Error handling** - Try/except blocks for file operations
6. **Encoding** - Understanding bytes vs characters (UTF-8)

## Test File
You can download a test file from the challenge:
```bash
wget https://www.dropbox.com/scl/fi/w14h890swx1g8dkueqzse/test.txt?rlkey=5pyx5kqf5zuasx5d2xf8mhj7q&st=q9kq78fe&dl=0 -O test.txt
```

Expected outputs for this test file:
- `-c`: 342190 bytes
- `-l`: 7145 lines
- `-w`: 58164 words
- `-m`: 339292 characters

## Success Criteria
Your implementation should:
- Pass all the test cases with the provided test file
- Handle both file input and stdin
- Match the exact output format of the Unix `wc` command
- Handle errors gracefully
- Follow Unix philosophy (simple, composable tool)
