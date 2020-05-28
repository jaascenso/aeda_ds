from .tad_stack import Stack
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import EmptyStackExpection , FullStackException


class ListStack(Stack):
    def __init__ (self, size = 40):
        self.head = None
        self.tail = None 
        self.list_size = size
        self.num_elements = 0
    
    def isEmpty(self): 
        return self.num_elements == 0

    def isFull(self):
        return self.num_elements == list_size

    def size(self): pass

    def top(self):
        if self.num_elements == 0:
            raise EmptyStackExpection
        return self.head.get_element()

    def push(self, element): 
        if size == 40: #num_elements == 40
            raise FullStackException
        
        elif not self.head:
            self.tail = element
        element = self.head

        else:

    def pop(self): pass