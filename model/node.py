
class Node():

    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


    def is_leaf(self):
        return self.left_child == None and self.right_child == None


    def get_value(self):
        return self.value


    def set_value(self, value):
        self.value = value


    def set_left_child(self, left_child):
        self.left_child = left_child


    def get_left_child(self):
        return self.left_child


    def set_right_child(self, right_child):
        self.right_child = right_child


    def get_right_child(self):
        return self.right_child


    def __str__ (self):
        return f' {self.__class__.__name__} => value: {self.value}, right_child: {self.right_child}, left_child: {self.left_child}'
