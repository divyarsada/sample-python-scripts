#!/bin/sh
from argparse import ArgumentParser
import sys

parser = ArgumentParser(description='Reading the contents of from the file in reverse and printing the same')
parser.add_argument('filename', help='Name of the  file to read from')
parser.add_argument('--limit', '-l', type=int, help='the no of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()
print(args)

try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(1)
else:
    with f:
        lines = f.readlines()
        lines.reverse()

