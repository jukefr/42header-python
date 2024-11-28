"""
42 Header Generator

A tool to generate and update 42 school-style headers for various programming files.
"""

import os
import sys
import re
from datetime import datetime
from .constants import ASCII_ART, COMMENT_STYLES, HEADER_LENGTH, MARGIN

def get_comment_style(filename):
    """Determine the comment style based on the file extension."""
    for pattern, style in COMMENT_STYLES.items():
        if re.search(pattern, filename):
            return style
    return '#', '#', '*'  # default comment style

def format_line(start, left_text, right_text, end):
    """Format a line within the header, adjusting left and right padding."""
    left_padded = left_text.ljust(HEADER_LENGTH - 2 * MARGIN - len(right_text))
    return f"{start}{' ' * (MARGIN - len(start))}{left_padded}{right_text}{' ' * (MARGIN - len(end))}{end}"

def generate_header(filename):
    """Generate the complete header for a file."""
    start, end, fill = get_comment_style(filename)
    lines = []
    username = os.getenv('USER', 'marvin')
    email = os.getenv('MAIL', 'marvin@42.fr')
    
    # Top line
    lines.append(f"{start} {fill * (HEADER_LENGTH - len(start) - len(end) - 2)} {end}")
    lines.append(format_line(start, "", "", end))
    
    # Lines with ASCII art and metadata
    lines.append(format_line(start, "", ASCII_ART[0], end))
    lines.append(format_line(start, filename, ASCII_ART[1], end))
    lines.append(format_line(start, "", ASCII_ART[2], end))
    lines.append(format_line(start, f"By: {username} <{email}>", ASCII_ART[3], end))
    lines.append(format_line(start, "", ASCII_ART[4], end))
    creation_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    lines.append(format_line(start, f"Created: {creation_date} by {username}", ASCII_ART[5], end))
    lines.append(format_line(start, f"Updated: {creation_date} by {username}", ASCII_ART[6], end))
    
    lines.append(format_line(start, "", "", end))
    lines.append(f"{start} {fill * (HEADER_LENGTH - len(start) - len(end) - 2)} {end}")
    
    return lines

def insert_header(filename, content):
    """Insert the header at the start of the file content."""
    header = generate_header(filename)
    return '\n'.join(header) + '\n\n' + content

def update_header(filename, content):
    """Update the header in the file content or create a new one if it doesn't exist."""
    start, end, _ = get_comment_style(filename)
    updated_line_prefix = f"{start}{' ' * (MARGIN - len(start))}Updated: "
    username = os.getenv('USER', 'marvin')
    current_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    updated_line = format_line(start, f"Updated: {current_date} by {username}", ASCII_ART[6], end)

    lines = content.splitlines(True)
    for i, line in enumerate(lines):
        if line.startswith(updated_line_prefix):
            lines[i] = updated_line + '\n'
            return ''.join(lines)
    
    return insert_header(filename, content)

def main():
    """
    Command-line entry point for the header generator.
    Reads from stdin and writes to stdout, making it suitable for use in text processing pipelines.
    """
    if len(sys.argv) != 2:
        print("Usage: header42 <filename>", file=sys.stderr)
        sys.exit(1)
    filename = sys.argv[1]
    try:
        content = sys.stdin.read()
        result = update_header(filename, content)
        print(result, end='')
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
