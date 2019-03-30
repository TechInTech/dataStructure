# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/23 12:02
# @Author  : Despicable Me
# @Email   : 
# @File    : arraylist.py
# @Software: PyCharm
# @Explain :

from arrays import Array
from abstractlist import AbstractList
from arraysortedlist import ArraySortedList
from arraylistiterator import ArrayListIterator

class ArrayList(ArraySortedList):

    def __init__(self, sourceCollection = None):
        ArraySortedList.__init__(self, sourceCollection)

    def index(self, item):
        return ArraySortedList.index(self, item)

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
        self._incModCount()

    def add(self, item):
        AbstractList.add(self, item)

    def listIterator(self):
        return ArrayListIterator(self)