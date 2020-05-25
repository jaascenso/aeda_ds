from .tad_dictionary import Dictionary
from ..exceptions import NoSuchElementException, DuplicatedKeyException, InvalidPositionException, EmptyListException
from ..lists.singly_linked_list import SinglyLinkedList

import ctypes
class HashTable(Dictionary):
    def __init__(self, size = 101):
        self.key = 0
        self.value = 0
        self.num_elements = 0
        self.array_size = size
        self.table = (self.array_size * ctypes.py_object)()

        for i in range(self.array_size):
            self.table[i] = SinglyLinkedList()

        # SinglyLinkedList.__init__(self)

    def size(self):
        return self.num_elements

    def is_full(self):
        return self.num_elements == self.array_size


    def get(self, k , size): 
        if k < 0 or k > size:
            raise InvalidPositionException
        pass
        



    def insert(self, k, v): pass

    def update(self, k, v): pass

    def remove(self, k): pass

    def keys(self): pass

    def values(self): pass

    def items(self): pass

    def hash_funtion(self, k): pass