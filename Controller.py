import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QListWidget
from PyQt5.QtGui import QFont

from DefaultWindow import DefaultWindow
from LearnWindowPre1 import LearnWindowPre1
from MainWindow import MainWindow
from LearnWindowPre1 import LearnWindowPre1

class Controller(QWidget):

    def __init__(self):
        super().__init__()
        self.Stack = QStackedWidget(self)
        self.MW = MainWindow()
        self.LWP1 = LearnWindowPre1()

        self.Stack.addWidget(self.MW)
        self.Stack.addWidget(self.LWP1)

        """
        self.WidgetList = QListWidget()
        self.WidgetList.insertItem(0, 'MainWindow')
        self.WidgetList.insertItem(1, 'LearnWindowPre1')
        """
        self.Stack.setCurrentIndex(0)

        self.show()
