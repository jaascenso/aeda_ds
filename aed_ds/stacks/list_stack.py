from .tad_stack import Stack
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import EmptyStackException , FullStackException


class ListStack(Stack):
    def __init__ (self, size = 40): 
        self.list_size = size
        self.list = SinglyLinkedList()

    def is_empty(self): 
        return self.list.is_empty()

    def is_full(self):
        return self.size() == self.list_size
    
    def size(self):
        return self.list.size()

    def top(self):
        if self.is_empty():
            raise EmptyStackException()
        return self.list.get_first()

    def push(self, element): 
        if self.is_full():
            raise FullStackException
        self.list.insert_first(element)

    def pop(self): 
        if self.is_empty():
            raise EmptyStackException
        element = self.list.remove_first()
        return element