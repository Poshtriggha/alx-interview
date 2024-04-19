#!/usr/bin/python3
"""A method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    
    """
    if type(boxes) is not list:
        return False

    if len(boxes) == 0:
        return False

    
    the_keys = [0]
    
    
    for k in the_keys:
        
        for b in boxes[k]:
            
            if b not in the_keys and b != k and 0 < b < len(boxes):
                the_keys.append(b)
    
   
    return len(the_keys) == len(boxes)
