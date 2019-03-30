# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/19 11:05
# @Author  : Despicable Me
# @Email   : 
# @File    : node.py
# @Software: PyCharm
# @Explain :

class Node(object):

    def __init__(self, data, next = None):
        self.data = data
        self.next = next