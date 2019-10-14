from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import os
import re

DIRECTORY = "D:/akshay"

import sys
import maya.cmds as cmds

USERAPPDIR = cmds.internalVar(userAppDir=True)
exporter_path = "2017/prefs/scripts/abcExporter/"
full_path=USERAPPDIR + exporter_path
sys.path.append(full_path)
from abcExporter import Exporter
reload(Exporter)




class sfUI(QDialog):

    def __init__(self):
        super(sfUI, self).__init__()
        self.setWindowTitle('EXPORT abc')
        self.episodes = []
        for x in os.listdir(DIRECTORY):
            if x.endswith('.ma') or x.endswith('.mb') or x.endswith('.txt'):
                continue
            self.episodes.append(x)

        self.seq = []
        self.take = ['t1', 't2', 't3', 't4']

        self.buildUI()
        #self.showUI()

    def buildUI(self):
        self.layout = QVBoxLayout(self)

        self.Layout0Widget = QWidget()
        self.Layout0 = QHBoxLayout(self.Layout0Widget)
        self.layout.addWidget(self.Layout0Widget)

        self.pathFeild = QLineEdit()
        self.Layout0.addWidget(self.pathFeild)
        self.pathFeild.setText('test path')

        self.Layout1Widget = QWidget()
        self.Layout1 = QHBoxLayout(self.Layout1Widget)
        self.layout.addWidget(self.Layout1Widget)

        self.epi_label = QLabel("Epi")
        self.epiBox = QComboBox()
        self.seq_label = QLabel("Seq")
        self.seqBox = QComboBox()
        self.take_label = QLabel("Take")
        self.takeBox = QComboBox()

        self.Layout1.addWidget(self.epi_label)
        for i in self.episodes:
            self.epiBox.addItem(i)
        self.Layout1.addWidget(self.epiBox)

        self.Layout1.addWidget(self.seq_label)
        for i in self.seq:
            self.seqBox.addItem(i)
        self.Layout1.addWidget(self.seqBox)

        self.Layout1.addWidget(self.take_label)
        for i in self.take:
            self.takeBox.addItem(i)
        self.Layout1.addWidget(self.takeBox)

        self.CBLayoutWidget = QWidget()
        self.CBLayout = QHBoxLayout(self.CBLayoutWidget)
        self.layout.addWidget(self.CBLayoutWidget)

        self.checkBox = QCheckBox("selectall", self)
        # checkBoxLabel = QLabel("select all")
        self.CBLayout.addWidget(self.checkBox)
        # CBLayout.addWidget(checkBoxLabel)

        self.Layout2Widget = QWidget()
        self.Layout2 = QHBoxLayout(self.Layout2Widget)
        self.layout.addWidget(self.Layout2Widget)

        self.listBox = QListWidget()
        self.Layout2.addWidget(self.listBox)

        self.Layout3Widget = QWidget()
        self.Layout3 = QHBoxLayout(self.Layout3Widget)
        self.layout.addWidget(self.Layout3Widget)

        ExpBtn = QPushButton('Export')
        ExpBtn.clicked.connect(self.function)
        self.Layout3.addWidget(ExpBtn)

        self.epiBox.currentIndexChanged.connect(self.upd_seq_item)
        self.find_maya_file()

    def on_combobox_changed(self):
        print "changing value"

    def upd_seq_item(self):
        self.seqBox.clear()
        self.seq = ['seq5', 'seq6']
        for i in self.seq:
            self.seqBox.addItem(i)

    def find_maya_file(self, directory="D:/akshay/test"):
        #self.clear()

        # D:/akshay/test (test directory)
        files = os.listdir(directory)
        mayaFiles = [f for f in files if f.endswith('.ma')]

        for ma in mayaFiles:
            item = QListWidgetItem(ma)
            # cb=QCheckBox(self)

            # self.listBox.addItem(cb)
            self.listBox.addItem(item)

            # print ma

    def function(self):
        self.pathFeild.setText('test path')
        '''
        print self.pathFeild.text()
        print self.checkBox.isChecked()
        print self.epiBox.currentText()
        print self.seqBox.currentText()
        print self.takeBox.currentText()

        currentItem = self.listBox.currentItem()

        print currentItem.text()

        '''
        self.currentItem = self.listBox.currentItem()
        exp = Exporter.test()
        exp.printer(path=self.pathFeild.text(), cb=self.checkBox.isChecked(), epi=self.epiBox.currentText(), seq= self.seqBox.currentText(), take= self.takeBox.currentText(), item=self.currentItem.text())
        






def showUI():
    ui = sfUI()
    ui.show()
    return ui

#ui = sfUI()