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

        # When user is done reviewing the results, they can go back to the title screen.
        ToTitleButton = QPushButton("Back to Title", self.widget)
        ToTitleButton.move(10, 10)
        ToTitleButton.clicked.connect(self._back_to_title)

        self.stack.addWidget(self.widget)
        self.stack.setCurrentWidget(self.widget)
        self.stack.show()

    # Return a "marking" array of size self.num_qs that contains T/F depending on whether the question at the index was correct or not    
    def _analyze(self):
        
        marking = [True] * self.num_qs
        for n in range(self.num_qs):
            if self.attempt[n] != self.answerkey[n]:
                marking[n] = False
        
        return marking
    
    def _get_widget(self, marking):
        widget = QWidget()
        form_layout = QFormLayout()
        group = QGroupBox()
        layout_margins = QMargins(50, 50, 50, 50)

        font_kanji = QFont("Times", 50, QFont.Bold)
        font_feedback = QFont("Times", 13, QFont.Bold)
        
        for n in range(self.num_qs):
            kanji = self.kanjis_asked[n]
            kanji = QLabel(kanji)
            kanji.setFont(font_kanji)

            feedback = QLabel()

            # Attempt was correct
            if marking[n]:
                feedback.setText('<font color="green">Correct!</font><br>Answer: ' + self.answerkey[n])

            else:
                # No attempt was made
                if self.attempt[n] is None:
                    feedback.setText('<font color="red">Not Attempted!</font><br>Answer: ' + self.answerkey[n])
                # Attempt was made but incorrect
                else:
                    feedback.setText('<font color="red">Incorrect!</font><br><b>You guessed:</b> ' + self.attempt[n] + "<br><b>Answer:</b> " + self.answerkey[n])

            feedback.setFont(font_feedback)
            form_layout.addRow(kanji, feedback)
        
        group.setLayout(form_layout)
        scroll = QScrollArea()
        scroll.setWidget(group)
        scroll.setWidgetResizable(True)

        layout = QVBoxLayout()
        layout.setContentsMargins(layout_margins)
        layout.addWidget(scroll)
        
        widget.setLayout(layout)
        return widget
        
    # When user is done reviewing the results, they can go back to the title screen.
    def _back_to_title(self):
        self.stack.setCurrentIndex(0)
        self.stack.show()
        