# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/25 17:37
# @Author  : Despicable Me
# @Email   : 
# @File    : arraydict.py
# @Software: PyCharm
# @Explain :

from abstractdict import AbstractDict, Item

class ArrayDict(AbstractDict):
    """基于数组的字典实现"""

    def __init__(self, sourceCollection = None):
        self._items = list()
        AbstractDict.__init__(self, sourceCollection)

    def __iter__(self):
        """返回的迭代器为字典的key"""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor].key
            cursor += 1

    def __getitem__(self, key):
        index = self._index(key)
        if index == -1:
            raise keyError("Missing" + str(key))
        return self._items[index].value

    def __setitem__(self, key, value):
        index = self._index(key)
        if index == -1:
            self._items.append(Item(key, value))
            self._size += 1
        else:
            self._items[index].value = value

    def clear(self):
        self._size -= 1
        self._items = list()

    def pop(self, key):
        index = self._index(key)
        if index == -1:
            raise KeyError("Missing" + str(key))
        self._size -= 1
        return self._items.pop(index).value

    def _index(self, key):
        index = 0
        for entry in self._items:
            if entry.key == key:
                return index
            index += 1
        # key不在数组中
        return -1

def main(dictionaryType = dict):
    d = dictionaryType()
    for key in range(1, 6):
        d[key] = "Value" + str(key)
    print("\nLength: ", len(d))
    print("\nThe dictionary: ", d)

    aClone = dictionaryType(map(lambda item: (item.key, item.value), d.items()))
    print("\nA clone: ", aClone)
    print("\nThe keys: ", set(d.keys()))
    print("\nThe values: ", list(d.values()))
    print("\nKeys Values (using [])")

    for key in d:
        print(key, " ", d[key])
    print("\nDelete all keys: ")
    for key in range(1, 6):
        print(d.pop(key))
    print("\nLength: ", len(d))

    newD = dictionaryType([(7, 8), (2, 3), (8, 9)])
    print("\nA clone: ", aClone)
    print("\nA second dictionary: ", newD)
    print("\nA Concatenate a clone and second: ", aClone + newD)

if __name__ == "__main__":
    main(ArrayDict)