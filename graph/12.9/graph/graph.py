# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/27 16:51
# @Author  : Despicable Me
# @Email   : 
# @File    : graph.py
# @Software: PyCharm
# @Explain :
from abstractcollection import abstractcollection as ab

# class LinkedDirectedGraph(ab.AbstractCollection):
#
#     def __init__(self, sourceCollection = None):
#         """Adding a vertex with the given lable to the graph."""
#         """类的实现保存了一个字典，其键为标签，其值和顶点对应"""
#         self._edgeCount = 0               # 用于记录边的数量
#         self._vertices = dict()
#         ab.AbstractCollection.__init__(self, sourceCollection)
#
#     def clear(self):
#         self._edgeCount = 0
#         self._vertices = dict()
#         self._size = 0
#
#     def clearEdgeMarks(self):
#         for edge in self.edges():
#             edge.clearMark()
#
#     def clearVertexMarks(self):
#         for vertex in self.vertices():
#             vertex.clearMark()
#
#     def sizeEdges(self):
#         return self._edgeCount
#
#     def sizeVertices(self):
#         return len(self)
#
#     def __str__(self):
#         result = str(self.sizeVertices()) + " vertices: "
#         for vertex in self.vertices():
#             result += " " + str(vertex)
#         result += "\n"
#         result += str(self.sizeEdges()) + " Edges: "
#         for edge in self.edges():
#             result += " " + str(edge)
#         return result
#
#     # iterators
#     def __iter__(self):
#         return self.vertices()
#
#     def edges(self):
#         edgesList = list()
#         for vertex in self.vertices():
#             edgesList += list(vertex.incidentEdges())
#         return iter(edgesList)
#
#     def vertices(self):
#         return iter(self._vertices.values())
#
#     def incidentEdges(self, label):
#          return self.getVertex(label).incidentEdges()
#
#     def neighboringVertices(self, label):
#         return self.getVertex(label).neighboringVertices()
#
#     def add(self, label):
#         self.addVertex(label)
#
#     # Methods relates to Vertices.
#     def addVertex(self, label):
#         """adding a vertex"""
#         self._vertices[label] = LinkedVertex(label)
#         self._size += 1
#
#     def containsVertex(self, label):
#         return label in self._vertices
#
#     # def getVertex(self, label):
#     #     """Precondition: a vertex with label must already be in the graph.
#     #             Raises: AttibuteError if a vertex with label is not already in the graph."""
#     #     if not self.containsVertex(label):
#     #         raise AttributeError("Label " + str(label) + " not in graph.""")
#     #     return self._vertices[label]
#
#     def getVertex(self, label):
#         """Precondition: a vertex with label must already be in the graph.
#         Raises: AttibuteError if a vertex with label is not already in the graph."""
#         if not self.containsVertex(label):
#             raise AttributeError("Label " + str(label) + " not in graph.""")
#         return self._vertices[label]
#
#     def removeVertex(self, label):
#         """Remove a vertex."""
#         removedVertex = self._vertices.pop(label, None)
#         if removedVertex == None:
#             return False
#         # examine all other vertices to remove edges directed at the removed vertex.
#         for vertex in self.vertices():
#             if vertex.removeEdgeTo(removedVertex):
#                 self._edgeCount -= 1
#
#         # Examine all edges from the removed vertex to other
#         for edge in removedVertex.incidentEdges():
#             self._edgeCount -= 1
#         self._size -= 1
#         return True
#
#     # Methods related to edges
#
#     def addEdge(self, formLabel, toLabel, weight):
#         formVertex = self.getVertex(formLabel)
#         toVertex = self.getVertex(toLabel)
#         if self.getEdge(formLabel, toLabel):
#             raise AttributeError("An edge already connects " + \
#                                  str(fromLabel) + " and " + \
#                                  str(toLabel))
#         formVertex.addEdgeTo(toVertex, weight)
#         self._edgeCount += 1
#
#     def containsEdge(self, formLabel, toLabel):
#         return self.getEdge(formLabel, toLabel) != None
#
#     def getEdge(self, formLabel, toLable):
#         formVertex = self.getVertex(formLabel)
#         toVertex = self.getVertex(toLable)
#         return formVertex.getEdgeTo(toVertex)
#
#     def removeEdge(self, formLabel, toLabel):
#         formVertex = self.getVertex(formLabel)
#         toVertex = self.getVertex(toLabel)
#         removedEdge = formVertex.removeEdggeTo(toVertex)
#         if removedEdge:
#             self._edgeCount -= 1
#         else:
#             return removedEdge


class LinkedDirectedGraph(ab.AbstractCollection):

    # A graph has a count of vertices, a count of edges,
    # and a dictionary of label/vertex pairs.

    def __init__(self, sourceCollection=None):
        self._edgeCount = 0
        self._vertices = {}
        ab.AbstractCollection.__init__(self, sourceCollection)

    # Methods for clearing, marks, sizes, string rep

    def clear(self):
        """Clears the graph."""
        self._size = 0
        self._edgeCount = 0
        self._vertices = {}

    def clearEdgeMarks(self):
        """Clears all the edge marks."""
        for edge in self.edges():
            edge.clearMark()

    def clearVertexMarks(self):
        """Clears all the vertex marks."""
        for vertex in self.vertices():
            vertex.clearMark()

    def sizeEdges(self):
        """Returns the number of edges."""
        return self._edgeCount

    def sizeVertices(self):
        """Returns the number of vertices."""
        return len(self)

    def __str__(self):
        """Returns the string representation of the graph."""
        result = str(len(self)) + " Vertices: "
        for vertex in self._vertices:
            result += " " + str(vertex)
        result += "\n";
        result += str(self.sizeEdges()) + " Edges: "
        for edge in self.edges():
            result += " " + str(edge)
        return result

    def add(self, label):
        """For compatibility with other collections."""
        self.addVertex(label)

    # Vertex related methods

    def addVertex(self, label):
        """Precondition: a vertex with label must not
        already be in the graph.
        Raises: AttibuteError if a vertex with label
        is already in the graph."""
        if self.containsVertex(label):
            raise AttributeError("Label " + str(label) + " already in graph.""")
        self._vertices[label] = LinkedVertex(label)
        self._size += 1

    def containsVertex(self, label):
        return label in self._vertices

    def getVertex(self, label):
        """Precondition: a vertex with label must already be in the graph.
        Raises: AttibuteError if a vertex with label is not already in the graph."""
        if not self.containsVertex(label):
            raise AttributeError("Label " + str(label) + " not in graph.""")
        return self._vertices[label]

    def removeVertex(self, label):
        """Returns True if the vertex was removed, or False otherwise."""
        removedVertex = self._vertices.pop(label, None)
        if removedVertex is None:
            return False

        # Examine all other vertices to remove edges
        # directed at the removed vertex
        for vertex in self.vertices():
            if vertex.removeEdgeTo(removedVertex):
                self._edgeCount -= 1

        # Examine all edges from the removed vertex to others
        for edge in removedVertex.incidentEdges():
            self._edgeCount -= 1
        self._size -= 1
        return True

    # Methods related to edges

    def addEdge(self, fromLabel, toLabel, weight):
        """Connects the vertices with an edge with the given weight.
        Preconditions: vertices with fromLabel and toLabel must
        already be in the graph.
        The vertices must not already be connected by an edge.
        Raises: AttibuteError if the vertices
        are not already in the graph or they are already connected."""
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        if self.getEdge(fromLabel, toLabel):
            raise AttributeError("An edge already connects " + \
                                 str(fromLabel) + " and " + \
                                 str(toLabel))
        fromVertex.addEdgeTo(toVertex, weight)
        self._edgeCount += 1

    def containsEdge(self, fromLabel, toLabel):
        """Returns True if an edge connects the vertices,
        or False otherwise."""
        return self.getEdge(fromLabel, toLabel) != None

    def getEdge(self, fromLabel, toLabel):
        """Returns the edge connecting the two vertices, or None if
        no edge exists.
        Precondition: vertices with fromLabel and toLabel must
        already be in the graph.
        Raises: AttibuteError if the vertices
        are not already in the graph."""
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        return fromVertex.getEdgeTo(toVertex)

    def removeEdge(self, fromLabel, toLabel):
        """Returns True if the edge was removed, or False otherwise.
        Precondition: vertices with fromLabel and toLabel must
        already be in the graph.
        Raises: AttibuteError if the vertices
        are not already in the graph."""
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        edgeRemovedFlg = fromVertex.removeEdgeTo(toVertex)
        if edgeRemovedFlg:
            self._edgeCount -= 1
        return edgeRemovedFlg

    # Iterators

    def __iter__(self):
        """Supports iteration over a view of self (the vertices)."""
        return self.vertices()

    def edges(self):
        """Supports iteration over the edges in the graph."""
        result = list()
        for vertex in self.vertices():
            result += list(vertex.incidentEdges())
        return iter(result)

    def vertices(self):
        """Supports iteration over the vertices in the graph."""
        return iter(self._vertices.values())

    def incidentEdges(self, label):
        """Supports iteration over the incident edges of the
        given verrtex.
        Precondition: a vertex with label must already be in the graph.
        Raises: AttibuteError if a vertex with label is not already in the graph."""
        return self.getVertex(label).incidentEdges()

    def neighboringVertices(self, label):
        """Supports iteration over the neighboring vertices of the
        given verrtex.
        Precondition: a vertex with label must already be in the graph.
        Raises: AttibuteError if a vertex with label is not already in the graph."""
        return self.getVertex(label).neighboringVertices()

    # Make a table of vertex labels and indicies for a matrix
    def makeLabelTable(self):
        """Returns a table (dictionary) associating vetrex labels with
        index positions."""
        labels = list(map(lambda vertex: vertex.getLabel(),
                          self))
        labels.sort()
        table = dict()
        index = 0
        for label in labels:
            table[label] = index
            index += 1
        return table

class LinkedEdge(object):

    def __init__(self, formVertex, toVertex, weight = None):
        self._vertex1 = formVertex
        self._vertex2 = toVertex
        self._weight = weight
        self._mark = False

    def clearMark(self):
        self._mark = False

    def setMark(self):
        self._mark = True

    def isMarked(self):
        return self._mark == True

    def getWeight(self):
        return self._weight

    def setWeight(self, weight):
        self._weight = weight

    def getOtherVertex(self, vertex):
        if self._vertex2 == vertex or None == vertex:
            return self._vertex1
        else:
            return self._vertex2

    def getToVertex(self):
        return self._vertex2

    def __str__(self):
        return str(self._vertex1) + ">" + str(self._vertex2) + ":" \
               + str(self._weight)

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self._vertex1 == other._vertex1 and self._vertex2 == \
               other._vertex2 and self._weight == other._weight


class LinkedVertex(object):

    def __init__(self, label):
        self._label = label
        self._edgeList = list()
        self._mark = False

    def clearMark(self):
        self._mark = False

    def setMark(self):
        self._mark = True

    def isMarked(self):
        return self._mark

    def getLabel(self):
        return self._label

    def setLabel(self, label, g):
        """g is a vertex."""
        g._vertices.pop(self._label, None)
        g._vertices[label] = self
        self._label = label

    def addEdgeTo(self, toVertex, weight):
        edge = LinkedEdge(self, toVertex, weight)
        self._edgeList.append(edge)

    def incidentEdges(self):
        return iter(self._edgeList)

    def neighboringVertices(self):
        vertices = list()
        for edge in self._edgeList:
            vertices.append(edge.getOtherVertex(self))
        return iter(vertices)

    def __str__(self):
        """Returns the string representation of the vertex."""
        return str(self._label)

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self.getLabel() == other.getLabel()

    def removeEdgeTo(self, toVertex):
        edge = LinkedEdge(self, toVertex)
        if edge in self._edgeList:
            self._edgeList.remove(edge)
            return True
        else:
            return False

    def getEdgeTo(self, toVertex):
        edge = LinkedEdge(self, toVertex)
        try:
            return self._edgeList[self._edgeList.index(edge)]
        except:
            return None