# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/25 8:06
# @Author  : Despicable Me
# @Email   : 
# @File    : expressiontree.py
# @Software: PyCharm
# @Explain :

from bstnode import BSTNode

class LeafNode(object):

    def __init__(self, data):
        self._data = data

    def value(self):
        return self._data

    def __str__(self):
        return str(self._data)

    def postfix(self):
        return str(self)

    def infix(self):
        return str(self)

    def prefix(self):
        return str(self)

class InteriorNode(object):
    """Represents the operator and its two operands."""

    def __init__(self, op, leftOper, rightOper):
        self._operator = op
        self._leftOperand = leftOper
        self._rightOperand = rightOper

    def value(self):
        leftValue = self._leftOperand.value()
        rightValue = self._rightOperand.value()
        if self._operator == "+":
            return leftValue + rightValue
        elif self._operator == "-":
            return leftValue - rightValue
        elif self._operator == "*":
            return leftValue * rightValue
        elif self._operator == "/":
            return self._leftOperand  / self._rightOperand
        else:
            return 0

    def postfix(self):
        return self._leftOperand.postfix() + " " + \
            self._rightOperand.postfix() + " " + \
            self._operator

    def infix(self):
        return "(" + self._leftOperand.infix() + " " + \
            self._operator + " " + \
            self._rightOperand.infix() + ")"

    def prefix(self):
        return self._operator + " " + \
            self._leftOperand.prefix() + " " + \
            self._rightOperand.prefix()