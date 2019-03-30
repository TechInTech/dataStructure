# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/21 11:04
# @Author  : Despicable Me
# @Email   : 
# @File    : arrayqueue.py
# @Software: PyCharm
# @Explain :

from arrays import Array
from abstractqueue import AbstractQueue

class ArrayQueue1(AbstractQueue):

    """移动队尾rear"""
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection = None):
        self._items = Array(ArrayQueue1.DEFAULT_CAPACITY)
        AbstractQueue.__init__(self, sourceCollection)
        self._front = 0
        self._rear = max(len(self) - 1, 0)

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def clear(self):
        self._size = 0
        self._items = Array(ArrayQueue1.DEFAULT_CAPACITY)

    def pop(self):
        if self.isEmpty():
            raise KeyError(" queue is empty.")
        cursor = 0
        oldItem = self._items[cursor]
        for i range(0, len(self) - 1):
            self._items[i] = self._items[i + 1]
        self._size -= 1
        return oldItem

    def peek(self):
        if self.isEmpty():
            raise KeyError("queue is empty.")
        return self._items[self._front]

    def __contains__(self, item):
        if self.isEmpty():
            raise KeyError("queue is empty.")
        for i in range(len(self)):
            if self._items[i] == item:
                return True
        return False

    def add(self, item):
        if self.isEmpty():
            self._items[0] = item
            self._size += 1
        elif (self._rear + 1) < ArrayQueue1.DEFAULT_CAPACITY:
            self._items[self._rear] = item
            self._rear += 1
            self._size += 1
        else:
            raise KeyError("the queue is full.")

class ArrayQueue2(AbstractQueue):

    """移动队头front"""
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection = None):
        self._items = Array(ArrayQueue2.DEFAULT_CAPACITY)
        AbstractQueue.__init__(self, sourceCollection)
        self._front = 0
        self._rear = max(len(self) - 1, 0)

    def __iter__(self):
        cursor = self._front
        while cursor <= self._rear:
            yield self._items[cursor]
            cursor += 1

    def clear(self):
        self._size = 0
        self._items = Array(ArrayQueue2.DEFAULT_CAPACITY)

    def pop(self):
        if self.isEmpty():
            raise KeyError(" queue is empty.")
        oldItem = self._items[self._front]
        if self._front < self._rear:
            self._front += 1
        elif self._front == self._rear:
            self._front = 0
            self._rear = 0
        self._size -= 1
        return oldItem

    def peek(self):
        if self.isEmpty():
            raise KeyError("queue is empty.")
        return self._items[self._front]

    def __contains__(self, item):
        if self.isEmpty():
            raise KeyError("queue is empty.")
        for i in range(self._front, self._rear + 1):
            if self._items[i] == item:
                return True
        return False

    def add(self, item):
        if self.isEmpty():
            self._items[self._front] = item
            self._size += 1
        elif (self._rear + 1) < ArrayQueue2.DEFAULT_CAPACITY:
            self._items[self._rear] = item
            self._rear += 1
            self._size += 1
            if self._front > 0 and self._rear == (ArrayQueue2.DEFAULT_CAPACITY - 1):
                for i in range(self._front, self._rear + 1):
                    self._items[i - 1] = self._items[i]
                self._front -= 1
                self._rear -= 1
        else:
            raise KeyError("the queue is full.")


class ArrayQueue3(AbstractQueue):

    """循环队列"""
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        self._items = Array(ArrayQueue3.DEFAULT_CAPACITY)
        AbstractQueue.__init__(self, sourceCollection)
        self._front = 0
        self._rear = max(len(self) - 1, 0)

    def __iter__(self):
        if self._front <= self._rear:
            cursor = self._front
            while cursor <= self._rear:
                yield self._items[cursor]
                cursor += 1
        else:
            cursor = self._front
            while cursor <= len(self) - 1:
                yield self._items[cursor]
                cursor += 1
            cursor = 0
            while cursor <= self._rear:
                yield self._items[cursor]
                cursor += 1

    def clear(self):
        self._size = 0
        self._items = Array(ArrayQueue3.DEFAULT_CAPACITY)

    def pop(self):
        if self.isEmpty():
            raise KeyError(" queue is empty.")
        oldItem = self._items[self._front]
        if self._front == (len(self) -1):
            self._front = 0
        else:
            self._front += 1
        self._size -= 1
        return oldItem

    def peek(self):
        if self.isEmpty():
            raise KeyError("queue is empty.")
        return self._items[self._front]

    def __contains__(self, item):
        if self.isEmpty():
            raise KeyError("queue is empty.")

        elif self._front <= self._rear:
            for i in range(self._front, self._rear + 1):
                if self._items[i] == item:
                    return True
            return False
        else:
            for i in range(0, self._rear + 1):
                if self._items[i] == item:
                    return True
            for i in range(self._front, len(self)):
                if self._items[i] == item:
                    return True
            return False


    def add(self, item):
        if self.isEmpty():
            self._items[self._rear] = item
            self._size += 1
        elif len(self) == ArrayQueue3.DEFAULT_CAPACITY:
            raise KeyError("the queue is full.")
        elif self._rear == len(self) - 1:
            self._items[0] = item
            self._rear += 1
            self._size += 1
        else:
            self._rear += 1
            self._items[self._rear] = item
            self._size += 1