# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/uknormalcard.ui'
#
# Created: Wed Sep  3 11:25:32 2014
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

class Ui_NormalCard(object):
    def setupUi(self, NormalCard):
        NormalCard.setObjectName(_fromUtf8("NormalCard"))
        NormalCard.resize(212, 88)
        self.baseWidget = QtGui.QWidget(NormalCard)
        self.baseWidget.setGeometry(QtCore.QRect(0, 0, 212, 88))
        self.baseWidget.setObjectName(_fromUtf8("baseWidget"))

        self.size = QtGui.QLabel(self.baseWidget)
        self.size.setGeometry(QtCore.QRect(75, 38, 110, 17))
        self.size.setText(_fromUtf8(""))
        self.size.setObjectName(_fromUtf8("size"))
        self.name = QtGui.QLabel(self.baseWidget)
        self.name.setGeometry(QtCore.QRect(75, 20, 110, 17))
        self.name.setText(_fromUtf8(""))
        self.name.setObjectName(_fromUtf8("name"))
        self.icon = QtGui.QLabel(self.baseWidget)
        self.icon.setGeometry(QtCore.QRect(20, 20, 48, 48))
        self.icon.setText(_fromUtf8(""))
        self.icon.setObjectName(_fromUtf8("icon"))
        self.isInstalled = QtGui.QLabel(self.baseWidget)
        self.isInstalled.setGeometry(QtCore.QRect(75, 54, 110, 17))
        self.isInstalled.setText(_fromUtf8(""))
        self.isInstalled.setObjectName(_fromUtf8("isInstalled"))
        self.detailWidget = QtGui.QWidget(NormalCard)
        self.detailWidget.setGeometry(QtCore.QRect(0, -88, 212, 88))
        self.detailWidget.setObjectName(_fromUtf8("detailWidget"))
        self.named = QtGui.QLabel(self.detailWidget)
        self.named.setGeometry(QtCore.QRect(10, 5, 190, 15))
        self.named.setText(_fromUtf8(""))
        self.named.setObjectName(_fromUtf8("named"))
        self.description = QtGui.QTextEdit(self.detailWidget)
        self.description.setGeometry(QtCore.QRect(6, 18, 205, 40))
        self.description.setObjectName(_fromUtf8("description"))
        self.btnDetail = QtGui.QPushButton(self.detailWidget)
        self.btnDetail.setGeometry(QtCore.QRect(0, 0, 212, 59))
        self.btnDetail.setText(_fromUtf8(""))
        self.btnDetail.setObjectName(_fromUtf8("btnDetail"))
        self.btn = QtGui.QPushButton(self.detailWidget)
        self.btn.setGeometry(QtCore.QRect(0, 59, 212, 29))
        self.btn.setText(_fromUtf8(""))
        self.btn.setObjectName(_fromUtf8("btn"))

        # wb:
        self.progressBar = QtGui.QProgressBar(NormalCard)
        self.progressBar.setGeometry(QtCore.QRect(0, 0, 212, 88))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progresslabel = QtGui.QLabel(NormalCard)
        self.progresslabel.setGeometry(QtCore.QRect(120, 35, 35, 18))
        self.progresslabel.setText(_fromUtf8(""))
        self.progresslabel.setVisible(False)
        self.progresslabel.setObjectName(_fromUtf8("progresslabel"))

        self.progressBar_icon = QtGui.QLabel(NormalCard)
        self.progressBar_icon.setGeometry(QtCore.QRect(20, 20, 48, 48))
        self.progressBar_icon.setText(_fromUtf8(""))
        self.progressBar_icon.setVisible(False)
        self.progressBar_icon.setObjectName(_fromUtf8("icon_progressBar"))


        self.retranslateUi(NormalCard)
        QtCore.QMetaObject.connectSlotsByName(NormalCard)

    def retranslateUi(self, NormalCard):
        NormalCard.setWindowTitle(_translate("NormalCard", "Form", None))

