# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/19 10:26
# @Author  : Despicable Me
# @Email   : 
# @File    : abstractstack.py
# @Software: PyCharm
# @Explain :

from abstractcollection import AbstractCollection

class AbstractStack(AbstractCollection):

    def __init__(self, sourceCollection = None):
        AbstractCollection.__init__(self, sourceCollection)


    def add(self, item):
        self.push(item)