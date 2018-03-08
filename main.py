# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 242)
        MainWindow.setMinimumSize(QtCore.QSize(700, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.table_area = QtWidgets.QScrollArea(self.centralwidget)
        self.table_area.setWidgetResizable(True)
        self.table_area.setObjectName("table_area")
        self.table_contents = TableContents()
        self.table_contents.setGeometry(QtCore.QRect(0, 0, 712, 175))
        self.table_contents.setObjectName("table_contents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.table_contents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.table_contents)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.table_area.setWidget(self.table_contents)
        self.gridLayout.addWidget(self.table_area, 2, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 1, 0, 1, 1)
        self.head = Head(self.centralwidget)
        self.head.setObjectName("head")
        self.gridLayout.addWidget(self.head, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TimeManager"))

from head import Head
from tablecontents import TableContents
