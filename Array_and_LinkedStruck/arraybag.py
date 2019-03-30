# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/18 22:31
# @Author  : Despicable Me
# @Email   : 
# @File    : arraybag.py
# @Software: PyCharm
# @Explain :

from arrays import Array
from abstractbag import AbstractBag

class Arraybag(AbstractBag):

    # class variable
    DEFAULT_CAPACITY = 10

    def __int__(self, sourceCollection = None):
        self._items = Array(Arraybag.DEFAULT_CAPACITY)
        AbstractBag.__init__(self, sourceCollection)

    def clear(self):
        self._size = 0
        self._items = Array(Arraybag.DEFAULT_CAPACITY)

    def add(self, item):
        self._items[len(self)] = item
        self._size += 1

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yeild self._items[cursor]
            cursor += 1

    def remove(self, item):
        if not item in self:
            raise KeyError(str(item) + " is not in bag ")
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        for i in range(targetIndex, len(self) - 1):
            self._items[i] = self._items[i + 1]
        self._size -= 1