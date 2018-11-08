import time
import math
from collections import Counter


def odd1(n):
    """odd or not using &
    """
    if n & 1== 0:
        return "偶数"
    return "奇数"


def odd2(n):
    """odd or not using %
    """
    if n % 2 == 0:
        return "偶数"
    return "奇数"


lookup = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
}
print(lookup['2'][0])
