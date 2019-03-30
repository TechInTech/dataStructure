# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/19 21:45
# @Author  : Despicable Me
# @Email   : 
# @File    : linkedbag.py
# @Software: PyCharm
# @Explain :

from node import Node
from abstractbag import AbstractBag

class LinkedBag(AbstractBag):

    def __init__(self,sourceCollection = None):
        self._items = None
        AbstractBag.__init__(self, sourceCollection)

    def __iter__(self):
        cursor = self._items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    def add(self, item):
        "头插法"
        self._items = Node(item, self._items)
        self._size += 1

    def append(self, item):
        "尾插法"
        node = Node(item, None)
        if self.isEmpty():
            self._items = node
        else:
            cursor = self._items
            while cursor.next != None:
                cursor = cursor.next
            cursor.next = node
        self._size +=1

    def clear(self):
        self._size = 0
        self._items =None

    def remove(self, item):
        if not item in self:
            raise KeyError(str(item) + "not in bag")
        probe  = self._items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next
        if probe == self._items:
            self._items = probe.next
        else:
            trailer.next = probe.next
        self._size -= 1