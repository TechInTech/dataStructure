"""
File: treesortedbag.py

Project 10.6

A binary search tree-based implementation of a sorted bag.
"""

from trees.linkedbst import LinkedBST
from abstract.abstractbag import AbstractBag

class TreeSortedBag(AbstractBag):
    """A binary search tree-based implementation of a sorted bag."""

    # Uses a LinkedBST to contain the bag's items.
    # The tree is rebalanced after items are added during istantiation.
    # The iterator uses an inorder traversal to ensure visiting items
    # in ascending order.

    # Searches, insertions, and removals are logarithmic on average,
    # and linear in the worst case.

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = LinkedBST()
        AbstractBag.__init__(self, sourceCollection)
        if not self._items.isBalanced():
            self._items.rebalance()

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        return self._items.inorder()

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items.clear()

    def add(self, item):
        """Adds item to self."""
        self._items.add(item)
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        if not item in self._items:
            raise KeyError(str(item) + " not in bag")
        self._items.remove(item)
        self._size -= 1
