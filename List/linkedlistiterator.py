# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/23 14:24
# @Author  : Despicable Me
# @Email   : 
# @File    : linkedlistiterator.py
# @Software: PyCharm
# @Explain :

class LinkedListIterator(object):

    def __init__(self, backingStore):
        self._backingStore = backingStore
        self._modCount = backingStore.getModCount()
        self.first()

    def first(self):
        self._cursor = self._backingStore._head.next
        self._lastItemPos = None

    def hasNext(self):
        return self._cursor != self._backingStore._head

    def next(self):
        if not self.hasNext():
            raise ValueError("No next item in list iterator")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store")
        self._lastItemPos = self._cursor
        self._cursor = self._cursor.next
        return self._lastItemPos.data

    def last(self):
        self._cursor = self._backingStore._head
        self._lastItemPos = None

    def hasPrevious(self):
        return self._cursor.previous != self._backingStore._head

    def previous(self):
        if not self.hasPrevious():
            raise ValueError("No next item in list iterator")
        self._cursor = self._cursor.previous
        self._lastItemPos = self._cursor
        return self._lastItemPos.data

    def replace(self, item):
        if self._lastItemPos == None:
            raise AttributeError("The current position is undefined.")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("List has been modified illegally.")
        self._lastItemPos.data = item
        self._lastItemPos = None

    def insert(self, item):
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("List has been modified illegally.")
        if self._lastItemPos == None:
            self._backingStore.add(item)
        else:
            newNode = TwoWayNode(item, self._lastItemPos.previous, self._lastItemPos)
            self._lastItemPos.previous.next = newNode
            self._lastItemPos.previous = newNode
            self._backingStore._size += 1
            self._backingStore.incModCount()
            self._lastItemPos = None
        self._modCount += 1

    def remove(self):
        if self._lastItemPos is None:
            raise AttributeError("The current position is undefined.")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("List has been modified illegally.")
        item = self._lastItemPos.data
        # If the item removed was obtained via next, move cursor back
        if self._lastItemPos == self._cursor:
            self._cursor = self._cursor.next
        self._lastItemPos.previous.next = self._lastItemPos.next
        self._lastItemPos.next.previous = self._lastItemPos.previous
        self._backingStore._size -= 1
        self._backingStore.incModCount()
        self._modCount += 1
        self._lastItemPos = None