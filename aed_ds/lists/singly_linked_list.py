from .tad_list import List
from .nodes import SingleListNode
from .singly_linked_list_iterator import SinglyLinkedListIterator
from ..exceptions import EmptyListException, InvalidPositionException, NoSuchElementException


class SinglyLinkedList(List):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def is_empty(self):
        return self.num_elements == 0

    def size(self):
        return self.num_elements

    def get_first(self): 
        if not self.head:
            raise EmptyListException
        return self.head.get_element()

    def get_last(self): 
        if not self.head:
            raise EmptyListException
        return self.tail.get_element()

    def get(self, position): 
        if not self.head:
            raise EmptyListException()
        cur_node = self.head
        idx = 0
        while cur_node:
            if idx == position:
                return cur_node.get_element()
            cur_node = cur_node.get_next()
            idx += 1

    def find(self, element): 
        cur_node = self.head
        idx = 0
        while cur_node:
            if element == cur_node.get_element():
                return idx
            cur_node = cur_node.get_next()
            idx += 1
        return -1            

    def insert_first(self, element):
        new_node = SingleListNode(element, self.head)
        if not self.head:
            self.tail = new_node
        self.head = new_node
        self.num_elements += 1
    
    def insert_last(self, element):
        new_node = SingleListNode(element, None)
        if not self.head: 
            self.head = new_node
        else:    
            self.tail.set_next(new_node)
        self.tail = new_node
        self.num_elements += 1

    def insert(self, element, position): 
        if position < 0 or position > self.size():
            raise InvalidPositionException()
        elif position == 0:
            return self.insert_first(element)
        elif position == self.size():
            return self.insert_last(element)
        prev_node = self.head
        cur_node = self.head
        idx = 0
        while prev_node:
            if position == idx: 
                new_node = SingleListNode(element, cur_node)
                prev_node.set_next(new_node)
                self.num_elements += 1
                break
            prev_node = cur_node
            cur_node = cur_node.get_next()
            idx += 1 

    def remove_first(self):
        if not self.head:
            raise EmptyListException()
        elif self.head == self.tail:
            result = self.head.get_element()
            self.make_empty()
            return result
        else:
            old_head = self.head
            self.head = self.head.get_next()
            self.num_elements -= 1
            return old_head.get_element()

    def remove_last(self): 
        if not self.head:
            raise EmptyListException()
        elif self.size() == 1:
            return self.remove_first()
        cur_node = self.head
        while cur_node.get_next().get_next() is not None:
            cur_node = cur_node.get_next()
        old_node = self.tail
        self.tail = cur_node
        cur_node.set_next(None)
        self.num_elements -= 1
        return old_node.get_element()

    def remove(self, position): 
        if position < 0 or position > self.size() - 1:
            raise InvalidPositionException()
        elif position == 0:
            return self.remove_first()
        elif position == self.size() - 1:
            return self.remove_last()
        cur_node = self.head
        idx = 0
        while cur_node:
            if idx == position:
                prev_node.set_next(cur_node.get_next())
                old_node = cur_node
                cur_node.set_next(None)
                self.num_elements -= 1
                return old_node.get_element()
            prev_node = cur_node
            cur_node = cur_node.get_next()
            idx += 1

    def make_empty(self):
        self.head = None
        self.tail = None
        self.num_elements = 0    

    def iterator(self):
        return SinglyLinkedListIterator(self)

