# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/25 15:59
# @Author  : Despicable Me
# @Email   : 
# @File    : arrayset.py
# @Software: PyCharm
# @Explain :

import arraybag import ArrayBag
import abstractset import AbstractSet

class ArraySet(ArrayBag, AbstractSet):

    def __init__(self, sourceCollection = None):
        ArrayBag.__init__(self, sourceCollection)

    def add(self, item):
        if not item in self:
            ArrayBag.add(self, item)