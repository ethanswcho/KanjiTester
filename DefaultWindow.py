import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QMainWindow
from PyQt5.QtGui import QFont


class DefaultWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title  = "Kanji Tester"
        self.width = 1200
        self.height = 800
        self.x = 200
        self.y = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)


