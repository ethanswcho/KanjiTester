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
        self.num_qs = 10
        self.attempt = np.zeros(self.num_qs)

        self.widget  = self._get_widget(kanjilist)
        BackButton(self.widget, self.stack, 1)
        FinishedButton = QPushButton("Finished", self.widget)
        FinishedButton.move(1090, 10)
        FinishedButton.clicked.connect(self._load_results)
    
        self.stack.addWidget(self.widget)
        self.stack.setCurrentWidget(self.widget)
        self.stack.show()
        
    def _load_results(self):
        
        self.attempt = [button.text() for button in self.button_grps if button.isChecked()]
        for a in self.attempt:
            print(a)


    
    def _get_widget(self, kanjilist):

        widget = QWidget()
        form_layout = QFormLayout()
        group = QGroupBox()

        font_kanji = QFont("Times", 50, QFont.Bold)
        layout_margins = QMargins(50, 50, 50, 50)
        question_margins = QMargins(50, 30, 0, 0)

        end = len(kanjilist)
        kanjis = [list(entry.keys())[0] for entry in kanjilist]
        meanings = [list(entry.values())[0]["meanings"] for entry in kanjilist]
        meanings = [", ".join(meaning) for meaning in meanings]

        # Randomly select kanji_nums number of kanji indexes to create a test set
        possible_kanjis = list(range(end))
        selected_indexes = random.sample(possible_kanjis, self.num_qs)
        
        self.answerkey = []
        self.button_grps = []
    
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

            #self.button_grps.append([r0, r1, r2, r3])
            self.button_grps = self.button_grps + [r0, r1, r2, r3]

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
        
        widget.setLayout(layout)
        return widget