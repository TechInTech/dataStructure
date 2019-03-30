# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/20 17:52
# @Author  : Despicable Me
# @Email   : 
# @File    : doublelink.py
# @Software: PyCharm
# @Explain :

class Node(object):

    def __init__(self,data, previous = None, next = None):
        self.data = data
        self.next = next
        self.previous = previous

from abstractbag import AbstractBag

class DoubleLink(AbstractBag):

    def __init__(self, sourceCollection = None):
        self._items = None
        AbstractBag.__init__(self, sourceCollection)

    def __iter__(self):
        cursor = self._items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    def add(self, item):
        "头插法"
        node = Node(item, None, None)
        self._items = node
        self._size += 1

    def append(self, item):
        node = Node(item, None, None)
        if self.isEmpty():
            self.add(item)
        else:
            cursor = self._items
            while cursor.next != None:
                cursor = cursor.next
            node.previous = cursor
            cursor.next = node
            self._size += 1

    def insert(self, index, item):

        if index <= 0:
            self.add(item)
        elif index >= len(self):
            self.append(item)
        else:
            node = Node(item, None, None)
            probe = self._items
            count = 0
            while count < (index - 1):
                probe = probe.next
                count += 1
            node.next = probe
            node.previous = probe.previous
            probe.previous = node
            probe.previous.next = node
            self._size += 1

    def clear(self):
        self._size = 0
        self._items = None

    def remove(self, item):
        if not item in self:
            raise KeyError(str(item) + "not in bag")

        probe  = self._items
        trailer = None

        while probe.next != None:
            if probe.data == item:
                if probe == self._items:
                    # rear = self._items
                    # while rear.next != self._items:
                    #     rear = rear.next
                    self._items = probe.next
                    # rear.next = self._items
                else:
                    probe.next.previous = trailer
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
                trailer.next = None
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