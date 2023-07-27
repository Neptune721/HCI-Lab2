# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asrInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 730)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")



        self.textbox = QtWidgets.QLineEdit(MainWindow)
        self.textbox.setFont(QtGui.QFont('Microsoft YaHei', 15))
        self.textbox.setGeometry(40, 660, 300, 40)
        self.textbox.setStyleSheet(
            "QLineEdit{color:rgb(0,0,0)}" 
            "QLineEdit{background-color:rgb(242,242,242)}" 
            "QLineEdit:hover{background-color:rgb(255,255,255)}"
        )

        self.text_btn = QtWidgets.QPushButton(MainWindow)
        self.text_btn.setFont(QtGui.QFont('Microsoft YaHei', 10))
        self.text_btn.setGeometry(340, 660, 40, 40)
        self.text_btn.setStyleSheet(
            "QPushButton{border-image: url(icon/search.png)}"
            "QPushButton:hover{border-image: url(icon/search3.png)}"
            "QPushButton:pressed{border-image: url(icon/search.png)}"
        )

        self.recognize_btn = QtWidgets.QPushButton(MainWindow)
        self.recognize_btn.setFont(QtGui.QFont('Microsoft YaHei', 10))
        self.recognize_btn.setGeometry(0, 660, 40, 40)
        self.recognize_btn.setStyleSheet(
            "QPushButton{border-image: url(icon/phone.png)}"
        )

        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(28, 50, 322, 242))
        self.voiceFig.setText("")
        self.gif = QMovie("icon/voice.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 250, 300, 150))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 400, 350, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 480, 350, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 510, 350, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 540, 350, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 570, 350, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
        self.label.setText(_translate("MainWindow", "Hi! How can I help?"))
        self.label_2.setText(_translate("MainWindow", "You can:"))
        self.label_3.setText(_translate("MainWindow", "1. Enjoy music speak \"music\""))
        self.label_4.setText(_translate("MainWindow", "2. open file speak \"text\""))
        self.label_5.setText(_translate("MainWindow", "3. use google speak \"search\""))


