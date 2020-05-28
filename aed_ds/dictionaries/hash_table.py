from .tad_dictionary import Dictionary
from ..exceptions import NoSuchElementException, DuplicatedKeyException, InvalidPositionException, EmptyListException
from ..lists.singly_linked_list import SinglyLinkedList
from .item import Item

import ctypes
class HashTable(Dictionary):
    def __init__(self, size = 101):
        self.num_elements = 0
        self.array_size = size
        self.table = (self.array_size * ctypes.py_object)()

        for i in range(self.array_size):
            self.table[i] = SinglyLinkedList()

    def size(self):
        return self.num_elements

    def is_full(self):
        return False

    def get(self, k):
        if self.has_key(k):
            raise NoSuchElementException   
        i = self.hash_function(k)
        colision_list = self.table[i]
        it = colision_list.iterator()
        while it.has_next():
            cur_item = it.next()
            if cur_item.get_key == k:
                return cur_item.get_valeu()
        
    def insert(self, k, v): 
        if self.has_key(k):
            raise DuplicatedKeyException
        idx = self.hash_function(k)
        item = Item(k,v)
        self.table[idx].insert.head(item)
        self.num_elements += 1 
        
    def update(self, k, v): 
        if self.has_key(k):
            raise NoSuchElementException
        
        idx = self.hash_function(k)
        colition_list = self.table[idx]
        it = colition_list.iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                return self.current_item.set_value(v)

            
    def remove(self, k):
        if self.has_key(k):
            raise NoSuchElementException
        idx = hash_function(k)
        item = Item(k,v)
        self.table[idx].remove.head(item)
        self.num_elements -= 1

        """ colition_list = self.table[idx]
        it = colition_list.iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() = k:
                item = Item(k,v) """

    def keys(self):
        if not self.num_elements != 0 :
            raise NoSuchElementException
        for idx in range (self.array_size):
             colition_list = self.table[idx]
             it = colition_list.iterator()
             while it.has_next():
                current_item = it.next()
                if current_item.get_key():
                    return self.current_item.get_keys()
        
    def values(self): 
        if not self.num_elements != 0 :
            raise NoSuchElementException
        for idx in range (self.array_size):
             colition_list = self.table[idx]
             it = colition_list.iterator()
             while it.has_next():
                current_item = it.next()
                if current_item.get_key():
                    return self.get_keys()

    def items(self): 
        if not self.num_elements != 0:
            raise NoSuchElementException
        for idx in (self.array_size):
            colition_list = self.table[idx]
            it = colition_list.iterator()
            while it.has_next:
                curent_item = it.next()
                if curent_item:
                    print(self.curent_item)

    def hash_function(self, k):
        return sum([ord(c) for c in k]) % self.array_size
    
    def has_key(self, k):
        idx = self.hash_function(k) # O(1)    
        colision_list = self.table[idx]
        it = colision_list.iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                return True
        return False