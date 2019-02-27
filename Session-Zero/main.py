from gui import Ui_MainWindow
import algs
import sys
import random
from PyQt5 import QtWidgets, QtCore, QtGui, Qt

statList = ['']
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
        self.name = ''
        self.stats = [0,0,0,0,0,0]
        print(self.stats)

        #self.ui.label.setFont(QtGui.QFont('SansSerif', 30))
        #self.ui.label.setGeometry(QtCore.QRect(10, 10, 200, 200))
        #self.ui.label.setText('Eat ass')

        self.ui.buildBtn.clicked.connect(self.clickBuild)
        self.ui.wave1GenBtn.clicked.connect(self.clickGen)
        self.ui.wave1EndBtn.clicked.connect(self.wave1End)

    def clickBuild(self):
        self.ui.stackedWidget.setCurrentIndex(1)

	"""
	clickGen()
	Takes the user's input of name, strengths, and weaknesses and passes it forward.
	Populates three tables with generated statblocks.
	"""
    def clickGen(self):
        # get character name
        self.name = self.ui.nameEdit.text()
		# return if name is blank
		if name == '':
			return
        # get chosen statistical strengths/weaknesses
        plusButtons = self.ui.statPlusGroup.buttons()
        minusButtons = self.ui.statMinusGroup.buttons()

        choices = []
        tempBlocks = []
        # generate stats based on str/weak
        for i in range(6):
            if plusButtons[i].isChecked():
                choices.append(1)
            elif minusButtons[i].isChecked():
                choices.append(-1)
            else:
                choices.append(0)

        # generate 3 statblocks
        for i in range(3):
            tempBlocks.append(algs.getStatblock(choices, self.ui.raceBox.currentText(), self.ui.classBox.currentText()))
            print(tempBlocks[i])

        
        # populate tables with values
        for i in range(6):
            print(tempBlocks[0][i])
            self.ui.statblock1.setItem(i,1,QtWidgets.QTableWidgetItem(str(tempBlocks[0][i])))
            self.ui.statblock2.setItem(i,1,QtWidgets.QTableWidgetItem(str(tempBlocks[1][i])))
            self.ui.statblock3.setItem(i,1,QtWidgets.QTableWidgetItem(str(tempBlocks[2][i])))
            
        self.ui.stackedWidget.setCurrentIndex(2)
      
	"""
	wave1End()
	Finalizes the first wave of character creation, having built a statblock and character name/race/class
	Moves the window forward to index 3
	"""
    def wave1End(self):
		blockChoices = self.ui.statblockGroup.buttons()
		if blockChoices[0].isChecked():
			chosen = self.ui.statblock1
		elif blockChoices[1].isChecked():
			chosen = self.ui.statblock2
		else
			chosen = self.ui.statblock3
		
		# populate stats with chosen statblock
		for i in range(6):
			self.stats = int(chosen.item(i, 1))
			
		# move to wave 2
        self.ui.stackedWidget.setCurrentIndex(3)


if __name__ == '__main__':
    
    #STR, DEX, CON, INT, WIS, CHA = (0,)*6
    
    app = QtWidgets.QApplication([])
    running = Program()
    running.show()
    random.seed()

    sys.exit(app.exec_())
