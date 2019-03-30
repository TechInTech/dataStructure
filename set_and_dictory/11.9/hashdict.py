# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/26 11:49
# @Author  : Despicable Me
# @Email   : 
# @File    : hashdict.py
# @Software: PyCharm
# @Explain :

from abstractdict import AbstractDict, Item
from arrays import Array
from node import Node

class HashDict(AbstractDict):
    """Represents a hash-based dictionary."""

    DEFAULT_CAPACITY = 9

    def __init__(self, sourceCollection = None):
        self._items = Array(HashDict.DEFAULT_CAPACITY)
        self._foundNode = self._priorNode = None
        self._index = -1
        AbstractDict.__init__(self, sourceCollection)

    def __contains__(self, key):
        self._index = abs(hash(key)) % len(self._items)
        self._priorNode = None
        self._foundNode = self._items[self._index]
        while self._foundNode != None:
            if self._foundNode.data.key == key:
                return True
            else:
                self._priorNode = self._foundNode
                self._foundNode = self._foundNode.next
        return False

    def __str__(self):
        return "{" + ", ".join(map(str,self)) + "}"

    def __iter__(self):
        cursor = 0
        while cursor < len(self._items):
            node = self._items[cursor]
            while node != None:
                yield node.data.key
                node = node.next
            cursor += 1

    def loadFactor(self):
        return len(self) / len(self._items)

    def __getitem__(self, key):
        if key in self:
            return self._foundNode.data.value
        else:
            raise KEyError("Missing: " + str(key))

    def __setitem__(self, key, value):
        if key in self:
            self._foundNode.data.value = value
        else:
            node = Node(Item(key, value), self._items[self._index])
            self._items[self._index] = node
            self._size += 1

    def pop(self, key):
        if not key in self:
            raise KeyError("Missing " + str(key))
        elif self._priorNode == None:
            self._items[self._index] = self._foundNode.next
        else:
            self._priorNode.next = self._foundNode.next
        self._size -= 1
        return self._foundNode.data.value