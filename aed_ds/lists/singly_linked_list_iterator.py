from ..exceptions import *
from ..tad_iterator import Iterator
from aed_ds.exceptions import EmptyListException, NoSuchElementException

class SinglyLinkedListIterator(Iterator):
    def __init__(self, singly_linked_list):
        self.singly_linked_list = singly_linked_list
        self.rewind()

    # Returns true iff the iteration has more elements.
    def has_next(self):
        return self.current_node != None

    # Returns the next element in the iteration.
    # Throws NoSuchElementException
    def next(self):
        if not self.has_next():
            raise NoSuchElementException()
        element = self.current_node.get_element()
        self.current_node = self.current_node.get_next()
        return element

    # Restarts the iteration. After rewind, if the iteration is not empty, next will return the first element in the iteration.
    def rewind(self):
        self.current_node = self.singly_linked_list.head
