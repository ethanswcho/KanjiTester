import sys
import random
import numpy as np

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QFormLayout, QGroupBox, QScrollArea, QRadioButton, QButtonGroup
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect, QMargins
from BackButton import BackButton

from DefaultWindow import DefaultWindow

# Mark and analyze the users test results.
# Show the mark and what questions they got wrong, along with what the correct answers were

class Result():

    def __init__(self, stack, num_qs, kanjis_asked, attempt, answerkey): 
        self.stack = stack
        self.num_qs = num_qs
        self.kanjis_asked = kanjis_asked
        self.attempt = attempt
        self.answerkey = answerkey

        marking = self._analyze()
        self.widget = self._get_widget(marking)

    # Return a "marking" array of size self.num_qs that contains T/F depending on whether the question was correct or not    
    def _analyze(self):
        
        marking = [True] * self.num_qs
        for n in range(self.num_qs):
            if self.attempt[n] != self.answerkey[n]:
                marking[n] = False
        
        return marking
    
    def _get_widget(self, marking):
        widget = QWidget()
        return widget
        