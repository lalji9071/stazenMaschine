# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StanzeMaschine.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StanzenMaschine(object):
    def setupUi(self, StanzenMaschine):
        StanzenMaschine.setObjectName("StanzenMaschine")
        StanzenMaschine.resize(694, 589)
        self.groupBox = QtWidgets.QGroupBox(StanzenMaschine)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 351, 71))
        self.groupBox.setObjectName("groupBox")
        self.pbConnect = QtWidgets.QPushButton(self.groupBox)
        self.pbConnect.setGeometry(QtCore.QRect(40, 30, 75, 23))
        self.pbConnect.setObjectName("pbConnect")
        self.lineEditIP = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditIP.setGeometry(QtCore.QRect(150, 30, 128, 23))
        self.lineEditIP.setObjectName("lineEditIP")

        self.retranslateUi(StanzenMaschine)
        QtCore.QMetaObject.connectSlotsByName(StanzenMaschine)

    def retranslateUi(self, StanzenMaschine):
        _translate = QtCore.QCoreApplication.translate
        StanzenMaschine.setWindowTitle(_translate("StanzenMaschine", "Form"))
        self.groupBox.setTitle(_translate("StanzenMaschine", "GroupBox"))
        self.pbConnect.setText(_translate("StanzenMaschine", "Connect"))

