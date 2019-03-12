from gui import Ui_MainWindow
import algs
import sys
import random
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
        self.name = ''
        self.stats = [0,0,0,0,0,0]
        self.traits = []
        self.skills = []
        self.bckgrndChoices = []
        self.best = ''
        self.worst =''
        self.cls = ''
        self.race = ''
        self.alignment = ''
        self.age = 0

        self.ui.titleLabel.setFont(QtGui.QFont('SansSerif', 30))
        #self.ui.label.setGeometry(QtCore.QRect(10, 10, 200, 200))

        self.ui.buildBtn.clicked.connect(self.clickBuild)
        self.ui.wave1GenBtn.clicked.connect(self.clickGen)
        self.ui.wave1EndBtn.clicked.connect(self.wave1End)
        self.ui.wave2GenBtn.clicked.connect(self.clickGen2)
        self.ui.wave2EndBtn.clicked.connect(self.wave2End)
        self.ui.addTraitBtn.clicked.connect(self.addTrait)
        self.ui.delTraitBtn.clicked.connect(self.removeTraits)
        self.ui.wave3Genbtn.clicked.connect(self.clickGen3)
        self.ui.finishButton.clicked.connect(self.genCharacter)
        self.ui.exportBtn.clicked.connect(self.exportCharacter)
        self.ui.newCharBtn.clicked.connect(self.restart)

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
        self.ui.nameEdit.clear()
        self.cls = self.ui.classBox.currentText()
        self.ui.classBox.setCurrentIndex(0)
        self.race = self.ui.raceBox.currentText()
        self.ui.raceBox.setCurrentIndex(0)
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
            plusButtons[i].setChecked(False)
            minusButtons[i].setChecked(False)
        

        # generate 3 statblocks
        for i in range(3):
            tempBlocks.append(algs.getStatblock(choices, self.ui.raceBox.currentText(), self.cls))
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
        self.ui.radioButton.setChecked(True)
        worstList[0].setChecked(True)

        print(self.best)
        print(self.worst)
        groups = [self.ui.braveGroup, self.ui.careGroup, self.ui.friendGroup, self.ui.honestGroup, self.ui.humbleGroup, self.ui.modestGroup, 
                  self.ui.moneyGroup, self.ui.patientGroup, self.ui.senseGroup, self.ui.witGroup]
        
        # populate traits for randomization
        for grp in groups:
            btns = grp.buttons()
            for i in range(3):
                if btns[i].isChecked():
                    tmpTraits.append(btns[i].text().lower())
                    grp.setExclusive(False)
                    btns[i].setChecked(False)
                    grp.setExclusive(True)
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

        self.ui.listWidget.clear()

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
    Takes the user's choices of background and motivation and generates a series of new traits for the list.
    Places the new traits in the next window for the user to select.
    """
    def clickGen3(self):
        # create list of background choices
        
        self.bckgrndChoices.append(self.ui.familyBox.currentText())
        self.ui.familyBox.setCurrentIndex(0)
        self.bckgrndChoices.append(self.ui.childBox.currentText())
        self.ui.childBox.setCurrentIndex(0)
        self.bckgrndChoices.append(self.ui.envBox.currentText())
        self.ui.envBox.setCurrentIndex(0)
        self.bckgrndChoices.append(self.ui.socialBox.currentText())
        self.ui.socialBox.setCurrentIndex(0)
        self.bckgrndChoices.append(self.ui.rolemodelBox.currentText())
        self.ui.rolemodelBox.setCurrentIndex(0)
        self.bckgrndChoices.append(self.ui.memBox.currentText())
        self.ui.memBox.setCurrentIndex(0)
        self.bckgrndChoices.append(self.ui.goalBox.currentText())
        self.ui.goalBox.setCurrentIndex(0)
        self.bckgrndChoices.append(self.ui.ageBox.currentText())
        self.ui.ageBox.setCurrentIndex(0)

        # adds three distinct lists of new traits to three list widgets
        self.ui.bList1.addItems(algs.getAdditionalTraits(self.bckgrndChoices, self.traits, self.stats, self.cls, self.race))
        self.ui.bList3.addItems(algs.getAdditionalTraits(self.bckgrndChoices, self.traits, self.stats, self.cls, self.race))
        self.ui.bList2.addItems(algs.getAdditionalTraits(self.bckgrndChoices, self.traits, self.stats, self.cls, self.race))

        self.ui.stackedWidget.setCurrentIndex(6)
        
    """
    genCharacter()
    Generates the full character according the the user's choices from the threee waves of questions and selections.
    Populates the various fields with stats, backstory, skills, and basic information.
    """
    # TODO: alignment, weight/height -> stretch goals
    def genCharacter(self):
        buttonList = self.ui.backgroundGroup.buttons()
        
        if buttonList[0].isChecked():
            chosen = self.ui.bList1
        elif buttonList[1].isChecked():
            chosen = self.ui.bList2
        else:
            chosen = self.ui.bList3
        
        # add new traits to trait list
        for i in range(chosen.count()):
            self.traits.append(chosen.item(i).text())

        self.ui.bList1.clear()
        self.ui.bList2.clear()
        self.ui.bList3.clear()

        # compute skills
        self.skills = algs.getSkills(self.stats, self.cls)

        # populate tables with stat and skill values
        for i in range(6):
            self.ui.statTable.setItem(i,1,QtWidgets.QTableWidgetItem(str(self.stats[i])))

        for i in range(len(self.skills)):
            self.ui.skillTable.setItem(i,1,QtWidgets.QTableWidgetItem(str(self.skills[i])))
            
        # generate textual background and fill textbox with it
        self.ui.bckgrndText.insertPlainText(algs.getBackground(self.name, self.traits, self.stats, self.cls, self.race, self.bckgrndChoices))

        # fill in header labels
        self.ui.nameLbl.setText(self.name)
        self.ui.classLbl.setText(self.cls)
        self.ui.raceLbl.setText(self.race)
        self.age = str(algs.getAge(self.race, self.bckgrndChoices[7]))
        self.ui.ageLbl.setText(self.age)
        self.ui.stackedWidget.setCurrentIndex(7)

    """
    exportCharacter()
    Takes the contents of the character sheet and writes it to a text file.
    """
    def exportCharacter(self):
        with open('{}.txt'.format(self.name), 'w') as outfile:
            outfile.write("Name: {}".format(self.name))
            outfile.write("Race: {}".format(self.race))
            outfile.write("Class: {}".format(self.cls))
            outfile.write("Age: {}\n".format(self.age))
            
            outfile.write("Stats:")
            for i in range(6):
                outfile.write(self.ui.statTable.item(i,0).text() + ': ' + str(self.stats[i]) + ' ')

            outfile.write("\nSkills:")
            for i in range(len(self.skills)):
                outfile.write(self.ui.skillTable.item(i,0).text() + ': ' + self.ui.skillTable.item(i,1).text() + ' ')

            outfile.write('\n' + self.ui.bckgrndText.toPlainText())

        Qt.QMessageBox.about(self,'Notice','Character data written to {}.txt'.format(self.name))

    """
    restart()
    Restarts the character creation process by setting the current page index to the first part of creation and resetting all variables to nothing.
    Also resets several lists to be empty.
    """
    def restart(self):
        self.name = ''
        self.stats = [0,0,0,0,0,0]
        self.traits = []
        self.skills = []
        self.bckgrndChoices = []
        self.best = ''
        self.worst =''
        self.cls = ''
        self.race = ''
        self.alignment = ''
        self.age = 0
        self.ui.bckgrndText.clear()
 
        self.ui.stackedWidget.setCurrentIndex(1)

if __name__ == '__main__':
    
    #STR, DEX, CON, INT, WIS, CHA = (0,)*6
    
    app = QtWidgets.QApplication([])
    running = Program()
    running.show()
    random.seed()

    sys.exit(app.exec_())
