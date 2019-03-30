# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/24 11:26
# @Author  : Despicable Me
# @Email   : 
# @File    : linkedbst.py
# @Software: PyCharm
# @Explain :

from bstnode import BSTNode
from abstractcollection import AbstractCollection
from stack.linkedstack import LinkedStack
from list.linkedlist import LinkedList
from queue.linkedqueue import LinkedQueue
from math import log

class LinkedBST(AbstractCollection):

    def __init__(self, sourceCollection = None):
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)

    def __contains__(self, item):
        return self.find(item) != None

    def find(self, item):
        """搜素二叉搜索树"""
        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)
        return recurse(self._root)

    def inorder(self):
        """中序遍历"""
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)
        recurse(self._root)
        return iter(lyst)

    def postorder(self):
        """后序遍历"""
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                recurse(node.right)
                lyst.append(node.data)
        recurse(self._root)
        return iter(lyst)

    def levelorder(self):
        """层级遍历"""
        def recurse(queue):
            if not queue.isEmpty():
                node = queue.pop()
                BSTlist.add(node.data)
                if node.left != None:
                    queue.add(node.left)
                if node.right != None:
                    queue.add(node.right)
                recurse(queue)
        BSTlist = LinkedList()
        BSTqueue = LinkedQueue()
        if not self.isEmpty():
            BSTqueue.add(self._root)
            recurse(BSTqueue)
        return iter(BSTlist)

    def preorder(self):
        """前序遍历(效率不高：线性运行时间和线性的内存使用)"""
        lyst = list()
        def recurse(node):
            if node != None:
                lyst.append(node.data)
                recurse(node.left)
                recurse(node.right)
        recurse(self._root)
        return iter(lyst)

    # def __iter__(self):
    #     """前序遍历"""
    #     BSTstack = LinkedStack()
    #     node = self._root
    #     if node != None:
    #         BSTstack.push(node)
    #         while not BSTstack.isEmpty:
    #             newnode = BSTstack.pop()
    #             yield newnode.data
    #             if newnode.right != None:
    #                 BSTstack.push(newnode.right)
    #             if newnode.left != none:
    #                 BSTstack.push(newnode.left)

    def __iter__(self):
        """前序遍历(推荐此方法)"""

        if not self.isEmpty():
            BSTstack = LinkedStack()
            node = self._root
            BSTstack.push(node)
            while not BSTstack.isEmpty():
                newnode = BSTstack.pop()
                yield newnode.data
                if newnode.right != None:
                    BSTstack.push(newnode.right)
                if newnode.left != None:
                    BSTstack.push(newnode.left)

    def __str__(self):
        """返回将树结构逆时针旋转90度之后的树结构"""
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s
        return recurse(self._root, 0)

    def add(self, item):
        """在二叉搜索树中插入一项"""
        def recurse(node):
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)

        # If tree is empty, so new item goes at the root
        if self.isEmpty():
            self._root = BSTNode(item)
        else:
            recurse(self._root)
        self._size += 1

    def remove(self, item):
        pass


    def replace(self, item, newitem):
        """
        If item is in self, replaces it with newItem and
        returns True, or returns False."""
        node = self._root
        while node != None:
            if node.data == item:
                node.data = newitem
                retun True
            elif node.data > item:
                node = node.right
            else:
                node = node.left
        return False

    def clear(self):
        self._size = 0
        self._root = None

    def height(self):
        """Returns the height of the tree (the length of the longest path
        from the root to a leaf node).
        When len(t) < 2, t.height() == 0."""
        def recurse(node):
            if node == None:
                return 0
            else:
                return 1 + max(recurse(node.left), recurse(node.right))
        h = recurse(self._root)
        if not sef.isEmpty():
            h -= 1
        return h

    def isBalance(self):
        return self.height() < 2 * log(len(self) + 1, 2) - 1

    def rebalance(self):
        def rebuild(data, first, last):
            if first <= last:
                mid = (first + last) // 2
                self.add(data[mid])
                rebuild(data, first, mid - 1)
                rebuild(data, mid + 1, last)
        if not self.isBalance():
            data = list(self.inorder())
            print(data)
            self.clear()
            rebuild(data, 0, len(data) - 1)