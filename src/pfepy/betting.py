import sys
from PyQt4 import QtCore, QtGui, uic

# -*- coding:utf-8 -*-
form_class = uic.loadUiType("betting.ui") [0]

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.loss = 0
        self.profit = 0
        self.mult = 0
        self.div = 0
        self.total_stake = 0
        self.stake = 0
        self.odds = 0
        self.calc_pushButton.clicked.connect(self.calc_pushButton_clicked)
        if self.profitLineEdit.text():
            self.profit = int(self.profitLineEdit.text())
        self.yes_btn.clicked.connect(self.yes_btn_clicked)
        self.no_btn.clicked.connect(self.no_btn_clicked)



    def calc_pushButton_clicked(self):
        self.mult = float(self.multiLineEdit.text())
        self.div = float(self.divLineEdit.text())
        self.odds = self.mult / self.div
        self.profit = float(self.profitLineEdit.text())
        self.stake = self.profit / self.odds
        self.total_stake = self.stake  + (self.stake / 10) + self.loss
        self.stakeLineEdit.setText(str(self.total_stake))

    def yes_btn_clicked(self):
        self.winLineEdit.setText("£" + (str(self.stake * self.odds) + " won!!"))

    def no_btn_clicked(self):
        self.loss = self.total_stake
        print(self.loss)

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.show()
app.exec_()