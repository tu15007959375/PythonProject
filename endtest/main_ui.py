# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainDlg(object):
    def setupUi(self, MainDlg):
        MainDlg.setObjectName("MainDlg")
        MainDlg.resize(555, 600)
        self.tableWidget = QtWidgets.QTableWidget(MainDlg)
        self.tableWidget.setGeometry(QtCore.QRect(20, 80, 301, 501))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.layoutWidget = QtWidgets.QWidget(MainDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(350, 50, 166, 529))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MethodComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.MethodComboBox.setStyleSheet("QComboBox{border:1px solid rgb(204,204,204);border-radius:3px;height:28px;}")
        self.MethodComboBox.setObjectName("MethodComboBox")
        self.MethodComboBox.addItem("")
        self.MethodComboBox.addItem("")
        self.MethodComboBox.addItem("")
        self.MethodComboBox.addItem("")
        self.verticalLayout.addWidget(self.MethodComboBox)
        self.SearchButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchButton.sizePolicy().hasHeightForWidth())
        self.SearchButton.setSizePolicy(sizePolicy)
        self.SearchButton.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgba(255, 255, 255, 0);\n"
"border-radius: 8px;\n"
"width:150px;\n"
"height:50px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 16px;\n"
"color:rgb(255, 255, 255);\n"
"border: 5px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(199, 255, 255);\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    \n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:40px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:20px;\n"
"}\n"
"")
        self.SearchButton.setObjectName("SearchButton")
        self.verticalLayout.addWidget(self.SearchButton)
        self.CloudButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloudButton.sizePolicy().hasHeightForWidth())
        self.CloudButton.setSizePolicy(sizePolicy)
        self.CloudButton.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgba(255, 255, 255, 0);\n"
"border-radius: 8px;\n"
"width:150px;\n"
"height:50px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 16px;\n"
"\n"
"color:rgb(255, 255, 255);\n"
"border: 5px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(199, 255, 255);\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    \n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:40px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:20px;\n"
"}\n"
"")
        self.CloudButton.setObjectName("CloudButton")
        self.verticalLayout.addWidget(self.CloudButton)
        self.ScrapyViewButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScrapyViewButton.sizePolicy().hasHeightForWidth())
        self.ScrapyViewButton.setSizePolicy(sizePolicy)
        self.ScrapyViewButton.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgba(255, 255, 255, 0);\n"
"border-radius: 8px;\n"
"width:150px;\n"
"height:50px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 16px;\n"
"\n"
"color:rgb(255, 255, 255);\n"
"border: 5px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(199, 255, 255);\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    \n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:40px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:20px;\n"
"}\n"
"")
        self.ScrapyViewButton.setObjectName("ScrapyViewButton")
        self.verticalLayout.addWidget(self.ScrapyViewButton)
        self.DataButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataButton.sizePolicy().hasHeightForWidth())
        self.DataButton.setSizePolicy(sizePolicy)
        self.DataButton.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgba(255, 255, 255, 0);\n"
"border-radius: 8px;\n"
"\n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 16px;\n"
"width:150px;\n"
"height:50px;\n"
"color:rgb(255, 255, 255);\n"
"border: 5px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(199, 255, 255);\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    \n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:40px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:20px;\n"
"}\n"
"")
        self.DataButton.setObjectName("DataButton")
        self.verticalLayout.addWidget(self.DataButton)
        self.HistoryButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HistoryButton.sizePolicy().hasHeightForWidth())
        self.HistoryButton.setSizePolicy(sizePolicy)
        self.HistoryButton.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgba(255, 255, 255, 0);\n"
"border-radius: 8px;\n"
"width:150px;\n"
"height:50px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 16px;\n"
"\n"
"color:rgb(255, 255, 255);\n"
"border: 5px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(199, 255, 255);\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    \n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:40px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:20px;\n"
"}\n"
"")
        self.HistoryButton.setObjectName("HistoryButton")
        self.verticalLayout.addWidget(self.HistoryButton)
        self.ExitButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ExitButton.sizePolicy().hasHeightForWidth())
        self.ExitButton.setSizePolicy(sizePolicy)
        self.ExitButton.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgba(255, 255, 255, 0);\n"
"border-radius: 8px;\n"
"width:150px;\n"
"height:50px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 16px;\n"
"\n"
"color:rgb(255, 255, 255);\n"
"border: 5px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(199, 255, 255);\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    \n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:40px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:20px;\n"
"}\n"
"")
        self.ExitButton.setObjectName("ExitButton")
        self.verticalLayout.addWidget(self.ExitButton)
        self.idlabel = QtWidgets.QLabel(MainDlg)
        self.idlabel.setGeometry(QtCore.QRect(601, 30, 151, 51))
        self.idlabel.setStyleSheet("font-size:20px;")
        self.idlabel.setText("")
        self.idlabel.setObjectName("idlabel")
        self.calendarWidget = QtWidgets.QCalendarWidget(MainDlg)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 80, 296, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        self.layoutWidget1 = QtWidgets.QWidget(MainDlg)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 50, 301, 26))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.StartDateEdit = QtWidgets.QDateEdit(self.layoutWidget1)
        self.StartDateEdit.setObjectName("StartDateEdit")
        self.horizontalLayout.addWidget(self.StartDateEdit)
        self.EndDateEdit = QtWidgets.QDateEdit(self.layoutWidget1)
        self.EndDateEdit.setObjectName("EndDateEdit")
        self.horizontalLayout.addWidget(self.EndDateEdit)
        self.groupBox = QtWidgets.QGroupBox(MainDlg)
        self.groupBox.setGeometry(QtCore.QRect(349, 10, 171, 31))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.IDlabel = QtWidgets.QLabel(self.groupBox)
        self.IDlabel.setGeometry(QtCore.QRect(20, 10, 141, 16))
        self.IDlabel.setObjectName("IDlabel")

        self.retranslateUi(MainDlg)
        QtCore.QMetaObject.connectSlotsByName(MainDlg)

    def retranslateUi(self, MainDlg):
        _translate = QtCore.QCoreApplication.translate
        MainDlg.setWindowTitle(_translate("MainDlg", "Dialog"))
        self.MethodComboBox.setItemText(0, _translate("MainDlg", "thulac"))
        self.MethodComboBox.setItemText(1, _translate("MainDlg", "pkuseg"))
        self.MethodComboBox.setItemText(2, _translate("MainDlg", "jieba"))
        self.MethodComboBox.setItemText(3, _translate("MainDlg", "snowlp"))
        self.SearchButton.setText(_translate("MainDlg", "词频提取"))
        self.CloudButton.setText(_translate("MainDlg", "生成词云"))
        self.ScrapyViewButton.setText(_translate("MainDlg", "图表展示"))
        self.DataButton.setText(_translate("MainDlg", "数据查看"))
        self.HistoryButton.setText(_translate("MainDlg", "操作历史"))
        self.ExitButton.setText(_translate("MainDlg", "退出"))
        self.IDlabel.setText(_translate("MainDlg", "用户名"))