#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""

import sys

def process_input():
    """
    Reads stdin line by line and computes metrics.
    """
    lines_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                  '404': 0, '405': 0, '500': 0}
    line_count = 0
    total_size = 0

    try:
        for line in sys.stdin:
            line_list = line.split(" ")

            if len(line_list) > 4:
                status_code = line_list[-2]
                file_size = int(line_list[-1])

                if status_code in lines_dict:
                    lines_dict[status_code] += 1

                total_size += file_size
                line_count += 1

                if line_count == 10:
                    line_count = 0
                    print('File size: {}'.format(total_size))
                    print_status_codes(lines_dict)

    except Exception as err:
        pass

    finally:
        print('File size: {}'.format(total_size))
        print_status_codes(lines_dict)

def print_status_codes(status_dict):
    """
    Prints status codes and their counts.
    """
    for key, value in sorted(status_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

if __name__ == "__main__":
    process_input()
