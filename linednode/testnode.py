# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/20 14:27
# @Author  : Despicable Me
# @Email   : 
# @File    : testnode.py
# @Software: PyCharm
# @Explain :
from singlelink import SingleLink

s = SingleLink()
t = SingleLink()
for i in range(10):
    s.add(i)
    t.append(i)
# 遍历
print("头插法遍历结果")
s.travel()
print("\n尾插法遍历结果")
t.travel()

# 搜素
print("\n不在链表内时应输出：False")
print(s.search(10))

print("在链表内时应输出：True")
print(s.search(8))

# 替换第4项3用给定的11
print("替换前的链表：")
s.travel()
s.replace(3, 11)
print("\n替换后的链表：")
s.travel()

# 插入

# 链表头插入
s.insert(0,12)
print("\n链表头插入")
s.travel()

# 链表尾插入
s.insert(11,23)
print("\n链表尾插入")
s.travel()

#任意位置插入（0 < index < len(self))
s.insert(5, 34)
print("\n任意位置插入")
s.travel()


# 迭代输出
# 验证程序的迭代方法__iter__
print("\ntesting the method：__iter__")
for item in s:
    print(item, end=" ")

# 测试remove方法

print("\n删除头部链表")
s.remove(12)
# print("\n")
s.travel()

print("\n删除尾部链表")
s.remove(23)
# print("\n")
s.travel()

print("\n删除中间的链表")
s.remove(34)
s.travel()

print("\n" + str(s))

# s.clear()

print("链表长度:",len(s))