import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from model.game import Game
from components.components import Components

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
