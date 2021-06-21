import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox, QInputDialog, QWidget

class Components(QWidget):

    def mount_button(self, name, width, height, pos_x=None, pos_y=None):
        button = QPushButton(name, self)
        button.resize(width, height)
        button.move(pos_x, pos_y)
        return button


    def mount_label(self, value, width, height):
        label = QLabel(value, self)
        label.resize(200, 50)
        label.move(width, height)
        label.show()


    def load_window(self, left, top, width, height, title):
        self.setGeometry(left, top, width, height)
        self.setWindowTitle(title)
        self.show()


    def mount_msg_box(self, text, type="about"):
        if type == "question":
            return QMessageBox.question(self, "Game Gourmet", text, QMessageBox.Yes | QMessageBox.No)
        else:
            return QMessageBox.about(self, "Game Gourmet", text)


    def mount_dialog(self, text):
        new_plate, ok = QInputDialog.getText(self, "Game Gourmet", text)

        if ok:
            return new_plate


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


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.components = Components()
        self.height = 200
        self.width = 300
        self.top = 500
        self.left = 800
        self.title = "Gourmet Game"
        self.game = Game()

        self.components.mount_label("Pense em um prato que gosta", self.width/5, self.height/6)
        self.button = self.components.mount_button("OK", 150, 50, self.width/4, self.height/3)
        self.button.clicked.connect(self.game.start_game)
        self.components.load_window(self.left, self.top, self.width, self.height, self.title)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
