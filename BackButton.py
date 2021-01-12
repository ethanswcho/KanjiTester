import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QTableWidget, QFormLayout, QGroupBox, QScrollArea
from PyQt5.QtGui import QFont

from DefaultWindow import DefaultWindow

class BackButton(QPushButton):

    def __init__(self, widget, stack, destination):
        super().__init__(widget)
        self.destination = destination
        self.stack = stack
        self.move(30, 20)
    
    def _pressed_(self):
        self.stack.setCurrentIndex(self.destination)
        self.stack.show()

