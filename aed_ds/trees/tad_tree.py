from abc import ABC, abstractmethod


class Tree(ABC):
    # Returns the root of the tree
    @abstractmethod
    def get_root(self): pass

    # Returns the number of elements in the tree
    @abstractmethod
    def size(self): pass

    # Returns the height of the tree
    @abstractmethod
    def height(self): pass

    # Returns True if the tree is empty
    @abstractmethod
    def is_empty(self): pass

    # Returns True if the tree is full
    @abstractmethod
    def is_full(self): pass