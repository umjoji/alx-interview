#!/usr/bin/python3
"""
Checks if available keys can unlock boxes
"""


def canUnlockAll(boxes):
    """
    Function that checks if available
    keys can unlock available boxes
    Returns:
        True if all boxes can be opened
        False otherwise
    """
    # list of unused keys
    unused_keys = set()
    # first box and start condition
    box_num = 0
    opened_boxes = []
    num_of_boxes = len(boxes)
    while box_num < num_of_boxes:
        old_box_num = box_num
        # add box to opened boxes
        opened_boxes.append(box_num)
        # add keys in opened box to unused keys
        unused_keys.update(boxes[box_num])
        # check each individual key if it has a locked box
        for key_num in unused_keys:
            if key_num != 0 and key_num < num_of_boxes and \
                    key_num not in opened_boxes:
                # box can be opened
                box_num = key_num
                break
        # check if all keys have been used
        if old_box_num == box_num:
            break
        continue

    for box_num in range(num_of_boxes):
        # return false if all boxes not opened
        if box_num not in opened_boxes and box_num != 0:
            return False
    # True if all have been opened
    return True
