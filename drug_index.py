import sys
import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent=parent)
		self.setupData()
		self.setupUi()

	def setupData(self):
		self.tr = json.load(open('drugs_trname.json'))
		self.sc = json.load(open('drugs_scname.json'))
		
	def setupUi(self):
		self.mainlayout = mainlayout = QVBoxLayout(self)
		searchlayout = QHBoxLayout()
		self.infowidget = QWidget()
		self.infowidget.hide()
		
		self.edit = QLineEdit()
		self.edit.returnPressed.connect(lambda: self.showInfo(self.edit.text()))
		
		radioTr = QRadioButton('Tr.', toggled = self.setSearchType)
		radioTr.setChecked(True)
		radioSc = QRadioButton('Sc.')
		
		
		searchlayout.addWidget(radioTr)
		searchlayout.addWidget(radioSc)
		searchlayout.addStretch()
		
		mainlayout.addWidget(self.edit)
		mainlayout.addLayout(searchlayout)
		mainlayout.addWidget(self.infowidget)
	
	def setSearchType(self, tr):
		if tr:
			completer = QCompleter(self.tr.keys())
			self.search = 'tr'
		else:
			completer = QCompleter(self.sc.keys())
			self.search = 'sc'
		self.edit.setCompleter(completer)
		
	def showInfo(self, drug):
		if self.search == 'tr':
			info = self.tr.get(drug)
			if not info: return
		
			old, self.infowidget = self.infowidget, QWidget()
			infolayout = QGridLayout(self.infowidget)		
			
			row = 0
			for label, data in info.items():
				infolayout.addWidget(QLabel(label), row, 0)
				infolayout.addWidget(QLabel(data), row, 1)
				row += 1
			
		# --------------------------------------
		else:
			info = self.sc.get(drug)
			if not info: return
			
			old, self.infowidget = self.infowidget, QListWidget()
			
			for record in info:
				self.infowidget.addItem(record.get('TradeName'))
		
		
		self.mainlayout.replaceWidget(old, self.infowidget)
		old.hide()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec()
