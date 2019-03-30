# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/23 10:54
# @Author  : Despicable Me
# @Email   : 
# @File    : linkedlist.py
# @Software: PyCharm
# @Explain :

from abstractlist import AbstractList
from node import Node
from linkedlistiterator import LinkedListIterator

class LinkedList(AbstractList):

    def __init__(self, sourceCollection = None):
        self._head = TwoWayNode()
        self._head.prevous = self._head.next = self._head
        AbstractList.__init__(self, sourceCollection)

    def __iter__(self):
        cursor = self._head.next
        while cursor != self._head:
            yield cursor.data
            cursor = cursor.next

    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._head = TwoWayNode()
        self._head.previous = self._head.next = self._head

    def _getNode(self, i):
        if i == len(self):
            return self._head
        if i == len(self) - 1:
            return self._head.previous
        probe = self._head.next
        while i > 0:
            probe = probe.next
            i -= 1
        return probe

    def __setitem__(self, i, item):
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        self._getNode(i).data = item

    def __getitem__(self, i):
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self._getNode(i).data

    def insert(self, i, item):
        if i < 0:
            i = 0
        elif i >= len(self):
            i = len(self)
        theNode = self._getNode(i)
        newNode = TwoWayNode(item, theNode.previous, theNode)
        theNode.previous = newNode
        theNode.previous.next = newNode
        self._size += 1
        self.incModCount()

    def pop(self, i=None):
        """Precondition: 0 <= i < len(self).
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError."""
        if i == None: i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        theNode = self._getNode(i)
        item = theNode.data
        theNode.previous.next = theNode.next
        theNode.next.previous = theNode.previous
        self._size -= 1
        self.incModCount()
        return item

    def listIterator(self):
        return LinkedListIterator(self)