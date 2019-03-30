# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/19 9:06
# @Author  : Despicable Me
# @Email   : 
# @File    : abstractbag.py
# @Software: PyCharm
# @Explain :

from abstractcollection import AbstractCollection

class AbstractBag(AbstractCollection):

    def __int__(self, sourceCollection = None):
        AbstractCollection.__init__(self, sourceCollection)