from PyQt5.QtWidgets import *

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
