#!/usr/bin/python3

import sys
from collections import defaultdict

def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))

def parse_line(line):
    parts = line.split()
    if len(parts) != 7:
        return None, None
    ip_address = parts[0]
    status_code = parts[5]
    file_size = parts[6]
    if not status_code.isdigit():
        return None, None
    return int(status_code), int(file_size)

total_size = 0
status_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        status_code, file_size = parse_line(line)
        if status_code is None:
            continue
        total_size += file_size
        status_counts[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)
except KeyboardInterrupt:
    print_stats(total_size, status_counts)
