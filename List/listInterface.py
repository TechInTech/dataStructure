# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/22 20:21
# @Author  : Despicable Me
# @Email   : 
# @File    : listInterface.py
# @Software: PyCharm
# @Explain :


class ListInterface(object):

    def __init__(self, sourceCollection = None):
        pass

    def isEmpty(self):
        return True

    def __iter__(self):
        return None

    def __str__(self):
        return ""

    def __len__(self):
        return 0

    def __add__(self, other):
        return None

    def __eq__(self, other):
        return False

    def pop(self):
        return None

    def insert(self, index, item):
        pass

    def replace(self, index, item):
        pass

    def add(self, item):
        pass

    def remove(self, index):
        pass