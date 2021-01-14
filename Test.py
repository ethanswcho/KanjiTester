import sys
import random
import numpy as np

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QFormLayout, QGroupBox, QScrollArea, QRadioButton, QButtonGroup
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect, QMargins
from BackButton import BackButton

from DefaultWindow import DefaultWindow


class Test():

    def __init__(self, stack, kanjilist):

        self.stack = stack
        self.widget  = self._get_widget(kanjilist)
        BackButton(self.widget, self.stack, 1)
        self.stack.addWidget(self.widget)
        self.stack.setCurrentWidget(self.widget)
        self.stack.show()
        self.num_qs = 10
        self.attempt = np.zeros(self.num_qs)
    
    def _get_widget(self, kanjilist):

        widget = QWidget()
        form_layout = QFormLayout()
        group = QGroupBox()

        font_kanji = QFont("Times", 50, QFont.Bold)
        layout_margins = QMargins(50, 50, 50, 50)
        question_margins = QMargins(50, 30, 30, 0)

        end = len(kanjilist)
        kanjis = [list(entry.keys())[0] for entry in kanjilist]
        meanings = [list(entry.values())[0]["meanings"] for entry in kanjilist]
        meanings = [", ".join(meaning) for meaning in meanings]

        # Randomly select kanji_nums number of kanji indexes to create a test set
        possible_kanjis = list(range(end))
        selected_indexes = random.sample(possible_kanjis, self.num_qs)
        
        self.answerkey = []
    
        for index in selected_indexes: 

            kanji = kanjis[index]
            kanji = QLabel(kanji)
            kanji.setFont(font_kanji)

            answer = meanings[index]
            self.answerkey.append(answer)

            # Generate 4 possible answer options including a correct one
            answers = [answer]
            possible_indexes = list(range(1, index)) + list(range(index+1, end))
            random_indexes = random.sample(possible_indexes, 3)
            answers = answers + [meanings[i] for i in random_indexes]
            random.shuffle(answers)

            # Generate a box of 4 shuffled radio buttons
            r0 = QRadioButton(answers[0])
            r1 = QRadioButton(answers[1])
            r2 = QRadioButton(answers[2])
            r3 = QRadioButton(answers[3])

            button_grp = QVBoxLayout()
            button_grp.addWidget(r0)
            button_grp.addWidget(r1)
            button_grp.addWidget(r2)
            button_grp.addWidget(r3)
        
            button_grp.setContentsMargins(question_margins)
            form_layout.addRow(kanji, button_grp)
        
        group.setLayout(form_layout)
        scroll = QScrollArea()
        scroll.setWidget(group)
        scroll.setWidgetResizable(True)

        layout = QVBoxLayout()
        layout.setContentsMargins(layout_margins)
        layout.addWidget(scroll)
        #layout.setGeometry(QRect(20, 20, 100, 100))
        
        widget.setLayout(layout)

        return widget