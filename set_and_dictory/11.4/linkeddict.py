# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/25 19:28
# @Author  : Despicable Me
# @Email   : 
# @File    : linkeddict.py
# @Software: PyCharm
# @Explain :

from abstractdict import AbstractDict, Item
from node import Node

class LinkedDict(AbstractDict):

    def __init__(self,sourceCollection = None):
        self._items = self._previousNode = None
        AbstractDict.__init__(self, sourceCollection)

    def __iter__(self):
        cursor = self._items
        while not cursor is None:
            yield cursor.data.key
            cursor = cursor.next

    def __getitem__(self, key):
        index = self._index(key)
        if index is None:
            raise KeyError("Missing" + str(key))
        return index.data.value

    def __setitem__(self, key, value):
        index = self._index(key)
        if index is None:
            self._items = Node(Item(key, value), self._items)
            self._size += 1
        else:
            index.data.value = value

    def clear(self):
        self._size = 0
        self._items = None

    def pop(self, key):
        index = self._index(key)
        if index is None:
            raise KeyError("Missing" + str(key))
        self._size -= 1
        # 考虑当index为第一节点时，当其为第一个节点时，其前一个节点为None
        # 否则，index不为第一个节点
        if index.previousNode is None:
            self._items = self._items.next
        else:
            self._previousNode.next = index.next
        return index.data.value

    def _index(self, key):
        self._previousNode = None
        index = self._items
        while not index is None:
            if index.data.key == key:
                return index
            index = index.next
            self._previousNode = index
        return None


def main(dictionaryType=dict):
    d = dictionaryType()
    for key in range(1, 6):
        d[key] = "Value" + str(key)
    print("\nLength: ", len(d))
    print("\nThe dictionary:", d)
    aClone = dictionaryType(map(lambda item: (item.key, item.value), d.items()))
    print("\nA clone:", aClone)
    print("\nThe keys:", set(d.keys()))
    print("\nThe values:", list(d.values()))
    print("\nKey Value (using [])")
    for key in d:
        print(key, " ", d[key])
    print("\nDelete all keys:")
    for key in range(1, 6):
        print(d.pop(key))
    print("\nLength: ", len(d))
    newD = dictionaryType([(7, 8), (2, 3), (8, 9)])
    print("\nA clone:", aClone)
    print("\nA second dictionary:", newD)
    print("\nA Concatenate a clone and second:", aClone + newD)


# Include your dictionary type as an argument to main
if __name__ == "__main__":
    main(LinkedDict)