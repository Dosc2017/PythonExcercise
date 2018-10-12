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


a = 123
b = str(a)[::-1]
print(b)
