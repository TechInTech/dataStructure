#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 21:06
# @Author  : Despicable Me
# @Site    : 
# @File    : 3_5_1.py
# @Software: PyCharm
# @Explain :

 # 快速排序实现

import random

def quicksort(lyst):
     quicksortHelper(lyst, 0, len(lyst) - 1)

def quicksortHelper(lyst, left, right):
     if left < right:
         pivotLocation = partition(lyst, left, right)
         quicksortHelper(lyst, left, pivotLocation - 1)
         quicksortHelper(lyst, pivotLocation + 1, right)

def partition(lyst, left, right):
    ''' Find the pivot and exchange it with the last item'''
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # set the boundary point to first position
    boundary = left
    # move items less than piovt to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary +=1
    # Exchange the pivot item and the boundary item
    swap(lyst, right, boundary)
    return boundary

def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

def main(size = 20, sort = quicksort):
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    print('Before sort:',lyst)
    sort(lyst)
    print('After sort:',lyst)

if __name__ == '__main__':
    main()