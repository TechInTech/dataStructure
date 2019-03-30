# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/26 10:39
# @Author  : Despicable Me
# @Email   : 
# @File    : hashset.py
# @Software: PyCharm
# @Explain :

import node import Node
import abstractset import AbstractSet
import arrays import Array
from abstractcollection import AbstractCollection

class HashSet(AbstractCollection, AbstractSet):
    """A hashing implementation of a set."""

    DEFAULT_CAPACITY = 9

    def __init__(self, sourceCollection = None, capacity = None):
        if capacity == None:
            self._capacity = HashSet.DEFAULT_CAPACITY
        else:
            self._capacity = capacity
        self._items = Array(self._capacity)         # 集的条目
        self._foundNode = self._priorNode = None    # 引用要定位的节点，否则为None,引用定位的节点之前的节点，否则为None
        self._index = -1                            # 引用节点所在链的索引，否则置为-1
        AbstractCollection.__init__(self, sourceCollection)

    def __contains__(self, item):
        self._index = abs(hash(item)) % len(self._items)
        self._priorNode = None
        self._foundNode = self._items[self._index]
        while self._foundNode != None:
            if self._foundNode.data == item:
                return True
            else:
                self._priorNode = self._foundNode
                self._foundNode = self._foundNode.next
        return False

    def __iter__(self):
        """
        Supports iteration over a view of self.
        集合实现采用了桶/链策略，即数组+链表的结构
        """
        cursor = 0
        while cursor < len(self._items):
            node = self._items[cursor]
            while node != None:
                yield node.data
                node = node.next
            cursor += 1

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def clear(self):
        self._items = Array(self._capacity)
        self._size = 0

    def add(self, item):
        if not item in self:
            self._items[self._index] = Node(item, self._items[self._index])
            self._size += 1

    def remove(self, item):
        if not item in self:
            raise KeyError(str(item) + "not in set")
        elif self._priorNode == None:
            self._items[self._index] = self._foundNode.next
        else:
            self._priorNode.next = self._foundNode.next
        self._size -= 1

    def loadFactor(self):
        return len(self) / len(self._items)

    def rehash(self):
        if self.loadFactor() > 0.5:
            items = list(self)
            self._items = Array(len(self._items) * 2)
            self._size = 0
            for item in items:
                self.add(item)