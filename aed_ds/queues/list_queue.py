from .tad_queue import Queue
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import EmptyQueueException , FullQueueException

class ListQueue(Queue):
    def __init__(self, size = 40):
        self.list_size = size
        self.list = SinglyLinkedList

    def is_empty(self): 
        return self.list.is_empty()

    def is_full(self):   
        return self.size == self.list_size

    def size(self): 
        return self.list.size()

    def enqueue(self, element):
        if self.is_full():
            raise FullQueueException()
        self.list.insert_last(element)

    def dequeue(self): 
        if self.is_empty():
            raise EmptyQueueException()
        pos = self.list.remove.first().get_element()
        return pos