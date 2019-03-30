# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/26 17:24
# @Author  : Despicable Me
# @Email   : 
# @File    : treesorteddict.py
# @Software: PyCharm
# @Explain :

from abstractdict import AbstractDict, Item
from linkedbst import LinkedBST

class TreeSortedDict(AbstractDict):

    # Uses composition, where the dictionary contains a tree object.
    # The tree contains items, each of which contains a key and a value.
    # Each dictionary method calls the corrseponding method on the tree.


    def __init__(self, sourceCollection = None):
        self._items = LinkedBST()
        AbstractDict.__init__(self, sourceCollection)

    def __contains__(self, key):
        item = Item(key, None)
        return item in self._items

    def add(self, item):
        if not item in self:
            self._items.add(item)
            self._size += 1

    def __getitem__(self, key):
        if not key in self:
            raise KeyError("Missing" + str(key))
        item = Item(key, None)
        return self._items.find(item).value

    def __setitem__(self, key, value):
        item = Item(key, value)
        if key in self:
            self._items.replace(item, item)
        else:
            self._items.add(item)
            self._size += 1

    def __iter__(self):
        return iter(map(labmda item: item.key, self._items.inorder()))

    def pop(self, key):
        if not key in self:
            raise KeyError("Missing " + str(key))
        item = self._items.remove(Item(key, None))
        self._size -= 1
        return item.value