from .tad_tree import Tree
from ..dictionaries.tad_ordered_dictionary import OrderedDictionary
from ..exceptions import DuplicatedKeyException, NoSuchElementException, EmptyDictionaryException
from .nodes.binary_nodes import BinarySearchTreeNode


class BinarySearchTree(OrderedDictionary, Tree):
    def __init__(self, size = 101):
        self.num_elements = 0
        

    # Returns the number of elements in the dictionary.
    def size(self):
        return self.num_elements

    # Returns true if the dictionary is full.
    def is_full(self): pass
        
    # Returns the value associated with key k.
    # Throws NoSuchElementException
    def get(self, k):
        return self.get_element(self.root , k)
        
    def get_element(self, root, k):
        if root is None:
            raise NoSuchElementException()
        else:
            if root.get_key() == k:
                return root.get_element()
            elif root.get_key() > k:
                return self.get_element(root.get_left_child(), k)
            else:
                return self.get_element(root.get_right_child(), k)


    
    # Inserts a new value, associated with key k.
    # Throws DuplicatedKeyException
    def insert(self, k, v):
        if self.root is None:
            self.root = BinarySearchTreeNode(k,v)
        else:
            node = self.root
            while True:
                if node.get_key() == k:
                    raise DuplicatedKeyException()
                elif node.get_key() > k:
                    if node.get_left_child() is None:
                        node.set_left_child(BinarySearchTreeNode(k,v))
                        break
                    else:
                        node = node.get_left_child()
                else:
                    if node.get_right_child() is None:
                        node.set_right_child(BinarySearchTreeNode(k,v))
                        break
                    else:
                        node = node.get_right_child()

    def insert_element(self, root, k, v): pass

    # Updates the value associated with key k.
    # Throws NoSuchElementException
    def update(self, k, v): pass

    # Removes the key k, and the value associated with it.
    # Throws NoSuchElementException
    def remove(self, k): pass

    def remove_right_minimum(self,root):
        node = root.get_right_child()
        if node is not None and node.get_left_child() is None:
            root.set_right_child(node.get_right_child())
        else:    
            while node.get_left_child() is not None:
                parent = node
                node = node.get_left_child()
                parent.set_left_child(node.get_right_child())
            return node


    # Returns a List with all the keys in the dictionary.
    def keys(self): pass

    # Returns a List with all the values in the dictionary.
    def values(self): pass

    # Returns a List with all the key value pairs in the dictionary.
    def items(self): pass

    # Returns an iterator of the elements in the dictionary
    def iterator(self): pass

    # Returns the element with the smallest key
    # Throws EmptyTreeException
    def get_min_element(self):
        if self.is_empty():
            raise EmptyDictionaryException()
        return self.get_min_node(self.root).get_element()

    # Returns the element with the largest key
    # Throws EmptyTreeException
    def get_max_element(self): pass

    # Returns the root of the tree
    # Throws EmptyTreeException
    def get_root(self): pass

    # Returns the height of the tree
    # Throws EmptyTreeException
    def height(self): pass

    # Returns True if the tree is empty
    def is_empty(self):
        return False
