import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QStackedWidget
from PyQt5.uic import loadUi
from MainWindow import MainWindow
from Controller import Controller

"""
if __name__ == "__main__":

    app = QApplication(sys.argv)
    MW = MainWindow()
    MW.initUI()
    MW.show()
    app.exec_()



if __name__ == "__main__":

    app = QApplication(sys.argv)
    Controller = Controller()

    #MW.initUI()
    #MW.show()
    app.exec_()
"""

class UI(QStackedWidget):
    def __init__(self):
        super(UI, self).__init__()
        loadUi('uis/Stack.ui', self)
        self.setCurrentIndex(1)
        self.show()

app = QApplication(sys.argv) 
window = UI()
app.exec_()