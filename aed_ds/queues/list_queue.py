from .tad_queue import Queue
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import EmptyQueueExpection , FullQueueException

class ListQueue(Queue):
    def __init__(self, size = 40):
        self.list_size = size
        self.list = SinglyLinkedList

    def is_empty(self): 
        return self.is_empty()

    def is_full(self):   
        return self.num_elements == self.size

    def size(self): 
        return self.num_elements

    def enqueue(self, element):
        if self.num_elements == self.size:
            raise FullQueueException()
        self.insert_last(element)

    def dequeue(self): 
        if self.num_elements == 0:
            raise EmptyQueueExpection()
        element = self.remove_tail
        return element.get_element()