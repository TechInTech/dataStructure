# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/23 10:31
# @Author  : Despicable Me
# @Email   : 
# @File    : arraylist.py
# @Software: PyCharm
# @Explain :

import arrays import Array
import abstractlist import AbstractList
import arraylistiterator import ArrayIterator

class ArrayList(AbstractList):

    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection = None):
        self._items = Array(ArrayList.DEFAULT_CAPACITY)
        AbstractList.__init__(self, sourceCollection)

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def clear(self):
        self._size = 0
        self._items = Array(ArrayList.DEFAULT_CAPACITY)

    def __getitem__(self, i):
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self._items[i]

    def __setitem__(self, i, item):
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        self._items[i] = item

    def insert(self, i, item):
        if i < 0:
            i = 0
        elif i >= len(self):
            i = len(self)
        if i < len(self):
            for j in range(len(self), i, -1):
                self._items[j] = self._items[j - 1]
        self._items[i] = item
        self.__size += 1
        self.incModCount()

    def pop(self, i = None):
        if i == None:
            i = len(self) - 1

        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        item = self._items[i]
        for j in range(i, len(self) - 1):
            self._items[j] = self._items[j + 1]
        self._size -= 1
        self.incModCount()
        return item

    def listIterator(self):
        return ArrayListIterator(self)
