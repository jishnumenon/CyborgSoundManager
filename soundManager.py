import sys
import os
import ast

from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 660, 540)
        self.setWindowTitle("Sound Manager")
        self.setWindowIcon(QtGui.QIcon('cyborgLogo1.png'))
        self.home()

	self.currentSetNumber = "SET1"

	# Define a Dictionary for audio files selected

	self.audioDict = {"SET1":{"TENTA" : "","TENTB" : "" , "TENTC" : "", "TENTD" : " " ,"TENTE" : " ","TENTF" : " "},
 "SET2":{"TENTA" : "","TENTB" : "" , "TENTC" : "", "TENTD" : " " ,"TENTE" : " ","TENTF" : " "},
 "SET3":{"TENTA" : "","TENTB" : "" , "TENTC" : "", "TENTD" : " " ,"TENTE" : " ","TENTF" : " "},
 "SET4":{"TENTA" : "","TENTB" : "" , "TENTC" : "", "TENTD" : " " ,"TENTE" : " ","TENTF" : " "},
 "SET5":{"TENTA" : "","TENTB" : "" , "TENTC" : "", "TENTD" : " " ,"TENTE" : " ","TENTF" : " "},
 "SET6":{"TENTA" : "","TENTB" : "" , "TENTC" : "", "TENTD" : " " ,"TENTE" : " ","TENTF" : " "}
 }


	# Background Image
        self.palette = QtGui.QPalette()
        self.palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap("1.png")))
 
        self.setPalette(self.palette)

	# Set the Logo Image
	self.logo = QtGui.QLabel() 
	self.pixmap = QtGui.QPixmap(os.getcwd() + '/cyborgLogo.png')
	self.logo.setPixmap(self.pixmap)
	self.logo.move(190,20)
	self.logo.resize(270,80)
	

    def home(self):

	#Exit Button
	self.exitBtn = QtGui.QPushButton("Quit", self)
        self.exitBtn.clicked.connect(self.close_application)
        self.exitBtn.resize(self.exitBtn.minimumSizeHint())
        self.exitBtn.move(540,420)
        self.exitBtn.resize(80,60)

	# browse for Tentacle A

        self.tentABtn = QtGui.QPushButton("Browse", self)
        self.tentABtn.clicked.connect(self.browseTentacleA)
        self.tentABtn.resize(self.tentABtn.minimumSizeHint())
        self.tentABtn.move(450,170)
	self.tentABtn.resize(100,30)

	# browse for Tentacle B
	
	self.tentBBtn = QtGui.QPushButton("Browse", self)
        self.tentBBtn.clicked.connect(self.browseTentacleB)
        self.tentBBtn.resize(self.tentBBtn.minimumSizeHint())
        self.tentBBtn.move(450,220)
	self.tentBBtn.resize(100,30)

	# browse for Tentacle C

	self.tentCBtn = QtGui.QPushButton("Browse", self)
        self.tentCBtn.clicked.connect(self.browseTentacleC)
        self.tentCBtn.resize(self.tentCBtn.minimumSizeHint())
        self.tentCBtn.move(450,270)
	self.tentCBtn.resize(100,30)

	# browse for Tentacle D

	self.tentDBtn = QtGui.QPushButton("Browse", self)
        self.tentDBtn.clicked.connect(self.browseTentacleD)
        self.tentDBtn.resize(self.tentDBtn.minimumSizeHint())
        self.tentDBtn.move(450,320)
	self.tentDBtn.resize(100,30)

	# browse for Tentacle E

	self.tentEBtn = QtGui.QPushButton("Browse", self)
        self.tentEBtn.clicked.connect(self.browseTentacleE)
        self.tentEBtn.resize(self.tentEBtn.minimumSizeHint())
        self.tentEBtn.move(450,370)
	self.tentEBtn.resize(100,30)


	# Label for  Selectinfg the set number
	self.setChoice = QtGui.QLabel("Select the Set", self)
	self.setChoice.move(80,120)
	self.setChoice.col = QtGui.QColor("white")

	# Drop Down Combo box
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.addItem("SET1")
        self.comboBox.addItem("SET2")
        self.comboBox.addItem("SET3")
        self.comboBox.addItem("SET4")
        self.comboBox.addItem("SET5")
        self.comboBox.addItem("SET6")
        self.comboBox.move(200, 120)
	self.comboBox.resize(220,30)
	self.comboBox.activated[str].connect(self.setSelected)
	
	# Burn Button 
	self.burnBtn = QtGui.QPushButton("Burn", self)
        self.burnBtn.clicked.connect(self.burnAudio)
        self.burnBtn.resize(self.burnBtn.minimumSizeHint())
        self.burnBtn.move(220,420)
        self.burnBtn.resize(210,50)


	self.show()


    def setSelected(self,currentSetNumber):
	currentSetNumber = str(self.comboBox.currentText())
	print currentSetNumber


    def browseTentacleA(self):
	print (" Selecting the sound for Tentacle A")
	self.tentacleAFileName = str(QtGui.QFileDialog.getOpenFileName(self, 'Open File'))
	currentSetNumber = str(self.comboBox.currentText())
	self.audioDict[currentSetNumber]["TENTA"]=self.tentacleAFileName
	print self.audioDict[currentSetNumber]

    def browseTentacleB(self):
	print (" Selecting the sound for Tentacle B")
	self.tentacleBFileName = str(QtGui.QFileDialog.getOpenFileName(self, 'Open File'))
        currentSetNumber = str(self.comboBox.currentText())
        self.audioDict[currentSetNumber]["TENTB"]=self.tentacleBFileName
        print self.audioDict[currentSetNumber]



    def browseTentacleC(self):
	self.tentacleCFileName = str(QtGui.QFileDialog.getOpenFileName(self, 'Open File'))
	currentSetNumber = str(self.comboBox.currentText())
        self.audioDict[currentSetNumber]["TENTC"]=self.tentacleCFileName
        print self.audioDict[currentSetNumber]



    def browseTentacleD(self):
	print (" Selecting the sound for Tentacle D")
	self.tentacleDFileName = str(QtGui.QFileDialog.getOpenFileName(self, 'Open File'))
        currentSetNumber = str(self.comboBox.currentText())
        self.audioDict[currentSetNumber]["TENTD"]=self.tentacleDFileName
        print self.audioDict[currentSetNumber]


    def browseTentacleE(self):
	print (" Selecting the sound for Tentacle E")
	self.tentacleEFileName = str(QtGui.QFileDialog.getOpenFileName(self, 'Open File'))
        currentSetNumber = str(self.comboBox.currentText())
        self.audioDict[currentSetNumber]["TENTE"]=self.tentacleEFileName
        print self.audioDict[currentSetNumber]


    def browseTentacleF(self):
        print (" Selecting the sound for Tentacle F")
        self.tentacleFFileName = str(QtGui.QFileDialog.getOpenFileName(self, 'Open File'))
        currentSetNumber = str(self.comboBox.currentText())
        self.audioDict[currentSetNumber]["TENTF"]=self.tentacleFFileName
        print self.audioDict[currentSetNumber]



    def mkDirectory(self):
	print "inside directory Fn"
	for key, value in self.audioDict.iteritems():
		command1 = "mkdir " + str(os.getcwd()) + '/audio/' + str(key)
		print key
		os.system(command1)


    def copyFiles(self):
	for key, value in self.audioDict.iteritems():
		directoryNow = str(key)
		insideNow = str(value)
		for key, value in ast.literal_eval(insideNow).iteritems():
			tentNow = key
			fileNow = value
			if (str(tentNow) == "TENTA"):
				command2 = str("cp " + str(fileNow) + " " + str(os.getcwd()) + '/audio/' + str(directoryNow)+"/"+"T1"+"I0"+directoryNow[0]+directoryNow[3]+".wav"  )
				print command2
				os.system(command2)

			if (str(tentNow) == "TENTB"):
				command2 = str("cp " + str(fileNow) + " " + str(os.getcwd()) + '/audio/' + str(directoryNow)+"/"+"T2"+"I0"+directoryNow[0]+directoryNow[3]+".wav"  )
				print command2
				os.system(command2)

			if (str(tentNow) == "TENTC"):
				command2 = str("cp " + str(fileNow) + " " + str(os.getcwd()) + '/audio/' + str(directoryNow)+"/"+"T3"+"I0"+directoryNow[0]+directoryNow[3]+".wav"  )
				print command2
				os.system(command2)

			if (str(tentNow) == "TENTD"):
				command2 = str("cp " + str(fileNow) + " " + str(os.getcwd()) + '/audio/' + str(directoryNow)+"/"+"T4"+"I0"+directoryNow[0]+directoryNow[3]+".wav"  )
				print command2
				os.system(command2)

			if (str(tentNow) == "TENTE"):
				command2 = str("cp " + str(fileNow) + " " + str(os.getcwd()) + '/audio/' + str(directoryNow)+"/"+"T5"+"I0"+directoryNow[0]+directoryNow[3]+".wav"  )
				print command2
				os.system(command2)

			if (str(tentNow) == "TENTF"):
				command2 = str("cp " + str(fileNow) + " " + str(os.getcwd()) + '/audio/' + str(directoryNow)+"/"+"T6"+"I0"+directoryNow[0]+directoryNow[3]+".wav"  )
				print command2
				os.system(command2)

			else:

				print "Error in separating File."






    def burnAudio(self):
	print "Burning"
	self.copyFiles()
	os.system("sshpass -p 'raspberry' scp -r audio/ pi@10.0.0.200:/home/pi/Desktop")

    def close_application(self):
 	print("EXit the application")
	sys.exit()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()



