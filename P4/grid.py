#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 22:19
# @Author  : Despicable Me
# @Site    : 
# @File    : grid.py
# @Software: PyCharm
# @Explain :

'''
Author: Ken Lambert
'''

from arrays import Array

class Grid(object):
    '''Represents a two-dimensional array'''

    def __init__(self, rows, columns, fillValue = None):
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns, fillValue)

    def getHight(self):
        '''Returns the number of rows.'''
        return len(self._data)

    def getWidth(self):
        '''Return the number of columns'''
        return len(self._data[0])

    def __getitem__(self, index):
        '''Supports two-dimensional indexing
        with [row][columns].'''
        return self._data[index]

    def __str__(self):
        '''Return a string representation of the grid'''
        result = ''
        for row in range(self.getHight()):
            for col in range(self.getWidth()):
                result += str(self._data[row][col]) + ' '
            result += '\n'
        return result