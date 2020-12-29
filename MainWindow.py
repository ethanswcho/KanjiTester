import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QStackedWidget
from PyQt5.QtGui import QFont

from DefaultWindow import DefaultWindow
from LearnWindowPre1 import LearnWindowPre1

class MainWindow(DefaultWindow):

    def __init__(self):
        super().__init__()

        self.windows = QStackedWidget()

        self.label_title = QLabel(self.title, self)
        self.label_title.setFont(QFont('Arial', 100))
        self.label_title.move(100, 100)

        self.button_learn = QPushButton("Learn", self)
        self.button_test = QPushButton("Test", self)
        self.button_about = QPushButton("About", self)

        self.button_learn.setFont(QFont("Arial", 20))
        self.button_test.setFont(QFont("Arial", 20))
        self.button_about.setFont(QFont("Arial", 20))

        self.button_learn.setGeometry(300, 350, 600, 100)
        self.button_test.setGeometry(300, 500, 600, 100)
        self.button_about.setGeometry(300, 650, 600, 100)

        self.button_learn.clicked.connect(self.clicked_learn)
    
    #def initUI(self):

    def clicked_learn(self):
        self.LWP1 = LearnWindowPre1()
        self.LWP1.initUI(self)
        self.LWP1.show()
        self.close()

