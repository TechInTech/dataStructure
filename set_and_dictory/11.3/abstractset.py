# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/25 15:37
# @Author  : Despicable Me
# @Email   : 
# @File    : abstractset.py
# @Software: PyCharm
# @Explain :

class AbstractSet(object):
    """Generic set method implementation."""

    def __or__(self, other):
        """并集"""
        return self + other

    def __and__(self, other):
        """交集"""
        intersection = type(self)()
        for item in self:
            if item in other:
                intersection.add(item):
        return intersection

    def __sub__(self, other):
        """差集"""
        difference = type(self)()
        for item in self:
            if not item in other:
                difference.add(item)
        return difference

    def issubset(self, other):
        """子集"""
        for item in self:
            if not item in other:
                return False
        return True