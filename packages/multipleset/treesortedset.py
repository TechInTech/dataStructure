"""
File: treesortedset.py
Project 11.8

A tree-based sorted set implementation.
"""

from bagset.treesortedbag import TreeSortedBag
from abstract.abstractset import AbstractSet

class TreeSortedSet(TreeSortedBag, AbstractSet):
    """An tree-based sorted set implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        TreeSortedBag.__init__(self, sourceCollection)

    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        if not item in self:
            TreeSortedBag.add(self, item)
