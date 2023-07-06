#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Function that checks if available
    keys can ulock available boxes
    """
    # return false if first box is empty
    if len(boxes[0]) == 0:
        return False
    for box in boxes:
        # skip first box
        if box == boxes[0]:
            continue
        # return false if box is empty
        if len(box) == 0:
            return False
        # return false if box is not reachable
        if box not in boxes[0]:
            return False
    return True