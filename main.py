import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QStackedWidget
from PyQt5.uic import loadUi

from windows.MainWindow import MainWindow
from windows.Stack import Stack


if __name__ == "__main__":

    app = QApplication(sys.argv)
    stack = Stack()
    MW = MainWindow(stack)
    app.exec_()
