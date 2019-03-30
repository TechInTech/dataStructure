# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/27 22:15
# @Author  : Despicable Me
# @Email   : 
# @File    : testdirected.py
# @Software: PyCharm
# @Explain :

from graph import graph

# create a directed graph using an adjacency list
g = graph.LinkedDirectedGraph()

# adding Vertices labeled A,B,C to the graph and print it

g.addVertex("A")
g.addVertex("B")
g.addVertex("C")

print("Except verteices ABC no edges: ", str(g))

# Insert edges with weight 2.5 and print the graph

g.addEdge("A", "B", 2.5)
g.addEdge("B", "C", 2.5)
g.addEdge("C", "B", 2.5)

print("Except same vertices and edges AB BC CB all with weight 2.5:" + "\n", str(g))

# Mark all the vertices
for vertex in g.vertices():
    vertex.setMark()

# print the vertices adjacent to vertex B
print("Except vertices adjacent to B, namely C: ")
v = g.getVertex("B")
for neighbor in g.neighboringVertices(v.getLabel()):
    print(neighbor)

# print the edges of vertex B

print("Except edges incident to B, namely C: ")
for edge in g.incidentEdges(v.getLabel()):
    print(edge)