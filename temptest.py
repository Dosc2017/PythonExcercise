import numpy as np



"""


def CutWatermelon(n=3, k=1):
   
   
    if n == 1:
        return k + 1
    elif k == 1:
        return 2

    return CutWatermelon(n, k-1) + CutWatermelon(n-1, k-1)



from array import array
from random import random
from time import perf_counter as pc


float1 = array('d', (random() for i in range(10**5)))

t0 = pc()
fp = open('float.bin', 'wb')
float1.tofile(fp)
fp.close()
print(pc()-t0)

t1 = pc()
float2 = array('d')
fp = open('float.bin', 'rb')
float2.fromfile(fp, 10**5)
fp.close()
print(pc() - t1)


from collections import deque
dp = deque(range(5), maxlen=6)

print(dp)


"""
"""
import sys
# AQUAMAN！！！！
import re


word_re = re.compile(r'\w+')

index = {}
with open(sys.argv[0], encoding='utf-8')as fp:
    for line_no, line in enumerate(fp, 1):
        for match in word_re.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
"""
"""


somelist = somelist[1] = [0, 1]
print(somelist[1], somelist)
print(somelist == somelist[1])





def energy_send(x):
        # 初始化一个 numpy 数组
    return np.array([float(x)])


def energy_receive():
        # 返回一个空的 numpy 数组
    return np.empty((), dtype=np.float).tolist()


print(energy_receive(), energy_send(2), energy_receive())


x = {0: None}

for i in x:
    del x[i]
    x[i+1] = None
    print(i)
"""
