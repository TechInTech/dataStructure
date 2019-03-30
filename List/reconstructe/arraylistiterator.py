# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/23 11:26
# @Author  : Despicable Me
# @Email   : 
# @File    : arraylistiterator.py
# @Software: PyCharm
# @Explain :

class ArrayListIterator(object):

    def __init__(self, backingStore):
        """
        :param backingStore: 在其上打开迭代器的列表
        """
        self._backingStore = backingStore
        self._modCount = backingStore.getModCount()
        self.first()

    def first(self):
        self._cursor = 0
        self._lastItemPos = -1

    def hasNext(self):
        return self._cursor < len(self._backingStore)

    def next(self):
        if not self.hasNext():
            raise ValueError("No next item in list iterator.")
        if self._modCount != bacingStore.getModCount():
            raise AttributeError("Illegal modification of backing store.")
        self._lastItemPos = self._cursor
        self._cursor += 1
        return self._backingStore[self._lastItemPos]

    def last(self):
        self._cursor = len(self._backingStore)
        self._lastItemPos = -1

    def hasPrevious(self):
        return self._cursor > 0

    def previous(self):
        if not self.hasPrevious():
            raise ValueError("No previous item in list iterator.")
        if self._modCount != bacingStore.getModCount():
            raise AttributeError("Illegal modification of backing store.")
        self._cursor -= 1
        self._lastItemPos = self._cursor
        return self._backingStore[self._lastItemPos]

    def replace(self, i, item):
        if self._lastItemPos == -1:
            raise AttributeError("The current position is not defined")
        if self._modCount != self._backingStore.getCount():
            raise AttributeError("List has been modified illegally.")
        self._backingStore[self._lastItemPos] = item
        self._lastItemPos = -1

    def insert(self, item):
        if self._modCount != self._backingStore.getCount():
            raise AttributeError("List has been modified illegally.")
        if self._lastItemPos == -1:
            self._backingStore.add(item)
        else:
            self._backingStore.insert(self._lastItemPos, item)
        self._lastItemPos = -1
        self._modCount += 1

    def remove(self):
        if self._lastItemPos == -1:
            raise AttributeError("The current position is not defined")
        if self._modCount != self._backingStore.getCount():
            raise AttributeError("List has been modified illegally.")
        item = self._backingStore[self._lastItemPos]
        if self._lastItemPos < self._cursor:
            self._cursor -= 1
        self._modCount += 1
        self._lastItemPos = -1