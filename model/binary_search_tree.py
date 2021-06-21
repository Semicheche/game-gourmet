from model.node import Node

class BinarySearchTree():

    def __init__(self):
        self.root =  None


    def insert(self, parent_node, value, choice):
        self.root = self.insert_new_node(parent_node, value, choice)


    def is_empty(self):
        return not self.root


    def show_tree(self, root_node):
        if root_node:
            print (root_node.get_value())
            self.show_tree(root_node.get_right_child())
            self.show_tree(root_node.get_left_child())


    def insert_new_node(self, parent_node, value, choice):
        if not parent_node:
            parent_node = Node(value)
            return parent_node
        elif choice:
            parent_node.set_right_child(self.insert_new_node(parent_node.get_right_child(), value, choice))
        else:
            parent_node.set_left_child(self.insert_new_node(parent_node.get_left_child(), value, choice))

        return parent_node
