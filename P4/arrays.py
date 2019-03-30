#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 16:25
# @Author  : Despicable Me
# @Site    : 
# @File    : arrays.py
# @Software: PyCharm
# @Explain :
'''
File: arrays.py

An Array is like a list, but the client can use
only [], str, len, iter.

To instantiate, use

<variable> = Array(<capacity>, <optional fill value>)

The fill value is None by default.
'''

class Array(object):
    '''Represent an array.'''

    def __init__(self, capacity, fillValue = None):
        '''Capacity is the static size of the array.
        fillValue is placed at each position.'''
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        '''-> The capacity of the array.'''
        return len(self._items)

    def __str__(self):
        '''-> The string representation of the array'''
        return str(self._items)

    def __iter__(self):
        '''Supports traversal with a for loop'''
        return iter(self._items)

    def __getitem__(self, index):
        '''Subscript operation for access at index'''
        return self._items[index]

    def __setitem__(self, index, NewItem):
        '''Subscript operator for replacement at index.'''
        self._items[index] = NewItem