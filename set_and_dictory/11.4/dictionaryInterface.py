# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/25 16:19
# @Author  : Despicable Me
# @Email   : 
# @File    : dictionaryInterface.py
# @Software: PyCharm
# @Explain :

class DictionaryInterface(object):

    def __init__(self, sourceCollection = None):
        pass

    def __getitem__(self, key):
        return False

    def __setitem__(self, key, value):
        return None

    def pop(self, key):
        return None

    def __iter__(self):
        return None

    def keys(self):
        return None

    def values(self):
        return None

    def items(self):
        return None