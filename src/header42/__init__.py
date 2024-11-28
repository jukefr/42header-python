"""
42 Header Generator Package

A tool for generating and updating 42 school-style headers in source code files.
"""

from .header import generate_header, insert_header, update_header

__version__ = "1.0.0"
__author__ = "Kate Jullien"
__email__ = "kate@juke.fr"

__all__ = ['generate_header', 'insert_header', 'update_header']
