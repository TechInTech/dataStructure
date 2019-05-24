# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/20 19:09
# @Author  : Despicable Me
# @Email   :
# @File    : queue.py
# @Software: PyCharm
# @Explain :

from abstractcollection import AbstractCollection

class AbstractQueue(AbstractCollection):

    def __init__(self, sourceCollection = None):
        AbstractCollection.__init__(self, sourceCollection)
