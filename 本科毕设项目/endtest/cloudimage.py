# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cloudimage.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cloudDialog(object):
    def setupUi(self, cloudDialog):
        cloudDialog.setObjectName("cloudDialog")
        cloudDialog.resize(500, 440)
        self.label = QtWidgets.QLabel(cloudDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 461, 401))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(cloudDialog)
        QtCore.QMetaObject.connectSlotsByName(cloudDialog)

    def retranslateUi(self, cloudDialog):
        _translate = QtCore.QCoreApplication.translate
        cloudDialog.setWindowTitle(_translate("cloudDialog", "Dialog"))
