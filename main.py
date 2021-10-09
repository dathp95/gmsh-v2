from gmsh import Ui_MainWindow
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui,QtCore


import qss as style
import json, os


from create_file import Ui_Dialog_CreateFile as Form_File
from import_data import Ui_Dialog_ImportNick as Form_Nick
from table_func import *





class MainWindow(QMainWindow,Ui_MainWindow,Table):
	def __init__(self, parent = None):
		super(MainWindow,self).__init__(parent)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.setupUi(self)	
		self.setUpButton()		
		self.setUpMain()
		self.setUpTheme()


	def setUpMain(self):
		self.stackedWidget.setCurrentWidget(self.page_setting)		
		self.shadow =QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(10)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QtGui.QColor(89, 145, 255))
		self.label_title.mouseMoveEvent = self.moveWindow 
		self.frame_main.setGraphicsEffect(self.shadow)

		self.comboBox.addItems(file.replace('.txt','') for file in os.listdir('data'))

	def setUpTheme(self):
		with open('settings/setting.json','r') as f:
			theme = json.load(f)
		self.state_theme = theme['state']
		self.changeTheme()

	def changeTheme(self):
		if self.state_theme:
			self.setStyleSheet(style.dark_theme)			
			self.state_theme = False
			current_theme = {
								"theme": "dark",
								"state": True,
							}
		else:
			self.setStyleSheet(style.light_theme)
			
			self.state_theme = True
			current_theme = {
								"theme": "light",
								"state": False,
							}
		
		with open('settings/setting.json','w') as file:
			file.write(json.dumps(current_theme,indent=4))


	def setUpButton(self):
		self.pushButton_setting.clicked.connect(self.showPageSetting)
		self.pushButton_get_cmt.clicked.connect(self.showPageImportCmt)
		self.pushButton_export_cmt.clicked.connect(self.showPageSetting)
		self.pushButton_import_cmt.clicked.connect(self.showPageImportCmt)
		self.pushButton_home.clicked.connect(self.changeTheme)
		self.pushButton_close.clicked.connect(self.close)
		self.pushButton_import_file.clicked.connect(self.showFormFile)
		self.pushButton_import_nick.clicked.connect(self.showImportNick)

		# Đang test chương trình
		self.pushButton_login.clicked.connect(self.showMessageBox)
		self.pushButton_stop.clicked.connect(self.setNickOnTable)
		

		self.pushButton_delete_file.clicked.connect(self.deleteFile)



	def moveWindow(self,event):
		# MOVE WINDOW 
		if event.buttons() == QtCore.Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()

	def mousePressEvent(self,event):
		self.dragPos = event.globalPos()

	

	def showPageSetting(self):
		self.stackedWidget.setCurrentWidget(self.page_setting)	


	def showPageImportCmt(self):
		self.stackedWidget.setCurrentWidget(self.page_import_cmt)

	
	def showFormFile(self):
		self.form_file = Dialog_CreateFile(self.styleSheet())


		self.form_file.pushButton_create_file.clicked.connect(self.createFile)		
		self.form_file.pushButton_import_data.clicked.connect(self.showImportNick)	

		self.form_file.exec_() # K tương tác được gui nữa - MAIN bị khóa


	def showImportNick(self):		
		self.import_nick = Dialog_ImportNick(self.styleSheet())

		self.setItemImportNick()

		self.import_nick.pushButton_create_file.clicked.connect(self.showFormFile)
		self.import_nick.pushButton_close_file.clicked.connect(self.import_nick.close)
		self.import_nick.pushButton__save_file.clicked.connect(self.saveFileNick)

		self.import_nick.exec_()
	def showMessageBox(self):
		msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='information',
			boldtext='Thông báo',
			text ='Xin chào tất cả ae nhé',
			ok =True,
			cancel = False)
		msg.exec_()


class Dialog_CreateFile(QDialog,Form_File):
	def __init__(self,style,parent =None):
		super(Dialog_CreateFile,self).__init__(parent)
		self.setupUi(self)
		self.setStyleSheet(style)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.pushButton_close.clicked.connect(self.close)

		self.shadow =QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(15)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QtGui.QColor(89, 145, 255))

		self.frame_body.setGraphicsEffect(self.shadow)
		self.label.mouseMoveEvent = self.moveWindow 


	def moveWindow(self,event):
		# MOVE WINDOW 
		if event.buttons() == QtCore.Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()

	def mousePressEvent(self,event):
		self.dragPos = event.globalPos()

class Dialog_ImportNick(QDialog,Form_Nick):
	def __init__(self,style,parent =None):
		super(Dialog_ImportNick,self).__init__(parent)
		self.setupUi(self)
		self.setStyleSheet(style)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.pushButton_close.clicked.connect(self.close)

		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(15)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QtGui.QColor(89, 145, 255))


		self.frame_body.setGraphicsEffect(self.shadow)
		self.label.mouseMoveEvent = self.moveWindow 




	def moveWindow(self,event):
		# MOVE WINDOW 
		if event.buttons() == QtCore.Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()

	def mousePressEvent(self,event):
		self.dragPos = event.globalPos()

# class TableView():
# 	pass


