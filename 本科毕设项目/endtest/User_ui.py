# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserDialog(object):
    def setupUi(self, UserDialog):
        UserDialog.setObjectName("UserDialog")
        UserDialog.resize(559, 365)
        self.widget = QtWidgets.QWidget(UserDialog)
        self.widget.setGeometry(QtCore.QRect(11, 11, 531, 331))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.delButton = QtWidgets.QPushButton(self.widget)
        self.delButton.setObjectName("delButton")
        self.verticalLayout.addWidget(self.delButton)
        self.addButton = QtWidgets.QPushButton(self.widget)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)
        self.backButton = QtWidgets.QPushButton(self.widget)
        self.backButton.setObjectName("backButton")
        self.verticalLayout.addWidget(self.backButton)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(UserDialog)
        QtCore.QMetaObject.connectSlotsByName(UserDialog)

    def retranslateUi(self, UserDialog):
        _translate = QtCore.QCoreApplication.translate
        UserDialog.setWindowTitle(_translate("UserDialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("UserDialog", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("UserDialog", "??????"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("UserDialog", "??????"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("UserDialog", "??????"))
        self.delButton.setText(_translate("UserDialog", "????????????"))
        self.addButton.setText(_translate("UserDialog", "????????????"))
        self.backButton.setText(_translate("UserDialog", "??????"))
