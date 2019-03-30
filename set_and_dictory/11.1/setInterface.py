# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/25 15:29
# @Author  : Despicable Me
# @Email   : 
# @File    : setInterface.py
# @Software: PyCharm
# @Explain :
class SetInterface(object):

    def __init__(self):
        pass

    def __len__(self):
        return 0

    def __str__(self):
        return None

    def isEmpty(self):
        return True

    def add(self, item):
        pass

    def remove(self, item):
        pass

    def __contains__(self, item):
        return False

    def __and__(self, other):
        return False

    def __or__(self, other):
        return False

    def __sub__(self, other):
        return False

    def isSubset(self, other):
        return False