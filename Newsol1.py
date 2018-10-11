import time
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


lst = [1, 2, 3]
a = lst.index(max(lst))
print(a)