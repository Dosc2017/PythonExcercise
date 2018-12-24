
"""
import collections
from random import choice


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_value = dict(spades=3, hearts=2, clubs=2, diamonds=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value*len(suit_value) + suit_value[card.suit]


a = "a！"
b = "a！"


# print('a' * 20 is 'aaaaaaaaaaaaaaaaaaaa', 'a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa')

import numpy as np



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



def HashTag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ' '.join('%s = "%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s %s>%s</%s>' % (name, attr_str, con, name)for con in content)
    return '<%s%s/>' % (name, attr_str)




from collections import namedtuple
from operator import attrgetter


metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
    ]
LatLong = namedtuple('LatLong','lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]

name_lat = attrgetter('name', 'cc', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('cc')):
    print(name_lat(city))



from abc import ABC, abstractmethod
from collections import namedtuple


Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = float(sum(item.total() for item in self.cart))
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.__total - float(discount)

    def __repr__(self):
        fmt = '<Order total: {:.2f}  due: {:.2f}'
        return fmt.format(self.total(), self.due())


proms = []


def promotion(func):
    proms.append(func)
    return func


@promotion
def Fidelity_prom(order):
        return order.total()*0.05 if order.customer.fidelity > 1000 else 0


@promotion
def BulkItem_prom(order):
        for item in order.cart:
            if item.quantity >= 20:
                return order.total()*0.1
        return 0


@promotion
def LargeOrder_prom(order):

        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total()*0.07
        return 0


Joe = Customer('Joe', 0)
Dave = Customer('Dave', 10000)  # Dave is rich!!
cart = [LineItem('banana', 6, .5),
        LineItem('apple', 30, 1.5),
        LineItem('watermelon', 5, 5.0)]


def best_prom(order):
    return max(prom(order) for prom in proms)


print(Order(Dave, cart, best_prom))


def make_avg():
    count = 0
    total = 0


    def avg(newvalue):
        nonlocal count, total
        count += 1
        total += newvalue
        return total/count
    return avg


avg = make_avg()
print(i for i in range(10))

"""
import time
import functools


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapse = time.perf_counter() - t0
        name = func.__name__
        arg_str = ''.join(repr(arg) for arg in args)
        print('[%0.9fs] %s(%s): %s' % (elapse, name, arg_str, result))
        return result

    return clocked


@clock
@functools.lru_cache()
def fact(n):
    if n < 2:
        return n
    return fact(n - 1) + fact(n - 2)


fact(9)





