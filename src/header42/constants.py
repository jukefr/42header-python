"""Constants used by the 42 header generator."""

# Header configuration
HEADER_LENGTH = 80
MARGIN = 5

# ASCII art for the header
ASCII_ART = [
    "        :::      ::::::::",
    "      :+:      :+:    :+:",
    "    +:+ +:+         +:+  ",
    "  +#+  +:+       +#+     ",
    "+#+#+#+#+#+   +#+        ",
    "     #+#    #+#          ",
    "    ###   ########.fr    "
]

# File extensions and their comment styles
COMMENT_STYLES = {
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
