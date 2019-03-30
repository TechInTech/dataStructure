# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/24 16:57
# @Author  : Despicable Me
# @Email   : 
# @File    : arrayhead.py
# @Software: PyCharm
# @Explain :

from abstractcollection import AbstractCollection
# from arrays import Array

class ArrayHeap(AbstractCollection):
    """数组实现堆"""

    # DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection = None):
        # self._heap = Array(ArrayHeap.DEFAULT_CAPACITY)
        self._heap = list()   # 这里将列表看作为一个数组
        AbstractCollection.__init__(self, sourceCollection)

    def add(self, item):
        self._size += 1
        self._heap.append(item)
        curPos = len(self._heap) - 1
        while curPos > 0:
            parent = (curPos - 1) // 2
            parentItem = self._heap[parent]
            if parentItem <= item:
                break
            else:
                self._heap[curPos] = self._heap[parent]
                self._heap[parent] = item
                curPos = parent

    def pop(self):
        """删除树的根节点，并返回"""
        if self.isEmpty():
            raise Exception, "Heap is empty."
        self._size -= 1
        topItem = self._heap[0]
        bottomItem = self._heap.pop(len(self._heap) - 1)
        if len(self._heap) == 0:
            return botomItem

        self._heap[0] = bottomItem
        lastIndex = len(self._heap) - 1
        curPos = 0
        while True:
            leftChild = 2 * curPos + 1
            rightChild = 2 * curPos + 2
            if leftChild > lastIndex:
                break
            if rightChild > lastIndex:
                maxChild = leftChild
            else:
                leftItem = self._heap[leftChild]
                rightItem = self._heap[rightChild]
                if leftItem < rightItem:
                    maxChild = leftChild
                else:
                    maxChild = rightChild
            maxItem = self._heap[maxChild]
            if bottomItem <= maxItem:
                break
            else:
                self._heap[curPos] = self._heap[maxChild]
                self._heap[maxChild] = bottomItem
                curPos = maxChild
        return topItem

    def peek(self):
        if self.isEmpty():
            raise Exception("The heap i sempty.")
        return self._heap[0]