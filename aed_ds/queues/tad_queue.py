from abc import ABC, abstractmethod
class Queue(ABC):
    # Returns true iff the queue contains no elements.
    @abstractmethod
    def isEmpty(self): pass

    # Returns true iff the queue cannot contain more elements.
    @abstractmethod
    def isFull(self): pass

    # Returns the number of elements in the queue.
    @abstractmethod
    def size(self): pass

    # Inserts the specified element at the rear of the queue.
    # Throws FullQueueException
    @abstractmethod
    def enqueue(self, element): pass

    # Removes and returns the element at the front of the queue.
    # Throws EmptyQueueException
    @abstractmethod
    def dequeue(self): pass