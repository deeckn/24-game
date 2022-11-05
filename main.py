import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel
from game import Game

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    sys.exit(app.exec())
