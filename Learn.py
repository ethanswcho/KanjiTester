import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QTableWidget, QFormLayout, QGroupBox, QScrollArea
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect, QMargins
from BackButton import BackButton

from DefaultWindow import DefaultWindow

# Dynamically construct a vertical scrollable area of kanji information of chosen level.
class Learn():

    def __init__(self, stack, kanjilist):

        self.stack = stack
        self.widget  = self.get_widget(kanjilist)
        BackButton(self.widget, self.stack, 1)
        self.stack.addWidget(self.widget)
        self.stack.setCurrentWidget(self.widget)
        self.stack.show()


    # Takes in the kanjilist and returns a scrollable vertical widget that contains kanjis from input kanjilist
    def get_widget(self, kanjilist):

        form_layout = QFormLayout()
        group = QGroupBox()

        font_kanji = QFont("Times", 30, QFont.Bold)
        font_info = QFont("Times", 15,)

        for index in range(len(kanjilist)): 
            
            entry = kanjilist[index]

            kanji = list(entry.keys())[0]
            data = list(entry.values())[0]
            
            strokes = data["strokes"]
            meanings = ", ".join(data["meanings"])
            readings_onyomi = data["readings_on"]
            readings_kunyomi = data["readings_kun"]

            info = 'Meanings: {}\nReading (Onyomi): {}\nReadings (Kunyomi): {}\nStrokes: {}'.format(meanings, readings_onyomi, readings_kunyomi, strokes)
            
            kanji = QLabel(kanji)
            info = QLabel(info)
            kanji.setFont(font_kanji)
            info.setFont(font_info)
            
            form_layout.addRow(kanji, info)
        
        group.setLayout(form_layout)
        scroll = QScrollArea()
        scroll.setWidget(group)
        scroll.setWidgetResizable(True)

        layout = QVBoxLayout()
        layout.addWidget(scroll)
        layout_margins = QMargins(50, 50, 50, 50)
        layout.setContentsMargins(layout_margins)
        widget = QWidget()
        widget.setLayout(layout)

        return widget

        
            
            




            

            
        
