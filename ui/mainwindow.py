# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Tue Oct 14 09:33:11 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(980, 608)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.navWidget = QtGui.QWidget(self.centralwidget)
        self.navWidget.setGeometry(QtCore.QRect(0, 0, 80, 608))
        self.navWidget.setObjectName(_fromUtf8("navWidget"))
        self.logoImg = QtGui.QLabel(self.navWidget)
        self.logoImg.setGeometry(QtCore.QRect(0, 0, 80, 80))
        self.logoImg.setText(_fromUtf8(""))
        self.logoImg.setObjectName(_fromUtf8("logoImg"))
        self.btnHomepage = QtGui.QPushButton(self.navWidget)
        self.btnHomepage.setGeometry(QtCore.QRect(0, 80, 80, 88))
        self.btnHomepage.setText(_fromUtf8(""))
        self.btnHomepage.setObjectName(_fromUtf8("btnHomepage"))
        self.btnUp = QtGui.QPushButton(self.navWidget)
        self.btnUp.setGeometry(QtCore.QRect(0, 256, 80, 88))
        self.btnUp.setText(_fromUtf8(""))
        self.btnUp.setObjectName(_fromUtf8("btnUp"))
        self.btnUn = QtGui.QPushButton(self.navWidget)
        self.btnUn.setGeometry(QtCore.QRect(0, 344, 80, 88))
        self.btnUn.setText(_fromUtf8(""))
        self.btnUn.setObjectName(_fromUtf8("btnUn"))
        self.btnWin = QtGui.QPushButton(self.navWidget)
        self.btnWin.setGeometry(QtCore.QRect(0, 432, 80, 88))
        self.btnWin.setText(_fromUtf8(""))
        self.btnWin.setObjectName(_fromUtf8("btnWin"))
        self.btnTask = QtGui.QPushButton(self.navWidget)
        self.btnTask.setGeometry(QtCore.QRect(0, 520, 80, 88))
        self.btnTask.setText(_fromUtf8(""))
        self.btnTask.setObjectName(_fromUtf8("btnTask"))
        self.btnAll = QtGui.QPushButton(self.navWidget)
        self.btnAll.setGeometry(QtCore.QRect(0, 168, 80, 88))
        self.btnAll.setText(_fromUtf8(""))
        self.btnAll.setObjectName(_fromUtf8("btnAll"))
        self.rightWidget = QtGui.QWidget(self.centralwidget)
        self.rightWidget.setGeometry(QtCore.QRect(80, 0, 900, 608))
        self.rightWidget.setObjectName(_fromUtf8("rightWidget"))
        self.allWidget = QtGui.QWidget(self.rightWidget)
        self.allWidget.setGeometry(QtCore.QRect(20, 36, 880, 572))
        self.allWidget.setObjectName(_fromUtf8("allWidget"))
        self.allline = QtGui.QLabel(self.allWidget)
        self.allline.setGeometry(QtCore.QRect(0, 44, 860, 1))
        self.allline.setText(_fromUtf8(""))
        self.allline.setObjectName(_fromUtf8("allline"))
        self.allcw1 = QtGui.QWidget(self.allWidget)
        self.allcw1.setGeometry(QtCore.QRect(750, 20, 130, 15))
        self.allcw1.setObjectName(_fromUtf8("allcw1"))
        self.alltext1 = QtGui.QLabel(self.allcw1)
        self.alltext1.setGeometry(QtCore.QRect(0, 0, 50, 15))
        self.alltext1.setText(_fromUtf8(""))
        self.alltext1.setObjectName(_fromUtf8("alltext1"))
        self.alltext2 = QtGui.QLabel(self.allcw1)
        self.alltext2.setGeometry(QtCore.QRect(69, 0, 44, 15))
        self.alltext2.setText(_fromUtf8(""))
        self.alltext2.setObjectName(_fromUtf8("alltext2"))
        self.allcount = QtGui.QLabel(self.allcw1)
        self.allcount.setGeometry(QtCore.QRect(23, 0, 50, 15))
        self.allcount.setText(_fromUtf8(""))
        self.allcount.setObjectName(_fromUtf8("allcount"))
        self.unWidget = QtGui.QWidget(self.rightWidget)
        self.unWidget.setGeometry(QtCore.QRect(20, 36, 880, 572))
        self.unWidget.setObjectName(_fromUtf8("unWidget"))
        self.unline = QtGui.QLabel(self.unWidget)
        self.unline.setGeometry(QtCore.QRect(0, 44, 860, 1))
        self.unline.setText(_fromUtf8(""))
        self.unline.setObjectName(_fromUtf8("unline"))
        self.uncw1 = QtGui.QWidget(self.unWidget)
        self.uncw1.setGeometry(QtCore.QRect(750, 20, 130, 15))
        self.uncw1.setObjectName(_fromUtf8("uncw1"))
        self.untext1 = QtGui.QLabel(self.uncw1)
        self.untext1.setGeometry(QtCore.QRect(0, 0, 50, 15))
        self.untext1.setText(_fromUtf8(""))
        self.untext1.setObjectName(_fromUtf8("untext1"))
        self.untext2 = QtGui.QLabel(self.uncw1)
        self.untext2.setGeometry(QtCore.QRect(69, 0, 44, 15))
        self.untext2.setText(_fromUtf8(""))
        self.untext2.setObjectName(_fromUtf8("untext2"))
        self.uncount = QtGui.QLabel(self.uncw1)
        self.uncount.setGeometry(QtCore.QRect(30, 0, 50, 15))
        self.uncount.setText(_fromUtf8(""))
        self.uncount.setObjectName(_fromUtf8("uncount"))
        self.homepageWidget = QtGui.QWidget(self.rightWidget)
        self.homepageWidget.setGeometry(QtCore.QRect(20, 36, 880, 572))
        self.homepageWidget.setObjectName(_fromUtf8("homepageWidget"))
        self.recommendWidget = QtGui.QWidget(self.homepageWidget)
        self.recommendWidget.setGeometry(QtCore.QRect(0, 275, 640, 291))
        self.recommendWidget.setObjectName(_fromUtf8("recommendWidget"))
        self.hometext1 = QtGui.QLabel(self.recommendWidget)
        self.hometext1.setGeometry(QtCore.QRect(0, 0, 60, 15))
        self.hometext1.setText(_fromUtf8(""))
        self.hometext1.setObjectName(_fromUtf8("hometext1"))
        self.homeline1 = QtGui.QLabel(self.recommendWidget)
        self.homeline1.setGeometry(QtCore.QRect(0, 17, 640, 1))
        self.homeline1.setText(_fromUtf8(""))
        self.homeline1.setObjectName(_fromUtf8("homeline1"))
        self.rankWidget = QtGui.QWidget(self.homepageWidget)
        self.rankWidget.setGeometry(QtCore.QRect(660, 275, 200, 291))
        self.rankWidget.setObjectName(_fromUtf8("rankWidget"))
        self.rankView = QtGui.QListWidget(self.rankWidget)
        self.rankView.setGeometry(QtCore.QRect(0, 23, 200, 268))
        self.rankView.setObjectName(_fromUtf8("rankView"))
        self.hometext2 = QtGui.QLabel(self.rankWidget)
        self.hometext2.setGeometry(QtCore.QRect(0, 0, 60, 15))
        self.hometext2.setText(_fromUtf8(""))
        self.hometext2.setObjectName(_fromUtf8("hometext2"))
        self.homeline2 = QtGui.QLabel(self.rankWidget)
        self.homeline2.setGeometry(QtCore.QRect(0, 17, 200, 1))
        self.homeline2.setText(_fromUtf8(""))
        self.homeline2.setObjectName(_fromUtf8("homeline2"))
        self.homeMsgWidget = QtGui.QWidget(self.homepageWidget)
        self.homeMsgWidget.setGeometry(QtCore.QRect(0, 0, 860, 44))
        self.homeMsgWidget.setObjectName(_fromUtf8("homeMsgWidget"))
        self.afterLoginWidget = QtGui.QWidget(self.homeMsgWidget)
        self.afterLoginWidget.setGeometry(QtCore.QRect(0, 0, 290, 44))
        self.afterLoginWidget.setObjectName(_fromUtf8("afterLoginWidget"))
        self.userLogoafter = QtGui.QLabel(self.afterLoginWidget)
        self.userLogoafter.setGeometry(QtCore.QRect(0, 14, 16, 16))
        self.userLogoafter.setText(_fromUtf8(""))
        self.userLogoafter.setObjectName(_fromUtf8("userLogoafter"))
        self.welcometext = QtGui.QLabel(self.afterLoginWidget)
        self.welcometext.setGeometry(QtCore.QRect(18, 14, 50, 15))
        self.welcometext.setText(_fromUtf8(""))
        self.welcometext.setObjectName(_fromUtf8("welcometext"))
        self.username = QtGui.QLabel(self.afterLoginWidget)
        self.username.setGeometry(QtCore.QRect(70, 14, 80, 16))
        self.username.setText(_fromUtf8(""))
        self.username.setObjectName(_fromUtf8("username"))
        self.btnLogout = QtGui.QPushButton(self.afterLoginWidget)
        self.btnLogout.setGeometry(QtCore.QRect(220, 14, 45, 15))
        self.btnLogout.setText(_fromUtf8(""))
        self.btnLogout.setObjectName(_fromUtf8("btnLogout"))
        self.btnAppList = QtGui.QPushButton(self.afterLoginWidget)
        self.btnAppList.setGeometry(QtCore.QRect(150, 14, 60, 15))
        self.btnAppList.setText(_fromUtf8(""))
        self.btnAppList.setObjectName(_fromUtf8("btnAppList"))
        self.beforeLoginWidget = QtGui.QWidget(self.homeMsgWidget)
        self.beforeLoginWidget.setGeometry(QtCore.QRect(0, 0, 290, 44))
        self.beforeLoginWidget.setObjectName(_fromUtf8("beforeLoginWidget"))
        self.userLogo = QtGui.QLabel(self.beforeLoginWidget)
        self.userLogo.setGeometry(QtCore.QRect(0, 14, 16, 16))
        self.userLogo.setText(_fromUtf8(""))
        self.userLogo.setObjectName(_fromUtf8("userLogo"))
        self.btnLogin = QtGui.QPushButton(self.beforeLoginWidget)
        self.btnLogin.setGeometry(QtCore.QRect(18, 14, 50, 15))
        self.btnLogin.setText(_fromUtf8(""))
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        self.btnReg = QtGui.QPushButton(self.beforeLoginWidget)
        self.btnReg.setGeometry(QtCore.QRect(70, 14, 65, 15))
        self.btnReg.setText(_fromUtf8(""))
        self.btnReg.setObjectName(_fromUtf8("btnReg"))
        self.homecw1 = QtGui.QWidget(self.homepageWidget)
        self.homecw1.setGeometry(QtCore.QRect(750, 20, 130, 15))
        self.homecw1.setObjectName(_fromUtf8("homecw1"))
        self.hometext3 = QtGui.QLabel(self.homecw1)
        self.hometext3.setGeometry(QtCore.QRect(0, 0, 50, 15))
        self.hometext3.setText(_fromUtf8(""))
        self.hometext3.setObjectName(_fromUtf8("hometext3"))
        self.hometext4 = QtGui.QLabel(self.homecw1)
        self.hometext4.setGeometry(QtCore.QRect(69, 0, 44, 15))
        self.hometext4.setText(_fromUtf8(""))
        self.hometext4.setObjectName(_fromUtf8("hometext4"))
        self.homecount = QtGui.QLabel(self.homecw1)
        self.homecount.setGeometry(QtCore.QRect(23, 0, 50, 15))
        self.homecount.setText(_fromUtf8(""))
        self.homecount.setObjectName(_fromUtf8("homecount"))
        self.searchWidget = QtGui.QWidget(self.rightWidget)
        self.searchWidget.setGeometry(QtCore.QRect(20, 36, 880, 572))
        self.searchWidget.setObjectName(_fromUtf8("searchWidget"))
        self.searchline = QtGui.QLabel(self.searchWidget)
        self.searchline.setGeometry(QtCore.QRect(0, 44, 860, 1))
        self.searchline.setText(_fromUtf8(""))
        self.searchline.setObjectName(_fromUtf8("searchline"))
        self.searchcw1 = QtGui.QWidget(self.searchWidget)
        self.searchcw1.setGeometry(QtCore.QRect(750, 20, 130, 15))
        self.searchcw1.setObjectName(_fromUtf8("searchcw1"))
        self.searchtext1 = QtGui.QLabel(self.searchcw1)
        self.searchtext1.setGeometry(QtCore.QRect(0, 0, 50, 15))
        self.searchtext1.setText(_fromUtf8(""))
        self.searchtext1.setObjectName(_fromUtf8("searchtext1"))
        self.searchtext2 = QtGui.QLabel(self.searchcw1)
        self.searchtext2.setGeometry(QtCore.QRect(69, 0, 44, 15))
        self.searchtext2.setText(_fromUtf8(""))
        self.searchtext2.setObjectName(_fromUtf8("searchtext2"))
        self.searchcount = QtGui.QLabel(self.searchcw1)
        self.searchcount.setGeometry(QtCore.QRect(30, 0, 50, 15))
        self.searchcount.setText(_fromUtf8(""))
        self.searchcount.setObjectName(_fromUtf8("searchcount"))
        self.taskWidget = QtGui.QWidget(self.rightWidget)
        self.taskWidget.setGeometry(QtCore.QRect(0, 0, 320, 608))
        self.taskWidget.setObjectName(_fromUtf8("taskWidget"))
        self.taskListWidget = QtGui.QListWidget(self.taskWidget)
        self.taskListWidget.setGeometry(QtCore.QRect(10, 65, 300, 475))
        self.taskListWidget.setObjectName(_fromUtf8("taskListWidget"))
        self.btnCloseTask = QtGui.QPushButton(self.taskWidget)
        self.btnCloseTask.setGeometry(QtCore.QRect(290, 1, 28, 36))
        self.btnCloseTask.setText(_fromUtf8(""))
        self.btnCloseTask.setObjectName(_fromUtf8("btnCloseTask"))
        self.taskhline = QtGui.QLabel(self.taskWidget)
        self.taskhline.setGeometry(QtCore.QRect(10, 55, 300, 1))
        self.taskhline.setText(_fromUtf8(""))
        self.taskhline.setObjectName(_fromUtf8("taskhline"))
        self.tasklabel = QtGui.QLabel(self.taskWidget)
        self.tasklabel.setGeometry(QtCore.QRect(10, 35, 151, 16))
        self.tasklabel.setText(_fromUtf8(""))
        self.tasklabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tasklabel.setObjectName(_fromUtf8("tasklabel"))
        self.taskvline = QtGui.QLabel(self.taskWidget)
        self.taskvline.setGeometry(QtCore.QRect(160, 37, 1, 14))
        self.taskvline.setText(_fromUtf8(""))
        self.taskvline.setAlignment(QtCore.Qt.AlignCenter)
        self.taskvline.setObjectName(_fromUtf8("taskvline"))
        self.taskBottomWidget = QtGui.QWidget(self.taskWidget)
        self.taskBottomWidget.setGeometry(QtCore.QRect(0, 544, 320, 64))
        self.taskBottomWidget.setObjectName(_fromUtf8("taskBottomWidget"))
        self.btnClearTask = QtGui.QPushButton(self.taskBottomWidget)
        self.btnClearTask.setGeometry(QtCore.QRect(146, 17, 28, 28))
        self.btnClearTask.setText(_fromUtf8(""))
        self.btnClearTask.setObjectName(_fromUtf8("btnClearTask"))
        self.upWidget = QtGui.QWidget(self.rightWidget)
        self.upWidget.setGeometry(QtCore.QRect(20, 36, 880, 572))
        self.upWidget.setObjectName(_fromUtf8("upWidget"))
        self.upline = QtGui.QLabel(self.upWidget)
        self.upline.setGeometry(QtCore.QRect(0, 44, 860, 1))
        self.upline.setText(_fromUtf8(""))
        self.upline.setObjectName(_fromUtf8("upline"))
        self.upcw1 = QtGui.QWidget(self.upWidget)
        self.upcw1.setGeometry(QtCore.QRect(750, 20, 130, 15))
        self.upcw1.setObjectName(_fromUtf8("upcw1"))
        self.uptext1 = QtGui.QLabel(self.upcw1)
        self.uptext1.setGeometry(QtCore.QRect(0, 0, 50, 15))
        self.uptext1.setText(_fromUtf8(""))
        self.uptext1.setObjectName(_fromUtf8("uptext1"))
        self.uptext2 = QtGui.QLabel(self.upcw1)
        self.uptext2.setGeometry(QtCore.QRect(69, 0, 44, 15))
        self.uptext2.setText(_fromUtf8(""))
        self.uptext2.setObjectName(_fromUtf8("uptext2"))
        self.upcount = QtGui.QLabel(self.upcw1)
        self.upcount.setGeometry(QtCore.QRect(30, 0, 50, 15))
        self.upcount.setText(_fromUtf8(""))
        self.upcount.setObjectName(_fromUtf8("upcount"))
        self.headerWidget = QtGui.QWidget(self.rightWidget)
        self.headerWidget.setGeometry(QtCore.QRect(20, 0, 860, 36))
        self.headerWidget.setObjectName(_fromUtf8("headerWidget"))
        self.btnClose = QtGui.QPushButton(self.headerWidget)
        self.btnClose.setGeometry(QtCore.QRect(0, 0, 28, 36))
        self.btnClose.setText(_fromUtf8(""))
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.btnMin = QtGui.QPushButton(self.headerWidget)
        self.btnMin.setGeometry(QtCore.QRect(28, 0, 28, 36))
        self.btnMin.setText(_fromUtf8(""))
        self.btnMin.setObjectName(_fromUtf8("btnMin"))
        self.btnConf = QtGui.QPushButton(self.headerWidget)
        self.btnConf.setGeometry(QtCore.QRect(84, 0, 28, 36))
        self.btnConf.setText(_fromUtf8(""))
        self.btnConf.setObjectName(_fromUtf8("btnConf"))
        self.firstFocus = QtGui.QLineEdit(self.headerWidget)
        self.firstFocus.setGeometry(QtCore.QRect(2000, 2000, 10, 10))
        self.firstFocus.setObjectName(_fromUtf8("firstFocus"))
        self.btnMax = QtGui.QPushButton(self.headerWidget)
        self.btnMax.setGeometry(QtCore.QRect(56, 0, 28, 36))
        self.btnMax.setText(_fromUtf8(""))
        self.btnMax.setObjectName(_fromUtf8("btnMax"))
        self.btnNormal = QtGui.QPushButton(self.headerWidget)
        self.btnNormal.setGeometry(QtCore.QRect(56, 0, 28, 36))
        self.btnNormal.setText(_fromUtf8(""))
        self.btnNormal.setObjectName(_fromUtf8("btnNormal"))
        self.headercw1 = QtGui.QWidget(self.headerWidget)
        self.headercw1.setGeometry(QtCore.QRect(575, 0, 285, 36))
        self.headercw1.setObjectName(_fromUtf8("headercw1"))
        self.btnCloseDetail = QtGui.QPushButton(self.headercw1)
        self.btnCloseDetail.setGeometry(QtCore.QRect(0, 14, 15, 19))
        self.btnCloseDetail.setText(_fromUtf8(""))
        self.btnCloseDetail.setObjectName(_fromUtf8("btnCloseDetail"))
        self.leSearch = QtGui.QLineEdit(self.headercw1)
        self.leSearch.setGeometry(QtCore.QRect(25, 12, 260, 24))
        self.leSearch.setObjectName(_fromUtf8("leSearch"))
        self.lebg = QtGui.QPushButton(self.headercw1)
        self.lebg.setGeometry(QtCore.QRect(264, 16, 16, 16))
        self.lebg.setText(_fromUtf8(""))
        self.lebg.setObjectName(_fromUtf8("lebg"))
        self.winpageWidget = QtGui.QWidget(self.rightWidget)
        self.winpageWidget.setGeometry(QtCore.QRect(20, 36, 880, 572))
        self.winpageWidget.setObjectName(_fromUtf8("winpageWidget"))
        self.wintitle = QtGui.QLabel(self.winpageWidget)
        self.wintitle.setGeometry(QtCore.QRect(0, 26, 301, 15))
        self.wintitle.setText(_fromUtf8(""))
        self.wintitle.setObjectName(_fromUtf8("wintitle"))
        self.winline = QtGui.QLabel(self.winpageWidget)
        self.winline.setGeometry(QtCore.QRect(0, 44, 860, 1))
        self.winline.setText(_fromUtf8(""))
        self.winline.setObjectName(_fromUtf8("winline"))
        self.wincw1 = QtGui.QWidget(self.winpageWidget)
        self.wincw1.setGeometry(QtCore.QRect(750, 20, 130, 15))
        self.wincw1.setObjectName(_fromUtf8("wincw1"))
        self.winlabel1 = QtGui.QLabel(self.wincw1)
        self.winlabel1.setGeometry(QtCore.QRect(0, 0, 50, 15))
        self.winlabel1.setText(_fromUtf8(""))
        self.winlabel1.setObjectName(_fromUtf8("winlabel1"))
        self.winlabel2 = QtGui.QLabel(self.wincw1)
        self.winlabel2.setGeometry(QtCore.QRect(69, 0, 44, 15))
        self.winlabel2.setText(_fromUtf8(""))
        self.winlabel2.setObjectName(_fromUtf8("winlabel2"))
        self.wincountlabel = QtGui.QLabel(self.wincw1)
        self.wincountlabel.setGeometry(QtCore.QRect(30, 0, 50, 15))
        self.wincountlabel.setText(_fromUtf8(""))
        self.wincountlabel.setObjectName(_fromUtf8("wincountlabel"))
        self.virtuallabel = QtGui.QLabel(self.rightWidget)
        self.virtuallabel.setGeometry(QtCore.QRect(20, 590, 880, 18))
        self.virtuallabel.setText(_fromUtf8(""))
        self.virtuallabel.setObjectName(_fromUtf8("virtuallabel"))
        self.detailShellWidget = QtGui.QWidget(self.rightWidget)
        self.detailShellWidget.setGeometry(QtCore.QRect(20, 50, 873, 558))
        self.detailShellWidget.setObjectName(_fromUtf8("detailShellWidget"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

