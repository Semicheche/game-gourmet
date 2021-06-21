from PyQt5.QtWidgets import *
from model.binary_search_tree import BinarySearchTree
from model.node import Node
from components.components import Components

class Game():

    def __init__(self):
        self.components = Components()
        self.node = None
        self.know_ledge_tree = BinarySearchTree()


    def start_game(self):
        if self.know_ledge_tree.is_empty():
            self.setup_game()

        self.guess(self.know_ledge_tree.root)


    def guess(self, node):
        self.msg_box = self.components.mount_msg_box("O prato que você pensou é " + node.get_value() + "?", "question")

        if (self.msg_box == QMessageBox.Yes):
            if node.is_leaf():
                self.win()
            else:
                self.guess(node.get_right_child())
        else:
            if node.get_right_child() == None:
                self.ask_new_information_guess(node)
            else:
                self.guess(node.get_left_child())


    def setup_game(self):
        self.know_ledge_tree.insert(None, "Massa", True)
        self.know_ledge_tree.insert_new_node(self.know_ledge_tree.root, "Macarrão", True)
        self.know_ledge_tree.insert_new_node(self.know_ledge_tree.root, "Bolo de chocolate", False)


    def win(self):
        self.components.mount_msg_box("Acertei de novo!")


    def ask_new_information_guess(self, node):
        new_plate = self.components.mount_dialog("Qual prato você pensou?")
        hint = self.components.mount_dialog( new_plate + " é ________ mas " + node.get_value() + " não.")

        self.add_node_hint_value(node, hint, new_plate)


    def add_node_hint_value(self, node, hint, value):
        wrong_guess_value = node.get_value()

        node.set_value(hint)
        node.set_left_child(Node(wrong_guess_value))
        node.set_right_child(Node(value))
