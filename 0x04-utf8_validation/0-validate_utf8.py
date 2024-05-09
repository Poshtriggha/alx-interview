#!/usr/bin/python3
"""Represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Represents a valid UTF-8"""
    expected_len = 0

    for n in data:
        if expected_len == 0:
            if n >> 5 == 0b110 or n >> 5 == 0b1110:

                expected_len = 1
            elif n >> 4 == 0b1110:
                expected_len = 2
            elif n >> 3 == 0b11110:
                expected_len = 3

        
            elif n >> 7 == 0b1:
                return False
        else:
            if n >> 6 != 0b10:
                return False
            
            expected_len -= 1
    return expected_len == 0