from abc import ABC, abstractmethod
class Dictionary(ABC):
    # Returns the number of elements in the dictionary.
    @abstractmethod
    def size(self): pass

    # Returns true if the dictionary is full.
    @abstractmethod
    def is_full(self): pass

    # Returns the value associated with key k.
    # Throws NoSuchElementException
    @abstractmethod
    def get(self, k): pass

    # Inserts a new value, associated with key k.
    # Throws DuplicatedKeyException
    @abstractmethod
    def insert(self, k, v): pass

    # Updates the value associated with key k.
    # Throws NoSuchElementException
    @abstractmethod
    def update(self, k, v): pass

    # Removes the key k, and the value associated with it.
    # Throws NoSuchElementException
    @abstractmethod
    def remove(self, k): pass

    # Returns a List with all the keys in the dictionary.
    @abstractmethod
    def keys(self): pass

    # Returns a List with all the values in the dictionary.
    @abstractmethod
    def values(self): pass

    # Returns a List of lists, with all the key value pairs in the dictionary.
    @abstractmethod
    def items(self): pass