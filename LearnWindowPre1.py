import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QFont

from DefaultWindow import DefaultWindow

class LearnWindowPre1(DefaultWindow):

        
    def initUI(self, MainWindow):
        self.instruction = "Please select levels of kanji you would like to learn."
        self.label_instruction = QLabel(self.instruction, self)
        self.label_instruction.setFont(QFont('Arial', 100))
        self.label_instruction.move(260, 100)
