#!/usr/bin/python3
"""
Module for validating UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing bytes of data.

    Returns:
        True if data is a valid UTF-8 encoding, else return False.
    """
    def countLeadingOnes(byte):
        count = 0
        mask = 1 << 7
        while byte & mask:
            count += 1
            mask >>= 1
        return count

    i = 0
    while i < len(data):
        leading_ones = countLeadingOnes(data[i])
        
        if leading_ones != 0 or (data[i] >> 6) == 2:
            return False
        
        elif leading_ones == 0 or leading_ones > 4:
            i += 1
            continue
        
        if i + leading_ones > len(data):
            return False
        
        for j in range(1, leading_ones):
            if (data[i+j] >> 6) != 2:
                return False
        
        i += leading_ones
    
    return True


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
