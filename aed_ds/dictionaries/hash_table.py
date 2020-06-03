from .tad_dictionary import Dictionary
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList
from .item import Item
import ctypes
class HashTable(Dictionary):
    def __init__(self, size=101):
        self.num_elements = 0
        self.array_size = size
        self.table = (self.array_size * ctypes.py_object)()
        self.main_list = SinglyLinkedList()

        for i in range(self.array_size):
            self.table[i] = SinglyLinkedList()

    def size(self): 
        return self.num_elements

    def is_full(self): 
        return self.num_elements == self.array_size
        

    def get(self, k):
        idx = self.hash_fuction(k)
        colision_list = self.table[idx]
        it = colision_list.iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                return current_item.get_value()
        raise NoSuchElementException()

    def insert(self, k, v): 
        if self.has_key(k):
            raise DuplicatedKeyException()
        else:
            idx = self.hash_fuction(k)
            colision_list = self.table[idx]
            new_item = Item(k, v)
            colision_list.insert_last(new_item)
            self.num_elements += 1


    def update(self, k, v): 
        if not self.has_key(k):
            raise NoSuchElementException()
        else:   
            idx = self.hash_fuction(k)
            colision_list = self.table[idx]
            it = colision_list.iterator()
            while it.has_next():
                current_item = it.next()
                if current_item.get_key() == k:
                    current_item.set_value(v)
        

    def remove(self, k): 
        idx = self.hash_fuction(k)
        colision_list = self.table[idx]
        it = colision_list.iterator()
        #it = self.table[i]
        count = 0
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                temp_value = current_item.get_value()
                colision_list.remove(count)
                self.num_elements -= 1
                return temp_value
            count += 1
            
        raise NoSuchElementException

    def keys(self): 
        for i in range(self.size()):
            colision_list = self.table[i]
            it = colision_list.iterator()
            while it.has_next():
                current_item = it.next()
                self.main_list.insert_last(current_item.get_key())
        return self.main_list


    def values(self):
        for i in range(self.size()):
            colision_list = self.table[i]
            it = colision_list.iterator()
            while it.has_next():
                current_item = it.next()
                self.main_list.insert_last(current_item.get_value())
        return self.main_list

    def items(self): 
        for i in range(self.size()):
            colision_list = self.table[i]
            it = colision_list.iterator()
            while it.has_next():
                current_item = it.next()
                self.main_list.insert_last(current_item)
        return self.main_list
                

    def hash_fuction(self, key):
        return sum([ord(c) for c in key]) % self.array_size
    
    def has_key(self, key):
        idx = self.hash_fuction(key)
        colision_list = self.table[idx]
        it = colision_list.iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == key:
                return True
        return False

