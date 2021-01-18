import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QStackedWidget
from PyQt5.uic import loadUi

from .MainWindow import MainWindow

# Stack of UIs. Generated on Qt Designer and loaded using loadUi method.

class Stack(QStackedWidget):
    def __init__(self):
        super(Stack, self).__init__()
        loadUi('uis/Stack.ui', self)

