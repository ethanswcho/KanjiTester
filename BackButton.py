import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QTableWidget, QFormLayout, QGroupBox, QScrollArea
from PyQt5.QtGui import QFont

from DefaultWindow import DefaultWindow

# Creates a Back Button AND adds itself to the widget.
# BackButton located in top left of each window that allows users to traverse backwards.
# Key argument "Destination" allows this button to traverse to the approrpiate page when pressed.

class BackButton(QPushButton):

    def __init__(self, widget, stack, destination):
        super().__init__('Back', widget)
        self.destination = destination
        self.stack = stack
        self.move(10, 10)
        self.clicked.connect(self._pressed_)
    
    def _pressed_(self):
        self.stack.setCurrentIndex(self.destination)
        self.stack.show()
