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
        self.traits = []
        self.best = ''
        self.worst =''

        #self.ui.label.setFont(QtGui.QFont('SansSerif', 30))
        #self.ui.label.setGeometry(QtCore.QRect(10, 10, 200, 200))
        #self.ui.label.setText('Eat ass')

        self.ui.buildBtn.clicked.connect(self.clickBuild)
        self.ui.wave1GenBtn.clicked.connect(self.clickGen)
        self.ui.wave1EndBtn.clicked.connect(self.wave1End)
        self.ui.wave2GenBtn.clicked.connect(self.clickGen2)
        self.ui.wave2EndBtn.clicked.connect(self.wave2End)
        self.ui.addTraitBtn.clicked.connect(self.addTrait)
        self.ui.delTraitBtn.clicked.connect(self.removeTraits)
        self.ui.wave3Genbtn.clicked.connect(self.clickGen3)

    def clickBuild(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    """
    clickGen()
    Takes the user's input of name, strengths, and weaknesses and passes it forward.
    Populates three QTableWidgets with generated statblocks.
    """
    def clickGen(self):
        # get character name
        self.name = self.ui.nameEdit.text()
		# return if name is blank
        if self.name == '':
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
        else:
            chosen = self.ui.statblock3

        # populate stats with chosen statblock
        for i in range(6):
            self.stats[i] = int(chosen.item(i, 1).text())

        # move to wave 2
        self.ui.stackedWidget.setCurrentIndex(3)

    """
    clickGen2()
    Takes the user's choices of character traits and calls another function to generate new ones.
    Populates an editable QListWidget with traits.
    """
    def clickGen2(self):
        # get greatest strengths/weaknesses
        tmpTraits = []
        bestList = self.ui.traitPlusGroup.buttons()
        worstList = self.ui.traitMinusGroup.buttons()
        for i in range(7):
            if bestList[i].isChecked():
                self.best = bestList[i].text().lower()
            if worstList[i].isChecked():
                self.worst = worstList[i].text().lower()

        print(self.best)
        print(self.worst)
        groups = [self.ui.braveGroup.buttons(), self.ui.careGroup.buttons(), self.ui.friendGroup.buttons(), self.ui.honestGroup.buttons(), self.ui.humbleGroup.buttons(), self.ui.modestGroup.buttons(), 
                  self.ui.moneyGroup.buttons(), self.ui.patientGroup.buttons(), self.ui.senseGroup.buttons()]
        
        # populate traits for randomization
        for btns in groups:
            for i in range(3):
                if btns[i].isChecked():
                    tmpTraits.append(btns[i].text().lower())
                    break
        
        # generate additional traits and populate list
        #for t in algs.getTraits(self.best, self.worst, tmpTraits, self.stats):
        self.ui.listWidget.addItems(algs.getTraits(self.best, self.worst, tmpTraits, self.stats))

        # populate lists with generated traits
        self.ui.stackedWidget.setCurrentIndex(4)

    """
    wave2End()
    Finishes the second wave of second wave of character creation, adding the primary set of traits to the character.
    Moves the window ahead to index 5.
    """
    def wave2End(self):
        # take values from listWidget and add to traits
        for i in range(self.ui.listWidget.count()):
            self.traits.append(self.ui.listWidget.item(i).text())

        self.ui.stackedWidget.setCurrentIndex(5)

    """
    addTrait()
    Prompts the user to add a new trait to the list in Wave 2, then adds it if valid.
    """
    def addTrait(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter the new trait:')

        if ok:
            self.ui.listWidget.addItem(text)

    """
    removeTraits()
    Deletes the selected traits from the trait list in Wave 2.
    """
    def removeTraits(self):
        for item in self.ui.listWidget.selectedItems():
            self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

    """
    clickGen3()
    Takes the user's choices of background and motivation and generates a series of backstories following it, as well as adds new traits to the list.
    Places the backstories in the next window for the user to select.
    """
    def clickGen3(self):
        # create list of background choices
        background = []
        
        background.append(self.ui.familyBox.currentText())
        background.append(self.ui.childBox.currentText())
        background.append(self.ui.envBox.currentText())
        background.append(self.ui.socialBox.currentText())
        background.append(self.ui.rolemodelBox.currentText())
        background.append(self.ui.memBox.currentText())
        background.append(self.ui.goalBox.currentText())

        txt = algs.getBackground(background, self.traits, self.stats)

        self.ui.stackedWidget.setCurrentIndex(6)

if __name__ == '__main__':
    
    #STR, DEX, CON, INT, WIS, CHA = (0,)*6
    
    app = QtWidgets.QApplication([])
    running = Program()
    running.show()
    random.seed()

    sys.exit(app.exec_())
