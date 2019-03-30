"""
File: hashset.py
Project 11.6

Adjusts the array's capacity and rehahses if the load factor > .80.
"""

from collection.node import Node
from collection.arrays import Array
from collection.abstractcollection import AbstractCollection
from abstract.abstractset import AbstractSet

class HashSet(AbstractCollection, AbstractSet):
    """Represents a hash-based set."""

    DEFAULT_CAPACITY = 9

    def __init__(self, sourceCollection = None):
        # Now tracks occupied cells for rehashing if necessary.
        self._array = Array(HashSet.DEFAULT_CAPACITY)
        self._foundNode = self._priorNode = None
        self._index = -1
        self._occupiedCells = 0
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __contains__(self, item):
        """Returns True if item is in self or False otherwise."""
        self._index = abs(hash(item)) % len(self._array)
        self._priorNode = None
        self._foundNode = self._array[self._index]
        while self._foundNode != None:
            if self._foundNode.data == item:
                return True
            else:
                self._priorNode = self._foundNode
                self._foundNode = self._foundNode.next
        return False

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        for node in self._array:
            while node != None:
                yield node.data
                node = node.next

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._array = Array(HashSet.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        if not item in self:
            if not self._array[self._index]:
                self._occupiedCells += 1
            self._array[self._index] = Node(item,
                                            self._array[self._index])
            self._size += 1
            if self.loadFactor() > 0.8:
                self._rehash()

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        if not item in self:
            raise KeyError(str(item) + " not in set")
        elif self._priorNode == None:
            self._array[self._index] = self._foundNode.next
            self._occupiedCells -= 1
        else:
            self._priorNode.next = self._foundNode.next
        self._size -= 1

    # Utility methods
    def loadFactor(self):
        return self._occupiedCells / len(self._array)

    def _rehash(self):
        items = list(self)
        self._array = Array(len(self._array) * 2)
        self._size = 0
        for item in items:
            self.add(item)
