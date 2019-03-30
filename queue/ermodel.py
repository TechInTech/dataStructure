# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/22 10:50
# @Author  : Despicable Me
# @Email   : 
# @File    : ermodel.py
# @Software: PyCharm
# @Explain :


from linkedpriorityqueue import LinkedPriorityQueue

class Condition(object):
    """Represents a condition."""

    def __init__(self, rank):
        self._rank = rank

    def __eq__(self, other):
        return self._rank == other._rank

    def __lt__(self, other):
        return self._rank < other._rank

    def __le__(self, other):
        return self._rank <= other._rank

    def __str__(self):
        """Returns the string rep of a condition."""
        if   self._rank == 1: return "critical"
        elif self._rank == 2: return "serious"
        else:                 return "fair"

class Patient(object):
    """Represents a patient with a name and a condition."""

    def __init__(self, name, condition):
        self._name = name
        self._condition = condition

    def __eq__(self, other):
        return self._condition == other._condition

    def __lt__(self, other):
        return self._condition < other._condition

    def __le__(self, other):
        return self._condition <= other._condition

    def __str__(self):
        """Returns the string rep of a patient."""
        return self._name + " / " + str(self._condition)


class ERModel(LinkedPriorityQueue):

    def __init__(self, sourceCollection = None):

        LinkedPriorityQueue.__init__(self, sourceCollection)

    def schedule(self, p):
        self.add(p)

    def treatNext(self):
        if self.isEmpty():
            return None
        else:
            return self.pop()