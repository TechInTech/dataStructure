#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 11:21
# @Author  : Despicable Me
# @Site    : 
# @File    : algorithms.py
# @Software: PyCharm
# @Explain :

# 排序算法
'''
File:  Algorithms.py
Algorithms configured for profiling.
'''
## *************** 选择排序 *****************
def selectionSort(lyst, profiler):
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            profiler.comparison()
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst, minIndex, i, profiler)
        i += 1

def swap(lyst, i, j, profiler):
    '''Exchange the element at position i and j.'''
    profiler.exchange()
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

## *************** 选择排序 *******************

## *************** 冒泡排序 *******************
def bubbleSort(lyst, profiler):
    n = len(lyst)
    while n > 1:
        swapped = False
        i = 1
        while i < n:
            profiler.comparison()
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i - 1, profiler)
                swapped = True
            i += 1
        if not swapped: return
        n -= 1
## *************** 冒泡排序 *******************

## *************** 插入排序 *******************
def insertionSort(lyst, profiler):
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            profiler.comparison()
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = itemToInsert
        i += 1
## *************** 插入排序 *******************

# def insertionSort(lyst):
#     i = 1
#     while i < len(lyst):
#         item = lyst[i]
#         j -= 1
#         while j >= 0:
#             if item < lyst[j]:
#                 lyst[j + 1] = lyst[j]
#                 j -= 1
#             else:
#                 break
#         lyst[j + 1] = item
#         i += 1
#
# def bubbleSort(lyst):
#     n = len(lyst)
#     while n > 1:
#         i = 1
#         while i < n:
#             if lyst[i] < lyst[i - 1]:
#                 swap(lyst, i, i - 1)
#             i += 1
#         n -= 1

