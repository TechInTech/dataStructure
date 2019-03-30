# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/19 15:55
# @Author  : Despicable Me
# @Email   : 
# @File    : teststack.py
# @Software: PyCharm
# @Explain :

from arraystack import ArrayStack
from linkedstack import LinkedStack

def test(stackType):
    s = stackType()
    print("length:", len(s))
    print("Empty:", s.isEmpty())
    print("push 1 - 10")
    for i in range(10):
        s.push(i + 1)
    print("peeking:", s.peek())
    print("Items (bottom to top:",  s)
    print("Length:", len(s))
    print("Empty:", s.isEmpty())
    clone = stackType(s)
    print("Items in clone(bottom to top):", clone)
    clone.clear()
    print("the length of clone after clear:", len(clone))
    print("Push 11")
    s.push(11)
    print("length:",len(s))
    print("popping items (top to bottom):", end=" ")
    while not s.isEmpty():
        print(s.pop(), end=" ")
    print("\nlength:", len(s))
    print("Empty:", s.isEmpty())

test(ArrayStack)

# test(LinkedStack)