from PyQt5.QtWidgets import QApplication, QWidget, QLabel

# potentially unused file now
"""
interface.py

Defines and generates the gui for this project.
"""
class Program(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        app = QApplication([])
        label = QLabel('hello world!')
        label.show()


        label = QLabel('hello world!')
        label.show()