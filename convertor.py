import sys
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import (
	QApplication, QMainWindow,
	QWidget, QLabel, QDoubleSpinBox, #QDoubleSpinBox Поле для вода дробных чисел
	QVBoxLayout, QPushButton
)
from PyQt5.Qt import Qt
from urllib.request import urlopen
from lxml import etree

class Course(QObject):
	CBR_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

	def get(self):
		"""
		with urlopen(self.CBR_URL) as f:
			tree = etree.parse(f)
			value = tree.xpath('*[@ID="R01235"]/Value')[0].text

		"""
		return 30 #float(value.replace(',','.'))

class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._initUi()
		self._initSignals()
		self._initLayouts()

	def _initUi(self):
		self.setWindowTitle('Конвертор валют')
		self.resize(400, 300)

		self.srcLabel = QLabel('Сумма в рублях', self)
		self.resultLabel = QLabel('Сумма в долларах', self)

		self.srcAmountEdit = QDoubleSpinBox(self)
		self.srcAmountEdit.setMaximum(999999999)
		self.resultAmountEdit = QDoubleSpinBox(self)
		self.resultAmountEdit.setMaximum(999999999)

		self.covertBtn = QPushButton('Перевести', self)
		self.resetBtn = QPushButton('Сброс', self)
		self.covertBtn.setEnabled(False)

	def _initSignals(self):
		self.covertBtn.clicked.connect(self.onClickConvertBtn)
		self.resetBtn.clicked.connect(self.onClickResetBtn)

		self.srcAmountEdit.valueChanged.connect(self.valuechange)
		self.resultAmountEdit.valueChanged.connect(self.valuechange)
		#Enter
		#self.covertBtn.setAutoDefault(True)
		#self.srcAmountEdit.returnPressed.connect(self.covertBtn.click)
		#self.srcAmountEdit.returnPressed.connect(self.onEnter)


	def _initLayouts(self):
		"""заполнение слоев разными объектами"""
		w = QWidget(self) #промежуточный виджет

		self.mainLayout = QVBoxLayout(w)

		self.mainLayout.addWidget(self.srcLabel)
		self.mainLayout.addWidget(self.srcAmountEdit)
		self.mainLayout.addWidget(self.resultLabel)
		self.mainLayout.addWidget(self.resultAmountEdit)
		self.mainLayout.addWidget(self.covertBtn)
		self.mainLayout.addWidget(self.resetBtn)

		self.setCentralWidget(w)

	def onClickConvertBtn(self):
		self.covertBtn.setEnabled(True)
		valueRub = self.srcAmountEdit.value()
		valueUsd = self.resultAmountEdit.value()
		if valueRub and not valueUsd:
			self.resultAmountEdit.setValue(
				valueRub / Course().get()
			)
		elif valueUsd and not valueRub:
			self.srcAmountEdit.setValue(
				valueUsd * Course().get()
			)

	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Return: 
			self.onClickConvertBtn()

	def onClickResetBtn(self):
		self.srcAmountEdit.setValue(0)
		self.resultAmountEdit.setValue(0)

	def valuechange(self):
		if (self.srcAmountEdit.value()) or (self.resultAmountEdit.value()) :
			self.covertBtn.setEnabled(True)
		else:
			self.covertBtn.setEnabled(False)



if __name__ == '__main__':
	app = QApplication(sys.argv)

	convertor = MainWindow()
	convertor.show()

	sys.exit(app.exec_())