from gui import Ui_MainWindow
import sys
from PyQt5 import QtWidgets, QtCore, QtGui, Qt

"""
Session Zero
A computational creativity project based on the stat system of tabletop roleplaying games. Helps writers, tabletop players, and dungeon masters create, build, and understand the characters in their world.

main file
used to initialize things and test out functionality
"""
        
class Program(QtWidgets.QMainWindow):
    def __init__(self):
        super(Program, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.label.setFont(QtGui.QFont('SansSerif', 30))
        #self.ui.label.setGeometry(QtCore.QRect(10, 10, 200, 200))
        self.ui.label.setText('Eat ass')

        self.ui.pushButton.clicked.connect(self.clickButton)

    def clickButton(self):
        self.ui.label.setText('I did it')
        self.ui.stackedWidget.setCurrentIndex(1)



if __name__ == '__main__':
    
    STR, DEX, CON, INT, WIS, CHA = (0,)*6
    
    app = QtWidgets.QApplication([])
    running = Program()
    running.show()

    sys.exit(app.exec_())
