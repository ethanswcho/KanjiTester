import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QTableWidget, QFormLayout, QGroupBox, QScrollArea
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect, QMargins

from buttons.BackButton import BackButton
from windows.DefaultWindow import DefaultWindow

class About():

    def __init__(self, stack):
        stack.setCurrentIndex(2)
        self.stack = stack
        self.widget = self.stack.currentWidget()

        self.BackButton = BackButton(self.widget, self.stack, 0)

        self.github = self.widget.findChild(QLabel, 'github')
        self.github.setText("<a href=\"https://github.com/tuna1mayo1/KanjiTester/\">Github link for the project</a>")
        self.github.setOpenExternalLinks(True)

        self.BackButton.show()
        self.stack.show()