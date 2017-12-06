# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../anagram.ui'
#
# Created: Mon Nov  4 20:12:56 2013
#      by: PyQt4 UI code generator 4.10
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
        MainWindow.resize(687, 399)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.prompt_label = QtGui.QLabel(self.centralwidget)
        self.prompt_label.setObjectName(_fromUtf8("prompt_label"))
        self.gridLayout.addWidget(self.prompt_label, 0, 0, 1, 1)
        self.input = QtGui.QLineEdit(self.centralwidget)
        self.input.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.input.setInputMask(_fromUtf8(""))
        self.input.setMaxLength(32767)
        self.input.setFrame(True)
        self.input.setCursorPosition(0)
        self.input.setDragEnabled(False)
        self.input.setPlaceholderText(_fromUtf8(""))
        self.input.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.input.setObjectName(_fromUtf8("input"))
        self.gridLayout.addWidget(self.input, 0, 1, 1, 1)
        self.find_btn = QtGui.QPushButton(self.centralwidget)
        self.find_btn.setObjectName(_fromUtf8("find_btn"))
        self.gridLayout.addWidget(self.find_btn, 0, 2, 1, 1)
        self.results_label = QtGui.QLabel(self.centralwidget)
        self.results_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.results_label.setObjectName(_fromUtf8("results_label"))
        self.gridLayout.addWidget(self.results_label, 1, 0, 1, 1)
        self.results_list = QtGui.QListView(self.centralwidget)
        self.results_list.setObjectName(_fromUtf8("results_list"))
        self.gridLayout.addWidget(self.results_list, 1, 1, 1, 1)
        self.exit_btn = QtGui.QPushButton(self.centralwidget)
        self.exit_btn.setObjectName(_fromUtf8("exit_btn"))
        self.gridLayout.addWidget(self.exit_btn, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 687, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.exit_btn, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ανα(ποδο)γραμματισμοί", None))
        self.prompt_label.setText(_translate("MainWindow", "Αναγραμματισμένη λέξη :", None))
        self.find_btn.setText(_translate("MainWindow", "Βρες την αρχική λέξη", None))
        self.results_label.setText(_translate("MainWindow", "Αποτελέσματα :", None))
        self.exit_btn.setText(_translate("MainWindow", "Έξοδος", None))

