from option_theme import *
from main import *

class OptionTheme(QDialog,Ui_Dialog):
	def __init__(self,parent = None):
		super(OptionTheme,self).__init__(parent)
		self.setupUi(self)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

		self.pushButton_close.clicked.connect(self.close)
		self.pushButton_cancel.clicked.connect(self.close)
		self.label_title.mouseMoveEvent = self.moveWindow 

		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(15)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QtGui.QColor(89, 145, 255))
		self.frame_main.setGraphicsEffect(self.shadow)

		self.radioButton_dark.setChecked(True)
		self.radioButton_light.toggled.connect(self.setTheme)
		self.pushButton_dark.clicked.connect(lambda: self.checkButton(True))
		self.pushButton_light.clicked.connect(lambda: self.checkButton(False))
		self.pushButton_ok.clicked.connect(self.Continue)		
		self.setTheme()

	def moveWindow(self,event):
		# MOVE WINDOW 
		
		if event.buttons() == QtCore.Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()			
			event.accept()

	def mousePressEvent(self,event):
		self.dragPos = event.globalPos()

	def setTheme(self):
		if self.radioButton_light.isChecked():
			self.pushButton_light.setStyleSheet('''background-image: url(:/gui/iconapp/gui/light_theme.png);
												border: 3px solid rgb(91, 152, 248);''')
			self.pushButton_dark.setStyleSheet('''background-image: url(:/gui/iconapp/gui/dark_theme.png);
												border: 3px solid rgb(33,33,33);''')
			theme = 'light'
			state = False
			print('Giao dien ban ngay')
		else:
			self.pushButton_light.setStyleSheet('''background-image: url(:/gui/iconapp/gui/light_theme.png);
												border: 3px solid rgb(33,33,33);''')
			self.pushButton_dark.setStyleSheet('''background-image: url(:/gui/iconapp/gui/dark_theme.png);
												border: 3px solid rgb(91, 152, 248);''')
			print('Giao dien ban dem')
			theme = 'dark'
			state = True

		setting = {
					
    			"theme": theme,
    			"state": state
		}
		

		with open('settings/setting.json','w') as f:
			f.write(json.dumps(setting,indent =4))

		

	def checkButton(self,boolean):
		if boolean:
			self.radioButton_dark.setChecked(True)
			self.radioButton_light.setChecked(False)
		else:
			self.radioButton_dark.setChecked(False)
			self.radioButton_light.setChecked(True)
		self.setTheme()

	def Continue(self):
		self.close()
		main = MainWindow()
		main.show()

			


if __name__ =='__main__':
	app = QApplication(sys.argv)
	if os.path.isfile('settings/setting.json'):
		window = MainWindow()
	else:
		window = OptionTheme()

	window.show()
	sys.exit(app.exec_())
