# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/20 16:08
# @Author  : Despicable Me
# @Email   : 
# @File    : recursive_link.py
# @Software: PyCharm
# @Explain :

from node import Node
from abstractbag import AbstractBag

class Recursive_Link(AbstractBag):

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
        self._items = Node(item, None)
        self._items.next = self._items
        self._size += 1

    def append(self, item):
        node = Node(item, None)
        if self.isEmpty():
            self.add(item)
        else:
            cursor = self._items
            while cursor.next != self._items:
                cursor = cursor.next
            node.next = self._items
            cursor.next = node
            self._size += 1

    def insert(self, index, item):

        if index <= 0:
            self.add(item)
        elif index >= len(self):
            self.append(item)
        else:
            node = Node(item, None)
            probe = self._items
            count = 0
            while count < (index - 1):
                probe = probe.next
                count += 1
            node.next = probe.next
            probe.next = node
            self._size += 1

    def clear(self):
        self._size = 0
        self._items = None

    def remove(self, item):
        if not item in self:
            raise KeyError(str(item) + "not in bag")

        probe  = self._items
        trailer = None

        while probe.next != self._items:
            if probe.data == item:
                if probe == self._items:
                    rear = self._items
                    while rear.next != self._items:
                        rear = rear.next
                    self._items = probe.next
                    rear.next = self._items
                else:
                    trailer.next = probe.next
                self._size -= 1
                return

            else:
                trailer = probe
                probe = probe.next
        if probe.data == item:
            if probe == self._items:
                self._items = None
            else:
                trailer.next = self._items
        self._size -= 1


    def travel(self):
        if self.isEmpty():
            raise KeyError("linked structure is empty.")

        probe = self._items
        while probe != None:
            print(probe.data, end=" ")
            probe = probe.next

    def search(self, item):
        if self.isEmpty():
            raise KeyError("linked structure is empty")
        probe = self._items
        while probe != None:
            if probe.data == item:
                return True
            probe = probe.next
        return False

    def replace(self, item, neItem):
        if self.isEmpty():
            raise KeyError("linked structure is empty")
        probe = self._items
        while probe != None:
            if probe.data == item:
                probe.data = newItem
                return True
            probe = probe.next
        return False