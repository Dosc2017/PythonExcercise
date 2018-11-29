import time
import math
from collections import Counter
import pandas as pd
import xlrd
import numpy as np
import glob


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
# print(lookup['2'][0])


def useless(n):
    for i in range(n):
        if i > 3:
            return
        print(i)


def Root(n):
    """

    :param n: int
    :return: int

    exapmle: func(12345) = 1 + 2 + 3 + 4 + 5 = 1 + 5 = 6
    """
    return (n-1) % 9 + 1


def readwork(filepath, n):
   data = pd.read_excel(filepath, n)
   return data












import openpyxl as op


data = op.load_workbook('20181112-2018-11-12_history-现状输出.xlsx', data_only=True)
target_sheet = data.get_sheet_by_name('取整算法')
b4 = target_sheet['AZ55']
print(f'({b4.column}, {b4.row}) is {b4.value}')


