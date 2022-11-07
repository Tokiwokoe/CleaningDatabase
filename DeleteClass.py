from PyQt5.QtWidgets import QDialog
from UiClass import DeleteMessage, DeleteData
import connection


class DeleteMessage(QDialog, DeleteMessage.Ui_Dialog):
    def __init__(self):
        super(DeleteMessage, self).__init__()
        self.setupUi(self)
        self.setFixedSize(560, 150)
        self.cursor = connection.connection.cursor()
        query = f'SELECT * FROM {table} WHERE id = {id}'
        self.cursor.execute(query)
        self.text.setText(f'Вы действительно хотите удалить {self.cursor.fetchall()}')
        self.OKbutton.clicked.connect(self.delete)
        self.CancelButton.clicked.connect(self.cancel)

    def delete(self):
        try:
            query = f'DELETE FROM {table} WHERE id = {id}'
            self.cursor.execute(query)
            connection.connection.commit()
            self.error.setText('Удалено!')
        except Exception as err:
            print(err)
            self.error.setText('Ошибка!')

    def cancel(self):
        self.close()


class DeleteData(QDialog, DeleteData.Ui_Dialog):
    def __init__(self):
        super(DeleteData, self).__init__()
        self.setupUi(self)
        self.setFixedSize(450, 150)
        self.table.addItem('Химчистки')
        self.table.addItem('Заказчики')
        self.table.addItem('Заказы')
        self.table.addItem('Услуги химчистки')
        self.table.addItem('Районы')
        self.table.addItem('Тарифы')
        self.table.addItem('Услуги')
        self.table.addItem('Тип собственности')
        self.OKbutton.clicked.connect(self.to_delete)
        self.cursor = connection.connection.cursor()

    def to_delete(self):
        global id
        id = self.id.text()
        global table
        if self.table.currentText() == 'Химчистки':
            table = '"Cleaning"'
        elif self.table.currentText() == 'Заказчики':
            table = '"Customer"'
        elif self.table.currentText() == 'Заказы':
            table = '"Order"'
        elif self.table.currentText() == 'Услуги химчистки':
            table = '"Cleaningservice"'
        elif self.table.currentText() == 'Районы':
            table = '"District"'
        elif self.table.currentText() == 'Тарифы':
            table = '"Rate"'
        elif self.table.currentText() == 'Услуги':
            table = '"Service"'
        elif self.table.currentText() == 'Тип собственности':
            table = '"Property"'
        message = DeleteMessage()
        message.exec_()
