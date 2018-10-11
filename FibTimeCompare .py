import time


def fib1(n):
    """
    fibonocci without dict
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


known = {0: 0, 1: 1}


def fib2(n):
    """
    fibonocci with dict

    """
    if n in known:
        return known[n]

    res = fib2(n-1) + fib2(n-2)
    known[n] = res
    return res


"""
runtime of fibonocci  with/without memo
"""

time_start = time.clock()

print(fib1(30))
time1 = time.clock()
print('time without dict:', time1 - time_start)

print(fib2(30))
time2 = time.clock()
print('time with dict:', time2 - time1)


