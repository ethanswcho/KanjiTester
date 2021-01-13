import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QStackedWidget
from PyQt5.QtGui import QFont

from DefaultWindow import DefaultWindow
from GroupSelect import GroupSelect

class MainWindow():

    def __init__(self, stack):
        stack.setCurrentIndex(0)
        self.stack = stack
        self.widget = self.stack.currentWidget()
        self.stack.show()

        self.learnButton = self.widget.findChild(QPushButton, 'learnButton')
        self.learnButton.clicked.connect(self.clicked_learn)
        
        self.testButton = self.widget.findChild(QPushButton, 'testButton')
        self.testButton.clicked.connect(self.clicked_test)

    def clicked_learn(self):
        self.GS = GroupSelect(self.stack, mode="learn")
    
    def clicked_test(self):
        self.GS = GroupSelect(self.stack, mode="test")

