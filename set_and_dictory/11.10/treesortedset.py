# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/26 16:41
# @Author  : Despicable Me
# @Email   : 
# @File    : treesortedset.py
# @Software: PyCharm
# @Explain :

from linkedbst import LinkedBST
from abstractcollection import AbstractCollection
from abstractset import AbstractSet

class TreeSortedSet(AbstractCollection, AbstractSet):
    "A tree-based implementation of a sorted set."

    def __init__(self, sourceCollection = None):
        self._items = LinkedBST()
        AbstractCollection.__init__(self, sourceCollection)

    def __contains__(self, item):
        return item in self._items

    def add(self, item):
        if not item in self:
            self._items.add(item)
            self._size += 1

    def __iter__(self):
        return self._items.inorder()

    def remove(self, item):
        if not item in self:
            raise KeyError(str(item) + "not in set.")
        self._items.remove(item)
        self._size -= 1

    def clear(self):
        self._items = LinkedBST()
        self._size = 0