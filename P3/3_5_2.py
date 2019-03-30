#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 9:20
# @Author  : Despicable Me
# @Site    : 
# @File    : 3_5_2.py
# @Software: PyCharm
# @Explain :

from numpy import array
import random

def mergesort(lyst):
    # lyst           the list being sorted
    # copyBuffer     temporary space needed during merge
    copyBuffer = array(len(lyst))
    mergeSortHelper(lyst, copyBuffer, 0, len(lyst) - 1)
    # return lyst

def mergeSortHelper(lyst, copyBuffer, low, high):
    # lyst           list being sorted
    # copyBuffer     temp space needed during merge
    # low, high      boundary of sublist
    # middle         midpoint of sublist
    if low < high:
        middle = (low + high) // 2
        mergeSortHelper(lyst, copyBuffer, low, middle)
        mergeSortHelper(lyst, copyBuffer, middle + 1, high)
        merge(lyst, copyBuffer, low, middle, high)

def merge(lyst, copyBuffer, low, middle, high):
    # low           beginning of first sorted sublist
    # middle        end of first sorted sublist
    # middle + 1    beginning of second sorted sublist
    # high          end of second sorted sublist

    # Initialize i1 and i2 to the firt items in each sublist
    i1 = low
    i2 = middle + 1

    # Interleave items from the sublists into the
    # copyBuffer in such a way that order is maintained.
    for i in range(low, high + 1):
        if i1 > middle:
            copyBuffer[i] = lyst[i2]      # First sublist exhausted
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = lyst[i1]      # Second sublist extraacted
            i1 += 1
        elif lyst[i1] < lyst[i2]:
            copyBuffer[i] = lyst[i1]      # Items in first sublist <
            i1 += 1
        else:
            copyBuffer[i] = lyst[i2]      # Items in second sublist <
            i2 += 1
    for i in range(low, high + 1):        # Copy sorted items back to
        lyst[i] = copyBuffer[i]           # proper position in lyst

def main():
    size = 20
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    print('Before Sorted:')
    print(lyst)
    lyst = mergesort(lyst)
    print('After Sorted:')
    print(lyst)

if __name__ == '__main__':
    main()