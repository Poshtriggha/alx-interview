#!/usr/bin/python3
""" AAAAAAAAA """


def makeChange(coins, total):
    """  coins needed
    to meet a given amount total """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort in descending order
    changeMade = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        changeMade += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return changeMade
