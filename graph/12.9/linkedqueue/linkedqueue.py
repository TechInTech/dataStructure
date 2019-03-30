# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/21 11:18
# @Author  : Despicable Me
# @Email   : 
# @File    : linkedqueue.py
# @Software: PyCharm
# @Explain :

from abstractcollection import abstractcollection as ab

class AbstractQueue(ab.AbstractCollection):

    def __init__(self, sourceCollection = None):
        ab.AbstractCollection.__init__(self, sourceCollection)

class Node(object):

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedQueue(AbstractQueue):

    def __init__(self, sourceCollection = None):
        self._front = None
        self._rear = None
        AbstractQueue.__init__(self, sourceCollection)

    def __iter__(self):
        cursor = self._front
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    def __contains__(self, item):
        if self.isEmpty():
            raise KeyError("queue is empty.")
        cursor = self._front
        while not cursor is None:
            if cursor.data == item:
                return True
            else:
                cursor = cursor.next
        return False

    def clear(self):
        self._size = 0
        self._front = None
        self._rear = None

    def pop(self):
        if self.isEmpty():
            raise KeyError("queue is empty.")
        oldItem = self._front.data
        if self._front.next == None:
            self._front = None
            self._rear = None
        else:
            self._front = self._front.next
        self._size -= 1
        return oldItem

    def peek(self):
        if self.isEmpty():
            raise KeyError("queue is empty.")
        return self._front.data

    def add(self, item):
        node = Node(item, None)
        if self.isEmpty():
            self._front = node
        else:
            self._rear.next = node
        self._rear = node
        self._size += 1