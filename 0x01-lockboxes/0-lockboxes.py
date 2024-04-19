#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    """
    if not boxes:
        return False

    keys = set(boxes[0])
    unlocked = set([0])

    while keys:
        key = keys.pop()
        if key < len(boxes):
            unlocked.add(key)
            keys.update(boxes[key])

    return len(unlocked) == len(boxes)

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
