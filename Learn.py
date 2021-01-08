import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QTableWidget, QFormLayout, QGroupBox, QScrollArea
from PyQt5.QtGui import QFont

from DefaultWindow import DefaultWindow

# Dynamically construct a vertical scrollable area of kanji information of chosen level.
class Learn():

    def __init__(self, stack, kanjilist):
        #stack.setCurrentIndex(2)
        #self.stack = stack
        #self.widget = self.stack.currentWidget()
    
        #self.widget.setLayout(self.kanjilist_to_layout(kanjilist))

        self.stack = stack

        widget = QWidget()
        layout = self.kanjilist_to_layout(kanjilist)
        layout.addWidget(widget)
        widget.setLayout = self.kanjilist_to_layout(kanjilist)
        self.widget = widget
        self.stack.addWidget(widget)
        self.stack.setCurrentWidget(self.widget)
        self.widget.show()
        #self.stack.show()
        

    # Takes in the kanjilist and returns a scrollable vertical layout with kanji and its information. 
    def kanjilist_to_layout(self, kanjilist):

        form_layout = QFormLayout()
        group = QGroupBox()

        kanjis = []
        infos = []

        for index in range(len(kanjilist)): 
            
            entry = kanjilist[index]

            kanji = list(entry.keys())[0]
            data = list(entry.values())[0]
            
            strokes = data["strokes"]
            meanings = ", ".join(data["meanings"])
            readings_onyomi = data["readings_on"]
            readings_kunyomi = data["readings_kun"]

            info = 'Meanings: {}\nReading (Onyomi): {}\nReadings (Kunyomi): {}\nStrokes: {}'.format(meanings, readings_onyomi, readings_kunyomi, strokes)
            
            kanjis.append(QLabel(kanji))
            infos.append(QLabel(info))

            form_layout.addRow(kanjis[index], infos[index])

            """
            table = QTableWidget()
            table.setRowCount(4)
            table.setColumnCount(2)

            table.setItem(0, 0, )
            """
        
        group.setLayout(form_layout)
        scroll = QScrollArea()
        scroll.setWidget(group)
        scroll.setWidgetResizable(True)

        layout = QVBoxLayout()
        layout.addWidget(scroll)

        return layout

        
            
            




            

            
        
