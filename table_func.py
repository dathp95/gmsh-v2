from dialog import *
from PyQt5 import QtCore, QtGui, QtWidgets



class Table:
	#self: Parameter
	def createFile(self):
		file_name = self.form_file.lineEdit_file.text().strip()
		if file_name =='':
			msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='warning',
			boldtext='Lỗi tên file',
			text ='Tên file không thể để trống',
			ok =True,
			cancel = False)
			msg.exec_

			return
		elif os.path.isfile(f'data/{file_name}.txt'):
			msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='warning',
			boldtext='Lỗi tên file',
			text ='File đã tồn tại vui lòng đặt tên khác!',
			ok =True,
			cancel = False)
			msg.exec_()		
			return
		elif'/' in file_name or '\\' in file_name:
			msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='warning',
			boldtext='Lỗi tên file',
			text ='Tên file không được chứa kí tự đặc biệt',
			ok =True,
			cancel = False)
			msg.exec_()		
			return

		open(f'data/{file_name}.txt','w')
		msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='information',
			boldtext='Thành công',
			text =f'Tạo thành công file {file_name}',
			ok =True,
			cancel = False)		
		
		if msg.exec() == 1:			
			self.form_file.close()

		self.comboBox.insertItem(0,file_name)
		self.comboBox.setCurrentText(file_name)
		try:
			self.import_nick.comboBox_list_file.insertItem(0,file_name)
			self.import_nick.comboBox_list_file.setCurrentText(file_name)
		except:
			pass

		return
	def deleteFile(self):
		file_name = self.comboBox.currentText()
		msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='question',
			boldtext='Thông báo',
			text =f"Bạn chắc chắn muốn xóa file {file_name}?",
			ok =True,
			cancel = True)
		
		if msg.exec()==1:
			os.remove(f'data/{file_name}.txt')
			index = self.comboBox.findText(file_name)  # find the index of text
			self.comboBox.removeItem(index)  # remove item from index
		
		return

	def setItemImportNick(self):		
		self.import_nick.comboBox_list_file.addItems(filename.replace('.txt','') for filename in os.listdir('data'))
		self.import_nick.comboBox_list_file.setCurrentText(self.comboBox.currentText())
		print(self.comboBox.currentText())

	def saveFileNick(self):
		file_name = self.import_nick.comboBox_list_file.currentText().strip()
		data_nick = list(filter(None,self.import_nick.textEdit_import_nick.toPlainText().strip().split('\n')))
		print(data_nick)
		if file_name=='':
			msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='question',
			boldtext='Thông báo',
			text =f"Tên file trống, cần khởi tạo!",
			ok =True,
			cancel = False)
			msg.exec_()
			return
		elif len(data_nick) <= 0:
			msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='question',
			boldtext='Thông báo',
			text =f"Vui lòng nhập tài khoản cần lưu",
			ok =True,
			cancel = False)
			msg.exec_()
			return

		with open(f'data/{file_name}.txt','a', encoding ='utf-8') as f: 
			for data in data_nick:
				f.write(data+'\n')

		msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='information',
			boldtext='Thành công',
			text =f'Đã lưu {len(data_nick)} tài khoản vào file {file_name}',
			ok =True,
			cancel = True)		
		
		if msg.exec() == 1:			
			self.import_nick.close()

		return

	def setNickOnTable(self):
		file_name = self.comboBox.currentText()
		with open(f'data/{file_name}.txt','r') as f:
			list_data_nick = f.readlines()		
		
		

		list_data_info = [data.replace('\n','') for data in list_data_nick]
		self.tableWidget.setRowCount(len(list_data_info))
		print(list_data_info)
		for index, item in enumerate(list_data_info):
			
			taikhoan = item.split('|')[0]
			matkhau = item.split('|')[1]
			taikhoan_widget = QtWidgets.QTableWidgetItem(taikhoan)
			matkhau_widget = QtWidgets.QTableWidgetItem(matkhau)

			
			self.tableWidget.setItem(index,1,taikhoan_widget)
			self.tableWidget.setItem(index,2,matkhau_widget)


		

		return


		




		





