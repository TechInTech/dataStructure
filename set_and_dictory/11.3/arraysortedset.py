# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/25 16:15
# @Author  : Despicable Me
# @Email   : 
# @File    : arraysortedset.py
# @Software: PyCharm
# @Explain :

import arraysortedset import ArraySortedSet
import abstractset import AbstractSet

class AbstractSortedSet(ArraySortedSet, AbstractSet):

    def __init__(self, sourceCollection = None):
        ArraySortedSet.__init__(self, sourceCollection)

    def add(self, item):
        ArraySortedSet.add(self, item)