# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/18 21:53
# @Author  : Despicable Me
# @Email   : 
# @File    : arrays.py
# @Software: PyCharm
# @Explain :

class Array(object):

    def __init__(self, capacity, fillValue = None):
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return  iter(self._items)

    def __str__(self):
        return str(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, newitem):
        self._items[index] = newitem
