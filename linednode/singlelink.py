# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/19 20:46
# @Author  : Despicable Me
# @Email   : 
# @File    : single_linkednode.py
# @Software: PyCharm
# @Explain :

from node import Node
from linkedbag import LinkedBag

class SingleLink(LinkedBag):

    def __init__(self, sourceCollection = None):
        LinkedBag.__init__(self, sourceCollection)

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

    def replace(self, item, newItem):
        if self.isEmpty():
            raise KeyError("linked structure is empty")
        probe = self._items
        while probe != None:
            if probe.data == item:
                probe.data = newItem
                return True
            probe = probe.next
        return False

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