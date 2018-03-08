# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_table(object):
    def setupUi(self, table):
        table.setObjectName("table")
        table.resize(700, 72)
        table.setMinimumSize(QtCore.QSize(700, 0))
        self.gridLayout = QtWidgets.QGridLayout(table)
        self.gridLayout.setObjectName("gridLayout")
        self.lesson = QtWidgets.QLineEdit(table)
        self.lesson.setText("")
        self.lesson.setObjectName("lesson")
        self.gridLayout.addWidget(self.lesson, 0, 1, 1, 1)
        self.deadline = QtWidgets.QDateEdit(table)
        self.deadline.setEnabled(False)
        self.deadline.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 9, 1), QtCore.QTime(0, 0, 0)))
        self.deadline.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2017, 9, 1), QtCore.QTime(0, 0, 0)))
        self.deadline.setObjectName("deadline")
        self.gridLayout.addWidget(self.deadline, 0, 3, 1, 1)
        self.buttons_layout = QtWidgets.QVBoxLayout()
        self.buttons_layout.setObjectName("buttons_layout")
        self.teach = QtWidgets.QPushButton(table)
        self.teach.setEnabled(False)
        self.teach.setObjectName("teach")
        self.buttons_layout.addWidget(self.teach)
        self.delete_2 = QtWidgets.QPushButton(table)
        self.delete_2.setObjectName("delete_2")
        self.buttons_layout.addWidget(self.delete_2)
        self.gridLayout.addLayout(self.buttons_layout, 0, 5, 1, 1)
        self.result = QtWidgets.QDoubleSpinBox(table)
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 0, 4, 1, 1)
        self.done = QtWidgets.QCheckBox(table)
        self.done.setText("")
        self.done.setObjectName("done")
        self.gridLayout.addWidget(self.done, 0, 0, 1, 1)

        self.retranslateUi(table)
        QtCore.QMetaObject.connectSlotsByName(table)
        table.setTabOrder(self.done, self.lesson)
        table.setTabOrder(self.lesson, self.deadline)
        table.setTabOrder(self.deadline, self.result)
        table.setTabOrder(self.result, self.teach)
        table.setTabOrder(self.teach, self.delete_2)

    def retranslateUi(self, table):
        _translate = QtCore.QCoreApplication.translate
        table.setWindowTitle(_translate("table", "Form"))
        self.lesson.setToolTip(_translate("table", "Описание предмета"))
        self.deadline.setToolTip(_translate("table", "Дата окончания"))
        self.teach.setText(_translate("table", "Обучить"))
        self.delete_2.setText(_translate("table", "Удалить"))
        self.result.setToolTip(_translate("table", "Результат"))
        self.done.setToolTip(_translate("table", "Задача выполнена"))

