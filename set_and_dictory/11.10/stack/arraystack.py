# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/19 10:34
# @Author  : Despicable Me
# @Email   : 
# @File    : arraystack.py
# @Software: PyCharm
# @Explain :

from arrays import Array
from abstractstack import AbstractStack


class ArrayStack(AbstractStack):

    DEFAULT_CAPACITY = 11

    def __init__(self, sourceCollection = None):
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, sourceCollection)

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def peek(self):
        if self.isEmpty():
            raise KeyError("the stack is empty")
        return self._items[len(self) - 1]

    def clear(self):
        self._size = 0
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)

    def push(self, item):
        self._items[len(self)] = item
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError("the stack is empty")
        oldItem = self._items[len(self) - 1]
        self._size -= 1
        return oldItem
