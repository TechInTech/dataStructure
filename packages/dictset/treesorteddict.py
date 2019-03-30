"""
File: treesorteddict.py
Project 11.9

Completes the tree-based sorted dictionary.
"""

from abstract.abstractdict import AbstractDict, Item
from trees.linkedbst import LinkedBST

class TreeSortedDict(AbstractDict):
    """Represents a tree-based sorted dictionary."""

    # Uses composition, where the dictionary contains a tree object.
    # The tree contains items, each of which contains a key and a value.
    # Each dictionary method calls the corrseponding method on the tree.

    def __init__(self, sourceCollection = None):
        """Will copy items to the collection from sourceDictionary
        if it's present."""
        self._items = LinkedBST()
        AbstractDict.__init__(self, sourceCollection)

    # Accessors
    def __contains__(self, key):
        """Returns True if key is in self or False otherwise."""
        item = Item(key, None)
        return item in self._items

    def __iter__(self):
        """Serves up the keys in the dictionary."""
        return iter(map(lambda item: item.key, self._items.inorder()))

    def __getitem__(self, key):
        """Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Returns the value associated with the key."""
        if not key in self: raise KeyError("Missing: " + str(key))
        item = Item(key, None)
        return self._items.find(item).value

    # Mutators
    def __setitem__(self, key, value):
        """If the key is in the dictionary,
        replaces the old value with the new value.
        Othwerise, adds the key and value to it."""
        item = Item(key, value)
        if key in self:
            self._items.replace(item, item)
        else:
            self._items.add(item)
            self._size += 1

    def pop(self, key):
        """Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Removes the key and returns the associated value if the
        key in in the dictionary."""
        if not key in self:
            raise KeyError("Missing: " + str(key))
        item = self._items.remove(Item(key, None))
        self._size -= 1
        return item.value
