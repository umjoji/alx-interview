#!/usr/bin/python3
'''Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
'''
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    '''
    Return: fewest number of coins needed to get
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''
    if total <= 0:
        return 0
    table = [float('inf')] * (total + 1)
    table[0] = 0
    available_denominations = len(coins)
    for i in range(1, total + 1):
        for j in range(available_denominations):
            if coins[j] <= i:
                min_coins_for_remainder = table[i - coins[j]]
                if min_coins_for_remainder != float('inf') and min_coins_for_remainder + 1 < table[i]:
                    table[i] = min_coins_for_remainder + 1

    if table[total] == float('inf'):
        return -1
    return table[total]
