''' برنامج لعرض أشهر أدوية الشراب فى السوق مصنفة حسب الاستخدام '''
import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent=parent)
		
		self.setupData()
		self.setupUi()
		
	def setupData(self):
		syrup_fn = 'syrup.txt'
		drops_fn = 'drops-sprays.txt'
		
		syrup_reader = csv.reader(open(syrup_fn))
		drops_reader = csv.reader(open(drops_fn))
		
		self.data = {}
		for reader in (syrup_reader, drops_reader):
			for name, category in reader:
				self.data.setdefault(category, set()).add(name)
	
	def setupUi(self):
		mainlayout = QVBoxLayout(self)
		
		combo = QComboBox()
		combo.addItems(sorted(self.data.keys(), key=lambda x: x.lower()))
		
		self.drug_list = drug_list = QListWidget()
		# drug_list.setStyleSheet('::item { padding: 5px}')

		combo.currentIndexChanged[str].connect(self.updateList)
		combo.currentIndexChanged[str].emit(combo.currentText())		
		
		mainlayout.addWidget(combo)
		mainlayout.addWidget(drug_list)
		
	def updateList(self, category):
		self.drug_list.clear()
		self.drug_list.addItems(sorted(self.data[category]))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec()
