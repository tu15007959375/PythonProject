import csv
import os
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import Qt, pyqtSignal, QTimer, QDate, QUrl, QFileInfo, QCoreApplication, QDir, QRect
import re

from PyQt5.QtGui import QDesktopServices, QCursor
import MD5
import datetime
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Login_ui import *
from About_ui import Ui_AboutDialog
from Register_ui import Ui_RegisterDialog
from endtest.User_ui import Ui_UserDialog
from endtest.alterpassword_ui import Ui_alterDialog
from endtest.cloudimage import Ui_cloudDialog
from endtest.data_ui import Ui_DataDialog
from endtest.history_ui import Ui_HistoryDialog
from endtest.scrapy_ui import Ui_ScrapyDialog
from information_ui import Ui_InformationDialog
from main_ui import *
from PyQt5.QtWidgets import *
import sys
import util
from PyQt5.QtCore import QSettings
from dataprocess import wordsegment
from dataprocess import charts
from dataprocess import cloudimage
import warnings

warnings.filterwarnings("ignore")


class LoginWidow(Ui_LoginWidow, QtWidgets.QMainWindow):
    user = [0] * 6
    autologin = 0
    app_data = None  # 设置配置文件的全局变量

    def __init__(self):

        super(Ui_LoginWidow, self).__init__()
        self.setupUi(self)
        self.LoginButton.setShortcut('enter')
        self.timer = QTimer(self)
        # 初始化信号函数
        self.init_connect()
        self.init_config()
        self.setObjectName("登录")
        self.setWindowTitle("登录")
        self.setStyleSheet("#登录{border-image:url(resources//back//back.jpeg)}")

    def init_connect(self):
        # 初始化信号与槽
        self.LoginButton.clicked.connect(self.check)
        self.AboutButton.clicked.connect(self.about_window)
        self.RegisterButton.clicked.connect(self.register_window)
        self.AutoLoginCheckBox.setChecked(False)
        self.AutoLoginCheckBox.stateChanged.connect(self.set_remeber_check)
        # 实现自动登陆
        self.timer.timeout.connect(self.login)
        self.timer.setSingleShot(True)
        self.timer.start(100)

    # 初始化配置文件
    def init_config(self):
        if os.path.exists('./config.ini'):
            appdata = QSettings('config.ini', QSettings.IniFormat)
            appdata.setIniCodec('UTF-8')
            self.user[0] = appdata.value('id')
            self.user[1] = appdata.value('password')
            self.user[2] = appdata.value('tag')
            self.autologin = appdata.value('autologin')
            self.IdEdit.setText(self.user[0])
            self.PassEdit.setText(self.user[1])
            if int(self.autologin) == 1:
                self.AutoLoginCheckBox.setChecked(True)
            else:
                self.RemebercheckBox.setChecked(True)

    # 自动登陆绑定函数
    def login(self):
        if self.AutoLoginCheckBox.isChecked():
            self.check(1)

    # 登录检测函数
    def check(self, auto=0):
        conn = util.get_conn(conn='Admin')
        userlist = []
        for user in conn.find():
            userlist.append(user)

        # 非空检测
        if self.IdEdit.text() == "" or self.PassEdit.text() == "":
            QMessageBox.information(self, '提示', '账号或者密码不能为空')
            return
        if auto == 0:
            for x in userlist:

                if self.IdEdit.text() == x['_id'] and MD5.create_md5(self.PassEdit.text(), x['salt']) == x['password']:
                    QMessageBox.information(self, '提示', '登录成功')
                    loginw.user[1] = MD5.create_md5(self.PassEdit.text(), x['salt'])
                    self.set_user(x)
                    self.initdata()
                    # 打开主界面
                    loginw.close()
                    mainw.inituser()
                    mainw.show()
                    return
                if self.IdEdit.text() == x['_id'] and self.user[1] == x['password']:
                    QMessageBox.information(self, '提示', '登录成功')
                    self.set_user(x)
                    self.initdata()
                    # 打开主界面
                    loginw.close()
                    mainw.inituser()
                    mainw.show()
                    return
        elif auto == 1:
            for x in userlist:

                if self.user[0] == x['_id'] and self.user[1] == x['password']:
                    QMessageBox.information(self, '提示', '登录成功')
                    self.set_user(x)
                    # 打开主界面
                    self.initdata()
                    loginw.close()
                    mainw.inituser()
                    mainw.show()
                    return
        QMessageBox.information(self, '提示', '账号密码不匹配')
        self.IdEdit.setText('')
        self.PassEdit.setText('')

    def initdata(self):
        if loginw.AutoLoginCheckBox.isChecked():
            self.autologin = 1
        else:
            self.autologin = 0
        if loginw.RemebercheckBox.isChecked():
            self.save_info()
        else:
            if os.path.exists('config.ini'):
                os.remove('config.ini')

    def save_info(self):
        if os.path.exists('config.ini'):
            os.remove('config.ini')
        self.app_data = QSettings('config.ini', QSettings.IniFormat)
        self.app_data.setIniCodec('UTF-8')
        self.app_data.setValue('id', self.user[0])
        self.app_data.setValue('password', self.user[1])
        self.app_data.setValue('tag', self.user[2])
        self.app_data.setValue('autologin', self.autologin)

    def set_user(self, x):
        loginw.user[0] = self.IdEdit.text()
        loginw.user[2] = int(x['tag'])
        loginw.user[3] = x['nick']
        loginw.user[4] = x['sex']
        loginw.user[5] = x['salt']

    def set_remeber_check(self):
        self.RemebercheckBox.setChecked(True)

    def about_window(self):
        aboutw.show()

    def register_window(self):
        util.save_history('', '', '', '', '注册')
        registerw.show()


# 主界面，显示信息，继承main_ui实现自定义信号和槽
class MainWindow(Ui_MainDlg, QtWidgets.QDialog):
    userid = 0
    userpwd = 0
    usertag = 1

    def __init__(self):
        super(Ui_MainDlg, self).__init__()
        # 设置右键菜单
        self.actionB = QAction(u'退出登录', self)
        self.actionA = QAction(u'个人信息', self)
        self.actionC = QAction(u'用户管理', self)
        self.groupBox_menu = QMenu(self)
        self.setupUi(self)
        # 声明在groupBox创建右键菜单
        self.groupBox.setContextMenuPolicy(Qt.CustomContextMenu)
        self.groupBox.customContextMenuRequested.connect(self.create_rightmenu)  # 连接到菜单显示函数
        self.groupBox_menu.addAction(self.actionA)  # 把动作A选项添加到菜单
        self.groupBox_menu.addAction(self.actionB)
        self.groupBox_menu.addAction(self.actionC)
        self.setObjectName("主窗口")
        self.setWindowTitle("主窗口")
        self.setStyleSheet("#主窗口{border-image:url(resources//back//back.jpeg)}")
        # 初始化组件
        self.initConnect()
        self.initTableWidget()
        self.orderType = Qt.AscendingOrder
        # 日期设置
        self.StartDateEdit.setDate(QDate(2022, 3, 1))
        self.EndDateEdit.setDate(QDate(2022, 3, 31))
        self.StartDateEdit.setDisplayFormat('yyyy-MM-dd')
        self.EndDateEdit.setDisplayFormat('yyyy-MM-dd')
        self.StartDateEdit.setCalendarPopup(True)
        self.EndDateEdit.setCalendarPopup(True)
        self.calendarWidget.setVisible(False)

    # 初始化信号与槽
    def initConnect(self):
        self.SearchButton.clicked.connect(self.search)
        self.ScrapyViewButton.clicked.connect(self.scrapy)
        self.ExitButton.clicked.connect(self.exit)
        self.CloudButton.clicked.connect(self.cloud)
        self.HistoryButton.clicked.connect(self.history)
        self.DataButton.clicked.connect(self.datashow)
        self.MethodComboBox.currentIndexChanged.connect(self.search)
        self.actionA.triggered.connect(self.information)  # 将动作A触发时连接到槽函数 button
        self.actionB.triggered.connect(self.backtologin)
        self.actionC.triggered.connect(self.usermanager)

    def initTableWidget(self):
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setHorizontalHeaderLabels(['热点词', '出现次数'])
        self.tableWidget.scrollToTop()
        # 设置只能选中一行
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 不可编辑
        self.tableWidget.setEditTriggers(QTableView.NoEditTriggers)
        # 列宽自动分配
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    # 展示数据到表格上
    def flesh(self, method, starttime, endtime):
        if method == 'pkuseg':
            countdict = wordsegment.get_pkuseg(starttime, endtime)
        elif method == 'thulac':
            countdict = wordsegment.get_thulac(starttime, endtime)
        elif method == 'jieba':
            countdict = wordsegment.get_jieba(starttime, endtime)
        elif method == 'snowlp':
            countdict = wordsegment.get_snowlp(starttime, endtime)

        namelist = []
        countlist = []
        for k, v in countdict.items():
            namelist.append(k)
            countlist.append(v)
        n = len(countdict)

        self.tableWidget.setRowCount(n)
        for i in range(n):
            item1 = QTableWidgetItem(str(namelist[i]))
            item2 = QTableWidgetItem(str(countlist[i]))
            self.tableWidget.setItem(i, 0, item1)
            self.tableWidget.setItem(i, 1, item2)
        self.tableWidget.update()

    def inituser(self):
        self.userid = loginw.user[0]
        self.userpwd = loginw.user[1]
        self.usertag = loginw.user[2]
        self.IDlabel.setText('用户:' + str(loginw.user[0]))

    def search(self):
        starttime = self.StartDateEdit.date().toString(Qt.ISODate)
        endtime = self.EndDateEdit.date().toString(Qt.ISODate)
        self.flesh(self.MethodComboBox.currentText(), starttime, endtime)
        util.save_history(self.userid, self.MethodComboBox.currentText(), starttime, endtime, '热点提取')

    def cloud(self):
        QMessageBox.information(self, '提示', '正在生成，请稍后')
        method = self.MethodComboBox.currentText()
        image = None
        starttime = self.StartDateEdit.date().toString(Qt.ISODate)
        endtime = self.EndDateEdit.date().toString(Qt.ISODate)
        util.save_history(self.userid, method, starttime, endtime, '提取词云')
        path1 = 'resources/cloud/'
        path2 = starttime + '_' + endtime + '.jpg'
        if method == 'pkuseg':
            cloudimage.pku_seg_cloud(starttime, endtime)
            image = QtGui.QPixmap(path1 + 'pkusegcloud' + path2)
        elif method == 'thulac':
            cloudimage.thulac_seg_cloud(starttime, endtime)
            image = QtGui.QPixmap(path1 + 'thulaccloud' + path2)
        elif method == 'jieba':
            cloudimage.jieba_seg_cloud(starttime, endtime)
            image = QtGui.QPixmap(path1 + 'jiebacloud' + path2)
        elif method == 'snowlp':
            cloudimage.snowlp_seg_cloud(starttime, endtime)
            image = QtGui.QPixmap(path1 + 'snowlpcloud' + path2)

        cloudw.label.setPixmap(image)
        cloudw.label.setScaledContents(True)
        cloudw.show()

    def scrapy(self):
        method = self.MethodComboBox.currentText()
        starttime = self.StartDateEdit.date().toString(Qt.ISODate)
        endtime = self.EndDateEdit.date().toString(Qt.ISODate)
        util.save_history(self.userid, method, starttime, endtime, '图表展示')
        scrapyw.show()

    def exit(self):
        QCoreApplication.instance().quit()

    def history(self):
        if self.usertag == 0:

            historyw.flesh()
            historyw.show()
        else:
            QMessageBox.information(self, '提示', '你不是管理员，不能进入该页面')

    def datashow(self):
        util.save_history(self.userid, '', '', '', '数据展示')
        dataw.show()

    # 创建右键菜单函数
    def create_rightmenu(self):
        # 菜单对象

        self.groupBox_menu.popup(QCursor.pos())  # 声明当鼠标在groupBox控件上右击时，在鼠标位置显示右键菜单   ,exec_,popup两个都可以，

    def backtologin(self):
        util.save_history(mainw.userid, '', '', '', '退出登陆')
        self.close()
        loginw.IdEdit.setText('')
        loginw.PassEdit.setText('')
        loginw.AutoLoginCheckBox.setChecked(False)
        loginw.RemebercheckBox.setChecked(False)
        loginw.show()

    def information(self):
        util.save_history(mainw.userid, '', '', '', '查看个人信息')
        informationw.initlabel()
        informationw.show()

    def usermanager(self):
        if self.usertag != 0:
            QMessageBox.information(self, '提示', '你不是管理员，不能进入该页面')
        else:
            userw.show()


# 图表展示
class ScrapyWindow(Ui_ScrapyDialog, QtWidgets.QDialog):

    def __init__(self):
        super(Ui_ScrapyDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('图表展示')
        self.setObjectName("图表展示")
        self.setStyleSheet("#图表展示{border-image:url(resources//back//back.jpeg)}")
        self.view = QWebEngineView(self)
        self.view.setGeometry(0, 0, 900, 700)
        self.getchart()
        self.initConnect()

    def initConnect(self):
        self.comboBox.currentIndexChanged.connect(self.switch)
        self.backButton.clicked.connect(self.back)

    def getchart(self):
        charts.get_all()
        self.loadhtml("resources/echarts/topo.html")

    def loadhtml(self, path):
        self.view.load(QUrl(QFileInfo(path).absoluteFilePath()))
        self.view.show()

    def switch(self):
        index = self.comboBox.currentIndex()
        path = 'resources/echarts/'
        if index == 0:
            # 加载外部的web页面
            util.save_history(mainw.userid, '', '', '', '查看拓扑图')
            charts.get_relation_topo()
            self.loadhtml(path + "topo.html")
        elif index == 1:
            # 加载外部的web页面
            util.save_history(mainw.userid, '', '', '', '查看柱状图')
            charts.get_count_barchart()
            self.loadhtml(path + "contentscountbar.html")
        elif index == 2:
            util.save_history(mainw.userid, '', '', '', '查看饼状图')
            charts.get_count_piechart()
            self.loadhtml(path + "contentscountpie.html")
        elif index == 3:
            util.save_history(mainw.userid, '', '', '', '查看jiebaLDA图')
            # wordsegment.getgensimlda('jieba', starttime, endtime)
            self.label.setText('一致度：0.434')
            self.loadhtml('resources/lda/jiebamallet_0.434.html')
        elif index == 4:
            util.save_history(mainw.userid, '', '', '', '查看thulacLDA图')
            self.label.setText('一致度：0.478')
            # wordsegment.getgensimlda('thulac', starttime, endtime)
            self.loadhtml('resources/lda/thulacmallet_0.478.html')
        elif index == 5:
            util.save_history(mainw.userid, '', '', '', '查看pkusegLDA图')
            self.label.setText('一致度：0.493')
            # wordsegment.getgensimlda('pkuseg', starttime, endtime)
            self.loadhtml('resources/lda/pkusegmallet_0.493.html')
        elif index == 6:
            util.save_history(mainw.userid, '', '', '', '查看snowlpLDA图')
            self.label.setText('一致度：0.479')
            # wordsegment.getgensimlda('snowlp', starttime, endtime)
            self.loadhtml('resources/lda/snowlpmallet_0.479.html')

    def back(self):
        self.close()


# 操作历史界面
class HistoryWindow(Ui_HistoryDialog, QtWidgets.QDialog):

    def __init__(self):
        super(Ui_HistoryDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('历史记录')
        self.setObjectName("历史记录")
        self.setStyleSheet("#历史记录{border-image:url(resources//back//back.jpeg)}")
        self.initConnect()

    def initConnect(self):
        # 初始化信号与槽
        self.clearButton.clicked.connect(self.clear)
        self.backButton.clicked.connect(self.back)
        self.importButton.clicked.connect(self.importfile)
        self.exportButton.clicked.connect(self.exportfile)
        pass

    def flesh(self):
        self.listWidget.clear()
        finlist = util.read_csv_to_list('resources/history/history.csv')
        self.listWidget.addItems(finlist)

    def importfile(self):
        dig = QFileDialog()
        # 设置可以打开任何文件
        dig.setFileMode(QFileDialog.AnyFile)
        # 文件过滤
        dig.setFilter(QDir.Files)

        if dig.exec_():
            # 接受选中文件的路径，默认为列表
            filenames = dig.selectedFiles()
            # 列表中的第一个元素即是文件路径，以只读的方式打开文件

            finlist = util.read_csv_to_list(filenames[0])
            self.listWidget.addItems(finlist)
            util.write_list_to_csv(finlist, 'resources/history/history.csv')
        QMessageBox.information(self, '提示', '导入成功')

    def exportfile(self):
        filename = QFileDialog.getSaveFileName(self, '选择保存路径', 'D:/', 'txt(*.txt)')
        util.write_list_to_csv(util.read_csv_to_list('resources/history/history.csv'), filename[0])
        QMessageBox.information(self, '提示', '导出成功')

    # 清除历史
    def clear(self):
        self.listWidget.clear()
        f = open('resources/history/history.csv', 'w', encoding='utf-8-sig', newline="")
        f.close()
        pass

    def back(self):
        self.close()


# 用户管理界面
class UserWindow(Ui_UserDialog, QtWidgets.QDialog):
    userlist = []
    db_qt_dict = {0: '_id', 1: 'tag', 2: 'nick', 3: 'sex'}
    nochange = 0

    def __init__(self):
        super(Ui_UserDialog, self).__init__()
        self.setupUi(self)
        self.setObjectName("用户管理")
        self.setWindowTitle("用户管理")
        self.setStyleSheet("#用户管理{border-image:url(resources//back//back.jpeg)}")
        self.inittablewidget()
        self.flesh()
        # 初始化信号函数
        self.initConnect()

    def initConnect(self):
        # 初始化信号与槽
        self.backButton.clicked.connect(self.close)
        self.addButton.clicked.connect(self.add)
        self.delButton.clicked.connect(self.deluser)
        self.tableWidget.itemChanged.connect(self.updateuser)
        self.tableWidget.doubleClicked.connect(self.setchange)

    def inittablewidget(self):
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.scrollToTop()
        # 设置只能选中一行
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 列宽自动分配
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def flesh(self):
        self.nochange = 1
        self.userlist = util.get_userlist()
        n = len(self.userlist)
        self.tableWidget.setRowCount(n)
        for i in range(n):
            li = self.userlist[i].split('!@')
            self.tableWidget.setItem(i, 0, QTableWidgetItem(li[0]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(li[1]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(li[2]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(li[3]))
        self.tableWidget.update()

    def add(self):
        registerw.setObjectName("添加用户")
        registerw.setWindowTitle("添加用户")
        registerw.setStyleSheet("#添加用户{border-image:url(resources//back//back.jpeg)}")
        registerw.show()

    def deluser(self):
        row = self.tableWidget.currentRow()
        uid = self.tableWidget.item(row, 0).text()
        conn = util.get_conn(conn='Admin')
        conn.delete_one({'_id': uid})
        self.tableWidget.removeRow(row)
        self.flesh()
        QMessageBox.information(self, '提示', '删除成功')

    def updateuser(self):
        if self.nochange == 1:
            return
        col = self.tableWidget.currentColumn()
        row = self.tableWidget.currentRow()
        newtext = self.tableWidget.item(row, col).text()
        conn = util.get_conn(conn='Admin')
        preuid = self.userlist[row].split('!@')[0]
        myquery = {'_id': preuid}
        newvalues = {'$set': {self.db_qt_dict[col]: newtext}}
        if col != 0:
            conn.update_one(myquery, newvalues)
            QMessageBox.information(self, '提示', '修改成功')
            self.nochange = 1
            return
        else:
            uidlist = []
            for li in self.userlist:
                uidlist.append(li.split('!@')[0])
            if newtext in uidlist:
                QMessageBox.information(self, '提示', '该uid已经存在，请重新修改')
                self.nochange = 1
                self.tableWidget.item(row, col).setText(preuid)
                return
            else:
                conn.update_one(myquery, newvalues)
                QMessageBox.information(self, '提示', '修改成功')
                return

    def setchange(self):
        self.nochange = 0


# 关于界面

class AboutWidow(Ui_AboutDialog, QtWidgets.QDialog):
    def __init__(self):
        super(Ui_AboutDialog, self).__init__()
        self.setupUi(self)
        self.setObjectName("关于")
        self.setWindowTitle("关于")
        self.setStyleSheet("#关于{border-image:url(resources//back//back.jpeg)}")
        # 初始化信号函数
        self.initConnect()

    def initConnect(self):
        # 初始化信号与槽
        self.ExitButton.clicked.connect(self.close)

    def back(self):
        aboutw.close()


# 个人信息界面
class InformationWidow(Ui_InformationDialog, QtWidgets.QDialog):
    def __init__(self):
        super(Ui_InformationDialog, self).__init__()
        self.setupUi(self)
        self.setObjectName("信息")
        self.setWindowTitle("信息")
        self.setStyleSheet("#信息{border-image:url(resources//back//back.jpeg)}")
        # 初始化信号函数
        self.initConnect()

    def initConnect(self):
        # 初始化信号与槽
        self.ConcelButton.clicked.connect(self.close)
        self.alterButton.clicked.connect(self.alter)

    def initlabel(self):
        self.IdLabel.setText(loginw.user[0])
        self.sexlabel.setText(loginw.user[4])
        self.nicklabel.setText(loginw.user[3])

    def alter(self):
        util.save_history(mainw.userid, '', '', '', '修改密码')
        alterpasswordw.IdLabel.setText(str(loginw.user[0]))
        alterpasswordw.show()


# 注册
class RegisterWindow(Ui_RegisterDialog, QtWidgets.QDialog):
    def __init__(self):
        super(Ui_RegisterDialog, self).__init__()
        self.setupUi(self)
        self.setObjectName("注册")
        self.setWindowTitle("注册")
        self.setStyleSheet("#注册{border-image:url(resources//back//back.jpeg)}")
        # 初始化信号函数
        self.initConnect()

    def initConnect(self):
        # 初始化信号与槽
        self.ConcealButton.clicked.connect(self.close)
        self.OKButton.clicked.connect(self.check)
        pass

    def settextnull(self):
        self.IdEdit.setText('')
        self.PassEdit.setText('')
        self.TwoPassEdit_2.setText('')
        self.sexEdit.setText('')
        self.nickEdit.setText('')

    def check(self):

        # 非空检测
        if self.IdEdit.text() == "" or self.PassEdit.text() == "" or self.TwoPassEdit_2.text() == "":
            QMessageBox.information(self, '提示', '账号或者密码不能为空，请重新输入')
            util.save_history('', '', '', '', '注册失败')
            self.settextnull()
            return
        if self.sexEdit.text() == "":
            QMessageBox.information(self, '提示', '性别不能为空，请重新输入')
            util.save_history('', '', '', '', '注册失败')
            self.settextnull()
            return
        if self.nickEdit.text() == "":
            QMessageBox.information(self, '提示', '昵称不能为空，请重新输入')
            util.save_history('', '', '', '', '注册失败')
            self.settextnull()
            return
        # 正则检测只能为数字
        pattern = re.compile('^[0-9]*$')
        if not re.match(pattern, self.IdEdit.text()) or not re.match(pattern, self.PassEdit.text()) or not \
                re.match(pattern, self.TwoPassEdit_2.text()):
            self.settextnull()
            QMessageBox.information(self, '提示', '只能输入数字，请重新输入')
            util.save_history('', '', '', '', '注册失败')
            return

        if self.PassEdit.text() != self.TwoPassEdit_2.text():
            QMessageBox.information(self, '提示', '密码不一致，请重新输入')
            util.save_history('', '', '', '', '注册失败')
            self.settextnull()
            return

        conn = util.get_conn(conn='Admin')
        userlist = []
        for user in conn.find():
            userlist.append(user)
        for li in userlist:
            if li['_id'] == self.IdEdit.text():
                QMessageBox.information(self, '提示', '用户ID已经存在!')
                util.save_history('', '', '', '', '注册失败')
                self.settextnull()
                return
        salt = MD5.create_salt()
        password = MD5.create_md5(self.PassEdit.text(), salt)
        registeruser = {'_id': self.IdEdit.text(), 'password': password, 'tag': 1, 'salt': salt,
                        'nick': self.nickEdit.text(), 'sex': self.sexEdit.text()}

        conn.insert_one(registeruser)
        util.save_history('', '', '', '', '注册成功')
        QMessageBox.information(self, '提示', '注册成功')
        userw.flesh()
        self.settextnull()
        self.close()


# 生成词云
class CloudWindow(Ui_cloudDialog, QtWidgets.QDialog):
    def __init__(self):
        super(Ui_cloudDialog, self).__init__()
        self.setupUi(self)
        self.setObjectName("词云")
        self.setWindowTitle("词云")
        # 初始化信号函数
        self.initConnect()

    def initConnect(self):
        pass


# 信息展示
class DataWindow(Ui_DataDialog, QtWidgets.QDialog):
    datadict = {}
    searchdict = {}
    idnamedict = {}
    allpage = 1
    nowpage = 1
    rowcount = 30
    content = ''

    def __init__(self):
        super(Ui_DataDialog, self).__init__()
        self.setupUi(self)
        self.setObjectName("数据展示")
        self.setWindowTitle("数据展示")
        self.setStyleSheet("#数据展示{border-image:url(resources//back//back.jpeg)}")
        self.tableWidget.scrollToTop()

        # 不可编辑
        self.tableWidget.setEditTriggers(QTableView.NoEditTriggers)
        # 设置列宽
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 550)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 350)
        self.tableWidget.setRowCount(self.rowcount)
        self.idnamedict = util.get_id_name_dict()
        # 初始化信号函数
        self.init_connect()
        self.init_content()

    def init_connect(self):
        self.PreDataButton.clicked.connect(self.init_content)
        self.NewDataButton.clicked.connect(self.new_content)
        self.NextPageButton.clicked.connect(self.next_page)
        self.PrePageButton.clicked.connect(self.pre_page)
        self.FirstPageButton.clicked.connect(self.first_page)
        self.LastPageButton.clicked.connect(self.last_page)
        self.EnterPageButton.clicked.connect(self.enter_page)
        self.searchButton.clicked.connect(self.search)
        self.tableWidget.doubleClicked.connect(self.copy)
        self.comboBox.currentIndexChanged.connect(self.new_content)

    def cal_all_page(self, n):

        # 计算总页数
        if n % 30 != 0:
            self.allpage = int(n / 30) + 1
        else:
            self.allpage = int(n / 30)
        self.AllPagelabel.setText('共' + str(self.allpage) + '页')

    def get_dict_len(self, mydict):
        n = 0
        for v in mydict.values():
            n += len(v)
        return n

    def init_content(self):
        if mainw.userid != '' and mainw.userid != 0:
            util.save_history(mainw.userid, '', '', '', '查看原始数据')

        self.content = ''
        self.datadict = util.get_infodict_from_csv('resources/datatest.csv')
        self.lineEdit_2.setText('')
        self.nowpage = 1
        self.flesh()

    def new_content(self):
        util.save_history(mainw.userid, '', '', '', '查看分词数据')
        self.content = ''
        method = self.comboBox.currentText()
        path = 'resources/datasegfile/' + method + 'seg.csv'
        self.datadict = util.get_infodict_from_csv(path)
        self.lineEdit_2.setText('')
        self.nowpage = 1
        self.flesh()

    def flesh(self, content=''):
        if content == '':
            self.add_content(self.datadict)
        else:
            for k, v in self.datadict.items():
                if content in k:
                    self.searchdict[k] = v
                    continue
                self.searchdict[k] = []
                for li in v:
                    if content in li:
                        self.searchdict[k].append(li)
            self.add_content(self.searchdict)

    def add_content(self, mydict):
        self.NowPagelabel.setText('当前第' + str(self.nowpage) + '页')
        self.tableWidget.clearContents()
        self.cal_all_page(self.get_dict_len(mydict))
        n = 0
        i = 0
        for k, v in mydict.items():
            for li in v:
                n += 1
                if n <= (self.nowpage - 1) * self.rowcount:
                    continue
                self.tableWidget.setItem(i, 3, QTableWidgetItem(str(k)))
                x = li.split('!@$')
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(x[0])))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.idnamedict.get(x[0]))))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(x[1])))
                label = QLabel()
                label.setText('<a href="' + str(x[2]) + '">' + str(x[2]) + '</a>')
                # <a href="' + x[2] + '">
                label.setOpenExternalLinks(True)
                self.tableWidget.setCellWidget(i, 4, label)
                # <a href="https://blog.csdn.net/s_daqing">
                i += 1

                if n > self.nowpage * self.rowcount:
                    break
            if n > self.nowpage * self.rowcount:
                break
        self.tableWidget.update()
        self.tableWidget.verticalScrollBar().setSliderPosition(0)

    def next_page(self):
        util.save_history(mainw.userid, '', '', '', '下一页')
        self.nowpage += 1
        if self.nowpage > self.allpage:
            self.nowpage = 1
        self.flesh(self.content)

    def pre_page(self):
        util.save_history(mainw.userid, '', '', '', '上一页')
        self.nowpage -= 1
        if self.nowpage < 1:
            self.nowpage = self.allpage
        self.flesh(self.content)

    def first_page(self):
        util.save_history(mainw.userid, '', '', '', '首页')
        self.nowpage = 1
        self.flesh(self.content)

    def last_page(self):
        util.save_history(mainw.userid, '', '', '', '尾页')
        self.nowpage = self.allpage
        self.flesh(self.content)

    def enter_page(self):

        if self.lineEdit.text().isdigit():
            page = int(self.lineEdit.text())
        else:
            page = 1
        if page < 1:
            page = 1
        elif page > self.allpage:
            page = self.allpage
        util.save_history(mainw.userid, '', '', '', '跳转到了第' + str(page) + '页')
        self.nowpage = page
        self.flesh(self.content)

    def search(self):
        util.save_history(mainw.userid, '', '', '', '搜索' + self.lineEdit_2.text())
        self.nowpage = 1
        self.content = self.lineEdit_2.text()
        self.flesh(content=self.content)

    def copy(self):
        util.save_history(mainw.userid, '', '', '', '复制')
        QApplication.clipboard().setText(self.tableWidget.selectedItems()[0].text())
        QMessageBox.information(self, '提示', '复制成功')


class AlterpasswordWindow(Ui_alterDialog, QtWidgets.QDialog):
    def __init__(self):
        super(Ui_alterDialog, self).__init__()
        self.setupUi(self)
        self.setObjectName("修改密码")
        self.setWindowTitle("修改密码")
        self.setStyleSheet("#修改密码{border-image:url(resources//back//back.jpeg)}")
        self.IdLabel.setText(str(loginw.user[0]))
        # 初始化信号函数
        self.initConnect()

    def initConnect(self):
        self.ConcelButton.clicked.connect(self.close)
        self.alterButton.clicked.connect(self.alterpassword)

    def alterpassword(self):
        prepass = self.prepassEdit.text()
        newpass = self.newpassEdit.text()
        if not prepass.isdigit():
            QMessageBox.information(self, '提示', '密码只能为数字')
            self.settextnull()
            util.save_history(mainw.userid, '', '', '', '修改密码失败')
            return
        if prepass == '' or newpass == '':
            QMessageBox.information(self, '提示', '密码不能为空')
            self.settextnull()
            util.save_history(mainw.userid, '', '', '', '修改密码失败')
            return
        if loginw.user[1] == MD5.create_md5(prepass, loginw.user[5]):
            loginw.user[1] = MD5.create_md5(newpass, loginw.user[5])
            conn = util.get_conn(conn='Admin')
            myquery = {"_id": loginw.user[0]}
            newvalues = {"$set": {"password": loginw.user[1]}}
            conn.update_one(myquery, newvalues)
            util.save_history(mainw.userid, '', '', '', '修改密码成功')
            QMessageBox.information(self, '提示', '修改成功,请重新登陆')
            self.close()
            informationw.close()
            mainw.close()
            loginw.show()
            return
        else:
            QMessageBox.information(self, '提示', '密码错误')
            self.settextnull()

    def settextnull(self):
        self.prepassEdit.setText('')
        self.newpassEdit.setText('')


if __name__ == '__main__':
    # 高分辨率自适应
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    # 实例化每个窗口
    loginw = LoginWidow()
    mainw = MainWindow()
    scrapyw = ScrapyWindow()
    aboutw = AboutWidow()
    historyw = HistoryWindow()
    userw = UserWindow()
    # historyw.show()
    dataw = DataWindow()
    loginw.show()
    # mainw.show()
    # dataw.show()
    registerw = RegisterWindow()
    informationw = InformationWidow()
    cloudw = CloudWindow()
    alterpasswordw = AlterpasswordWindow()
    sys.exit(app.exec_())
