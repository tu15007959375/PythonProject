# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(547, 578)
        self.layoutWidget = QtWidgets.QWidget(AboutDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 40, 452, 501))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("font-size:30px;\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font-size:30px;\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("font-size:30px;\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("font-size:30px;\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.ExitButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ExitButton.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgba(255, 255, 255, 0);\n"
"border-radius: 8px;\n"
"padding: 16px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 16px;\n"
"margin: 4px 2px;\n"
"color:rgb(255, 255, 255);\n"
"border: 5px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    /*????????????*/  \n"
"    background-color:rgb(199, 255, 255);\n"
"}\n"
" \n"
"/*???????????????*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*????????????*/  \n"
"    \n"
"    /*???????????????3????????????????????????????????????3??????*/  \n"
"    padding-left:40px;\n"
"    /*???????????????3????????????????????????????????????3??????*/  \n"
"    padding-top:20px;\n"
"}\n"
"")
        self.ExitButton.setObjectName("ExitButton")
        self.verticalLayout.addWidget(self.ExitButton)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "Dialog"))
        self.label.setText(_translate("AboutDialog", "??????????????????"))
        self.label_2.setText(_translate("AboutDialog", "??????:8002118264"))
        self.label_3.setText(_translate("AboutDialog", "?????????????????????????????????????????????"))
        self.label_4.setText(_translate("AboutDialog", "?????????1.0.0"))
        self.ExitButton.setText(_translate("AboutDialog", "??????"))
