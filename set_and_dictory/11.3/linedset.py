# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/25 16:06
# @Author  : Despicable Me
# @Email   : 
# @File    : linedset.py
# @Software: PyCharm
# @Explain :
from linedbag import LinkedBag
from abstractaet import AbstractSet

class LinedSet(LinkedBag, AbstractSet):

    def __init__(self, sourceCollection = None):
        LinkedBag.__init__(self, sourceCollection)

    def add(self, item):
        LinkedBag.append(self, item)