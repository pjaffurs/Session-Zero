from PyQt5.QtWidgets import QApplication, QLabel


"""
interface.py

Defines and generates the gui for this project.
"""

def initGUI():
    app = QApplication([])
    label = QLabel('hello world!')
    label.show()
    app.exec_()
