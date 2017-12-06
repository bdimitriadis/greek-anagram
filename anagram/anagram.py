#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import anagramx
from anag import *

class capsValidator(QtGui.QRegExpValidator):
	def __init__(self, regx=None):
		super(capsValidator, self).__init__(regx)

	def validate(self, input, pos):
		input=input.replace(0, len(input), input.toUpper())
		return super(capsValidator, self).validate(input, pos)




class Ui_improved:
	def setupUi(self, MainWindow):
		self.uii=anagramx.Ui_MainWindow()
		self.uii.setupUi(MainWindow)
		self.dic_lst=load_dic()
		#self.uii.input.setMaxLength(40)
		cvalidator=capsValidator(QtCore.QRegExp("[^\W\d_]{2,40}"))
		self.uii.input.setValidator(cvalidator)		
		self.uii.find_btn.pressed.connect(self.updateList)
	

	def updateList(self):
		flist=anagram(unicode(self.uii.input.text()), self.dic_lst)
		slist=QtCore.QStringList()	
		for eachresult in flist:	
			slist << eachresult
    		model = QtGui.QStringListModel(slist)
    		self.uii.results_list.setModel(model)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_improved()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
