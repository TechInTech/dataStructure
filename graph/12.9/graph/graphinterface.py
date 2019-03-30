# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/28 8:28
# @Author  : Despicable Me
# @Email   : 
# @File    : graphinterface.py
# @Software: PyCharm
# @Explain :
 class GraphInterface(object):

     def __init__(self):
         self._edgeCount = 0
         self._vertices = {}
         AbstractCollection.__init__(self, souceCollection)

     def __str__(self):
         return None

     def __iter__(self):
         return None

     def __len__(self):
         return 0

     def clearEdgeMarks(self):
         pass

     def clearVertexMarks(self):
         pass

     def clear(self):
         pass

     def isEmpty(self):
         return False

     def sizeEdges(self):
         return 0

     def sizeVertices(self):
         return 0

     def add(self, label):
         pass

     # 迭代器

     def edges(self, label):
         return None

     def vertices(self, label):
         return None

     def incedentEdges(self, label):
         return None

     def neiboringVertices(self, label):
         return None

     # 与边有关的方法

     def removeEdge(self, formLabel, toLabel):
         return True

     def getEdges(self, fromLabel, toLabel):
         return None

     def addEdge(self, toLabel, weight = None):
         pass

     def containsEdge(self, formLabel, toLabel):
         return False

     # 有顶点有关的方法

     def removeVerter(self, label):
         pass

     def getVertiex(self, label):
         return None

     def addVertex(self, label):
         pass

     def containsVertex(self, label):
         return False