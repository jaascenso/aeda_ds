class BinaryTreeNode:
    def __init__(self, element=None, left_child=None, right_child=None):
        self.element = element
        self.left_child = left_child
        self.right_child = right_child
    
    def get_element(self):
        return self.element

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_element(self, element):
        self.element = element

    def set_left_child(self, left_child):
        self.left_child = left_child

    def set_right_child(self, right_child):
        self.right_child = right_child

    def is_leaf(self):
        return self.left_child is None and self.right_child is None

class BinarySearchTreeNode(BinaryTreeNode):
    def __init__(self, key=None, element=None, left_child=None, right_child=None):
        BinaryTreeNode.__init__(self, element, left_child, right_child)
        self.key = key
    
    def get_key(self):
        return self.key
