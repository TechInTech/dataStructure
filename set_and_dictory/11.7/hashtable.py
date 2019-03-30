# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/25 20:33
# @Author  : Despicable Me
# @Email   : 
# @File    : hashtable.py
# @Software: PyCharm
# @Explain :

from arrays import Array

class HashTable(object):
    """定义hash table 类，采用数组方式表示"""

    EMPTY = None
    DELETED = True

    def __init__(self, capacity = 29, hashFunction = hash, liner = True):
        """
        :param capacity: hash table 的大小，默认大小为29，可自调节。
        :param hashFunction: 指定hash函数 Python默认为自带的hash函数。
        :param liner: 指定是否使用线性探测器策略，True表示是，False为否。(线性探测器用于解决哈希表中的冲突问题)
        """
        self._table = Array(capacity, HashTable.EMPTY)
        self._size = 0
        self._hash = hashFunction
        self._homeIndex = -1         # 主索引
        self._actualIndex = -1       # 实际索引
        self._liner = liner          # 冲突策略
        self._probeCount = 0         # 探测次数

    def insert(self, item):
        """Inserts item into the table
        Preconditions: There is at least one empty cell or
        one previously occupied cell.
        There is not a duplicate item."""
        self._probeCount = 0
        self._homeIndex = abs(self._hash(item)) % len(self._table)

        distance = 1
        index = self._homeIndex

        # Stop searching when an empty cell is encounted
        while not self._table[index] in (HashTable.EMPTY, HashTable.DELETED):

            # Incremnt the index and wrap around to first position
            # if necessary
            if self._liner:
                increment = index + 1
            else:
                # 二次探测
                increment = self._homeIndex + distance ** 2
                distance += 1
            index = increment % len(self._table)
            self._probeCount += 1

        # An empty cell is found, so store the item
        self._table[index] = item
        self._size += 1
        self._actualIndex = index

    def remove(self, item):
        """Remove the item if it exists and return its index, return -1 otherwise."""
        # self._probeCount = 0
        self._homeIndex = abs(self._hash(item)) % len(self._table)
        distance = 1
        index = self._homeIndex

        while (self._table[index] != HashTable.EMPTY or \
               self._table[index] == HashTable.DELETED) and \
                self._table[index] != item:

            if self._liner:
                increment = index + 1
            else:
                increment = self._homeIndex + distance ** 2
                distance += 1
            index = increment % len(self._table)
            self._probeCount += 1

        if self._table[index] == item:
            self._table[index] = HashTable.DELETED
            self._actualIndex = index
            self._size -= 1
            return index
        else:
            self._actualIndex = -1
            return -1

    def get(self, item):
        """Return the index if the item is present, return -1 otherwish"""
        self._probeCount = 0
        self._homeIndex = abs(self._hash(item)) % len(self._table)
        distance = 1
        index = self._homeIndex

        while (self._table[index] != HashTable.EMPTY or \
               self._table[index] == HashTable.DELETED) and \
                self._table[index] != item:

            if self._liner:
                increment = index + 1
            else:
                increment = self._homeIndex + distance ** 2
                distance += 1
            index = increment % len(self._table)
            self._probeCount += 1

        if self._table[index] == item:
            self._actualIndex = index
            return index
        else:
            self._actualIndex = -1
            return -1

    def __len__(self):
        return self._size

    def loadFactor(self):
        return float(len(self)) / len(self._table)

    def homeIndex(self):
        return self._homeIndex

    def actualIndex(self):
        return self._actualIndex

    def probeCount(self):
        return self._probeCount

    def __str__(self):
        return str(self._table)


def main():
    """Use an example data set from Chapter 19."""
    table = HashTable(8, lambda x: x)
    print("Before insert the data: ")
    print("Table: ", table)

    for item in range(10, 71, 10):
        table.insert(item)
    print("After the data inserted: ")
    print("Table: ", table)

    print("Item and positions during runs of the method get: ")
    for item in range(10, 71, 10):
        print("{%d, %d}" % (item, table.get(item)), end=",")

    print("\nItems, positons, and the table during runs of the method remove: ")
    for item in range(10, 71, 10):
        print("{%d, %d}" % (item, table.remove(item)))
        print(table)

if __name__ == "__main__":
    main()