"""
File: arraysortedset.py
Author: Ken Lambert
"""

from bagset.arraysortedbag import ArraySortedBag
from abstract.abstractset import AbstractSet

class ArraySortedSet(ArraySortedBag, AbstractSet):
    """An array-based set implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        ArraySortedBag.__init__(self, sourceCollection)

    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        if not item in self:
            ArraySortedBag.add(self, item)
