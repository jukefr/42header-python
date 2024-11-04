import os
import re
import time
from datetime import datetime

# ASCII Art and Configuration
ascii_art = [
    "        :::      ::::::::",
    "      :+:      :+:    :+:",
    "    +:+ +:+         +:+  ",
    "  +#+  +:+       +#+     ",
    "+#+#+#+#+#+   +#+        ",
    "     #+#    #+#          ",
    "    ###   ########.fr    "
]
header_length = 80
margin = 5
username = os.getenv('USER', 'marvin')
email = os.getenv('MAIL', 'marvin@42.fr')

# Define file types and their respective comment styles
comment_styles = {
    r'\.c$|\.h$|\.cc$|\.hh$|\.cpp$|\.hpp$|\.tpp$|\.ipp$|\.cxx$|\.go$|\.rs$|\.php$|\.py$|\.java$|\.kt$|\.kts$': ('/*', '*/', '*'),
    r'\.htm$|\.html$|\.xml$': ('<!--', '-->', '*'),
    r'\.js$|\.ts$': ('//', '//', '*'),
    r'\.tex$': ('%', '%', '*'),
    r'\.ml$|\.mli$|\.mll$|\.mly$': ('(*', '*)', '*'),
    r'\.vim$|vimrc$': ('"', '"', '*'),
    r'\.el$|\.emacs$|\.asm$': (';', ';', '*'),
    r'\.f90$|\.f95$|\.f03$|\.f$|\.for$': ('!', '!', '/'),
    r'\.lua$': ('--', '--', '-')
}

# Determine the comment style based on the file extension
def get_comment_style(filename):
    for pattern, style in comment_styles.items():
        if re.search(pattern, filename):
            return style
    return '#', '#', '*'  # default comment style

# Format a line within the header, adjusting left and right padding
def format_line(start, left_text, right_text, end):
    left_padded = left_text.ljust(header_length - 2 * margin - len(right_text))
    return f"{start}{' ' * (margin - len(start))}{left_padded}{right_text}{' ' * (margin - len(end))}{end}"

# Generate the header
def generate_header(filename):
    start, end, fill = get_comment_style(filename)
    lines = []
    
    # Top line
    lines.append(f"{start} {fill * (header_length - len(start) - len(end) - 2)} {end}")

    lines.append(format_line(start, "", "", end))
    
    # Lines with ASCII art and metadata
    lines.append(format_line(start, "", ascii_art[0], end))
    lines.append(format_line(start, filename, ascii_art[1], end))
    lines.append(format_line(start, "", ascii_art[2], end))
    lines.append(format_line(start, f"By: {username} <{email}>", ascii_art[3], end))
    lines.append(format_line(start, "", ascii_art[4], end))
    creation_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    lines.append(format_line(start, f"Created: {creation_date} by {username}", ascii_art[5], end))
    lines.append(format_line(start, f"Updated: {creation_date} by {username}", ascii_art[6], end))
    
    lines.append(format_line(start, "", "", end))

    # Bottom line
    lines.append(f"{start} {fill * (header_length - len(start) - len(end) - 2)} {end}")
    
    return lines

# Insert the header at the start of the file
def insert_header(filename):
    header = generate_header(filename)
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write('\n'.join(header) + '\n\n' + content)

# Update only the "Updated" line in the header if it exists
def update_header(filename):
    start, end, _ = get_comment_style(filename)
    updated_line_prefix = f"{start}{' ' * (margin - len(start))}Updated: "
    current_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    updated_line = format_line(start, f"Updated: {current_date} by {username}", ascii_art[6], end)
    
    with open(filename, 'r+') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith(updated_line_prefix):
                lines[i] = updated_line + '\n'
                break
        else:
            insert_header(filename)
            return

        f.seek(0)
        f.writelines(lines)

# Main function to check and update or insert header
def main(filename):
    try:
        if os.path.exists(filename):
            update_header(filename)
        else:
            print(f"File '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python 42header.py <filename>")
    else:
        main(sys.argv[1])
