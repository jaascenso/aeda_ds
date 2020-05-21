from .tad_dictionary import Dictionary
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList

class HashTable(Dictionary):
    def __init__(self, size = 101):
        self.key = None
        self.value = None
        SinglyLinkedList.__init__(self)

    def size(self):
        return self.size

    def is_full(self):
        if self.key == None:
            raise NoSuchElementException


    def get(self, k , size): 
        if k < 0 or k > size:
            raise NoSuchElementException
        



    def insert(self, k, v): pass

    def update(self, k, v): pass

    def remove(self, k): pass

    def keys(self): pass

    def values(self): pass

    def items(self): pass

    def hash_funtion(self, k): pass