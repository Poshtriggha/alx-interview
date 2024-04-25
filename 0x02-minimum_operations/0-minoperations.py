#!/usr/bin/python3
"""
AAA
"""

def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    clipboard = 1
    buffer = 1

    while buffer < n:
        if n % buffer == 0:
    
            clipboard = buffer
            operations += 1
        buffer += clipboard
        operations += 1

    return operations

# Testing the function
if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
