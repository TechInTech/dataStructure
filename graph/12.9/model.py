# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/28 10:05
# @Author  : Despicable Me
# @Email   : 
# @File    : model.py
# @Software: PyCharm
# @Explain :

from graph import graph

class GraphDemoModel(object):

    def __init__(self):
        self._graph = None
        self._startLabel = None

    def createGraph(self, rep, startLabel):
        self._graph = graph.LinkedDirectedGraph()
        self._startLable = startLabel
        edgeList = rep.split()
        for edge in edgeList:
            if not ">" in edge:
                # 边中不含有字符">"，说明只有未连接的顶点，则此时edge表示为顶点
                if not self._graph.containsVertex(edge):
                    self._graph.addVertex(edge)
                else:
                    self._graph = None
                    return "Duplicate vertex."
            else:
                # 若edge表示边
                bracketPos = edge.find(">")
                colonPos = edge.find(":")
                if bracketPos == -1 or colonPos == -1 or bracketPos > colonPos:
                    self._graph = None
                    return "Problem with > or :"
                else:
                    formVertex = edge[:bracketPos]
                    toVertex = edge[bracketPos + 1:colonPos]
                    weight = edge[colonPos + 1:]
                    if weight.isdigit():
                        weight = int(weight)
                    if not self._graph.containsVertex(formVertex):
                        self._graph.addVertex(formVertex)
                    if not self._graph.containsVertex(toVertex):
                        self._graph.addVertex(toVertex)
                    if not self._graph.containsEdge(formVertex, toVertex):
                        self._graph.addEdge(formVertex, toVertex, weight)
                    else:
                        self._graph = None
                        return "Duplicate edge."
        vertex = self._graph.getVertex(startLabel)
        if vertex is None:
            self._graph = None
            return "Duplicate edge."
        else:
            vertex.setMark()
            return "Graph created successfully."

    def getGraph(self):
        if not self._graph:
            return None
        else:
            return str(self._graph)

    def run(self, algorithm):
        if self._graph is None:
            return None
        else:
            return algorithm(self._graph, self._startLabel)