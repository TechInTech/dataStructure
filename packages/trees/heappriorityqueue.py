"""
File: heappriorityqueue.py
Project 10.11

Heap-based implementation of a priority queue
"""

from collection.abstractcollection import AbstractCollection
from trees.arrayheap import ArrayHeap

class HeapPriorityQueue(AbstractCollection):
    """A heap-based priority queue implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = ArrayHeap()
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        return iter(self._items)

    def peek(self):
        """
        Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the stack is empty."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        return self._items.peek()

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items.clear()

    def add(self, item):
        """Adds item to the rear of the queue."""
        self._items.add(item)
        self._size += 1

    def pop(self):
        """
        Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the queue is empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        self._size -= 1
        return self._items.pop()
