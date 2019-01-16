"""
网页取数示意（伪）

"""

# 类别属性
# 输入： 属性C， 逻辑， 属性值

# 原有数据
"""
a1 = dict(owner_bag_no_come=None, owner_bag_no_sned=None, pda_code='自动分拣')
a2 = dict(owner_bag_no_come=1456, owner_bag_no_sned=None, pda_code='自动分拣')
a = (a1, a2)

for i in range(len(a)):
    if not a[i]['owner_bag_no_come']:
        a[i]['C'] = '前散后包'
    else:
        a[i]['C'] = '混包'


for i in range(len(a)):
    print('a[{0}]:'.format(i), a[i], '\n')



# 数值属性
# 输入： 属性N， 取值逻辑

b1 = dict(owner_bag_no_come=2345, owner_bag_no_sned=124, pda_code=None)
b2 = dict(owner_bag_no_come=1456, owner_bag_no_sned=None, pda_code='自动分拣')
b = (b1, b2)


import itertools
def add(a, b):
    pairs = itertools.zip_longest(a, b, fillvalue =0)
    return [a + b for a, b in pairs]

a = [1, 2]
b = [1, 2, 3, 4]
print(hash(a[1]))

"""
from random import randint


def roll():
    return randint(1,6)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, b+a



