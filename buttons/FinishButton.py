import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QTableWidget, QFormLayout, QGroupBox, QScrollArea
from PyQt5.QtGui import QFont

from windows.DefaultWindow import DefaultWindow

# Creates a Finshed Button AND adds itself to the widget.
# Finished button located in top right of test window that allows users to submit their solution (to get it marked)
# Key argument "Destination" allows this button to traverse to the approrpiate page when pressed.

class FinishButton(QPushButton):

    def __init__(self, widget, stack):
        self.stack = stack
        self.move(10, 10)
        self.clicked.connect(self._pressed)
    