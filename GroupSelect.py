import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QFont

from DefaultWindow import DefaultWindow
from Kanjis import Kanjis
from Learn import Learn
from BackButton import BackButton
from Test import Test

class GroupSelect():

    def __init__(self, stack, mode):
        stack.setCurrentIndex(1)
        self.stack = stack
        self.widget = self.stack.currentWidget()
        self.mode = mode

        self.BackButton = BackButton(self.widget, self.stack, 0)
        
        self.N1 = self.widget.findChild(QPushButton, 'N1')
        self.N2 = self.widget.findChild(QPushButton, 'N2')
        self.N3 = self.widget.findChild(QPushButton, 'N3')
        self.N4 = self.widget.findChild(QPushButton, 'N4')
        self.N5 = self.widget.findChild(QPushButton, 'N5')

        self.N1.clicked.connect(lambda: self._clicked_N(self.N1.text()))
        self.N2.clicked.connect(lambda: self._clicked_N(self.N2.text()))
        self.N3.clicked.connect(lambda: self._clicked_N(self.N3.text()))
        self.N4.clicked.connect(lambda: self._clicked_N(self.N4.text()))
        self.N5.clicked.connect(lambda: self._clicked_N(self.N5.text()))

        kanjis = Kanjis()
        self.Kanjis = kanjis.get_instance()

        self.stack.show()
        self.BackButton.show()
        
    
    # Fillter Kanjis to chosen level and pass it onto Learn/Test
    def _clicked_N(self, level):
        print('level selected: ' + level)
        level = level.replace('N', '')
        
        filtered_kanjis = self.Kanjis[level]

        if self.mode == "learn":
            self.Learn = Learn(self.stack, filtered_kanjis)
        elif self.mode == "test":
            self.Test = Test(self.stack, filtered_kanjis)

        

        

