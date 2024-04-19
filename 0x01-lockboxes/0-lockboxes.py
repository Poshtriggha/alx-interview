#!/usr/bin/python3
"""A method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if type(boxes) is not list:
        return False

    if len(boxes) == 0:
        return False

    # Initialize a list to keep track of keys that have been discovered
    the_keys = [0]
    
    # Iterate through the discovered keys
    for k in the_keys:
        # Iterate through the keys in the current box
        for b in boxes[k]:
            # Check if the key has not been discovered yet and it's a valid key
            if b not in the_keys and b != k and 0 < b < len(boxes):
                the_keys.append(b)
    
    # Check if all boxes can be opened
    return len(the_keys) == len(boxes)
