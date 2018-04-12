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
		self.data = json.load(open('drugs.json'))
	
	def setupUi(self):
		self.mainlayout = mainlayout = QVBoxLayout(self)
		self.infowidget = QWidget()
		
		# drug_list = QComboBox()
		# drug_list.setEditable(True)
		# drug_list.addItems(sorted(self.data.keys()))
		# drug_list.currentIndexChanged[str].connect(self.showInfo)
		
		drug_edit = QLineEdit()
		completer = QCompleter(self.data.keys())
		drug_edit.setCompleter(completer)
		drug_edit.returnPressed.connect(lambda: self.showInfo(drug_edit.text()))
		
		# mainlayout.addWidget(drug_list)
		mainlayout.addWidget(QLabel('Trade Name Search'))
		mainlayout.addWidget(drug_edit)
		self.mainlayout.addWidget(self.infowidget)
		
	def showInfo(self, drug):
		info = self.data.get(drug)
		if not info: return
		
		old, self.infowidget = self.infowidget, QWidget()
		infolayout = QGridLayout(self.infowidget)		
		
		row = 0
		for label, data in info.items():
			infolayout.addWidget(QLabel(label), row, 0)
			infolayout.addWidget(QLabel(data), row, 1)
			row += 1
		
		self.mainlayout.replaceWidget(old, self.infowidget)
		old.hide()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec()
