import sys
import connection
from UiClass import LoginScreen, Window, AdminWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from AddClass import (
    AddCleaning,
    AddCleaningservice,
    AddClient,
    AddDistrict,
    AddOrder,
    AddPropery,
    AddRate,
    AddService
)
from DeleteClass import (
    DeleteCleaning,
    DeleteCleaningservice,
    DeleteClient,
    DeleteDistrict,
    DeleteOrder,
    DeletePropery,
    DeleteRate,
    DeleteService
)


class PrintTable(QMainWindow):
    def __init__(self):
        super(PrintTable, self).__init__()

    def to_print_table(self):
        i = 0
        for elem in self.rows:
            j = 0
            for t in elem:
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(t).strip()))
                j += 1
            i += 1
        i = 0
        self.tableWidget.resizeColumnsToContents()

    def to_print_cleaning(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT cleaning_name, year_opened, phone, district_name, property_type FROM "Cleaning" ' \
                'LEFT JOIN "District" ON "District".id = "Cleaning".district_id ' \
                'LEFT JOIN "Property" ON "Property".id = "Cleaning".property_id ' \
                'ORDER BY "Cleaning".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(5)
        self.labels = ['Название химчистки', 'Год открытия', 'Телефон', 'Район', 'Тип собственности']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_customer(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT firstname, lastname, birth_date, social_status, customer_phone, customer_address ' \
                'FROM "Customer" ORDER BY "Customer".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(6)
        self.labels = ['Имя', 'Фамилия', 'Дата рождения', 'Социальный статус', 'Телефон', 'Адрес']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_service(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT service, deadline FROM "Service" ORDER BY "Service".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['Услуга', 'Время выполнения (дн.)']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_cl_sv(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT cleaning_name, district_name, service, price FROM "Cleaningservice" ' \
                'LEFT JOIN "Cleaning" ON "Cleaning".id = "Cleaningservice".cleaning_id ' \
                'LEFT JOIN "Service" ON "Service".id = "Cleaningservice".service_id ' \
                'LEFT JOIN "District" ON "Cleaning".district_id = "District".id ' \
                'ORDER BY "Cleaningservice".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(4)
        self.labels = ['Название химчистки', 'Район', 'Услуга', 'Цена']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_dist(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT district_name FROM "District" ' \
                'ORDER BY "District".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(1)
        self.labels = ['Район']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_rate(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT rate FROM "Rate" ' \
                'ORDER BY "Rate".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(1)
        self.labels = ['Тариф']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_prop(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT property_type FROM "Property" ' \
                'ORDER BY "Property".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(1)
        self.labels = ['Тип собственности']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_order(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT firstname, lastname, service, cleaning_name, district_name, order_date, rate FROM "Order" ' \
                'LEFT JOIN "Customer" ON "Order".customer_id = "Customer".id ' \
                'LEFT JOIN "Rate" ON "Rate".id = "Order".rate_id ' \
                'LEFT JOIN "Cleaning" ON "Cleaning".id = "Order".cleaning_id ' \
                'LEFT JOIN "District" ON "District".id = "Cleaning".district_id ' \
                'LEFT JOIN "Service" ON "Service".id = "Order".service_id ' \
                'ORDER BY "Order".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(7)
        self.labels = ['Имя', 'Фамилия', 'Услуга', 'Название химчистки', 'Район', 'Дата заказа', 'Тариф']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_1(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT cleaning_name, district_name, year_opened, phone FROM "Cleaning" ' \
                'INNER JOIN "District" ON "District".id = "Cleaning".district_id ' \
                'WHERE "Cleaning".id > 4'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(4)
        self.labels = ['Название химчистки', 'Район', 'Год открытия', 'Телефон']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_2(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT cleaning_name, district_name, year_opened, phone FROM "Cleaning" ' \
                'INNER JOIN "District" ON "District".id = "Cleaning".district_id ' \
                'WHERE "District".id = 1'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(4)
        self.labels = ['Название химчистки', 'Район', 'Год открытия', 'Телефон']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_3(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT firstname, lastname, order_date FROM "Order" ' \
                'INNER JOIN "Customer" ON "Customer".id = "Order".customer_id ' \
                'WHERE birth_date BETWEEN \'15.05.1997\' AND \'29.12.2000\''
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(3)
        self.labels = ['Имя', 'Фамилия', 'Дата заказа']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_4(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT firstname, lastname, order_date FROM "Order" ' \
                'INNER JOIN "Customer" ON "Customer".id = "Order".customer_id ' \
                'WHERE order_date > \'01.01.2014\''
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(3)
        self.labels = ['Имя', 'Фамилия', 'Дата заказа']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_5(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT cleaning_name, phone, property_type FROM "Cleaning" ' \
                'INNER JOIN "Property" ON "Property".id = "Cleaning".property_id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(3)
        self.labels = ['Название химчистки', 'Телефон', 'Тип собственности']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_6(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT firstname, lastname, "Order".id FROM "Customer" ' \
                'INNER JOIN "Order" ON "Order".customer_id = "Customer".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(3)
        self.labels = ['Имя', 'Фамилия', 'ID заказа']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_7(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT cleaning_name, district_name, service FROM "Cleaning" ' \
                'INNER JOIN "Cleaningservice" ON "Cleaningservice".cleaning_id = "Cleaning".id ' \
                'INNER JOIN "Service" ON "Service".id = "Cleaningservice".service_id ' \
                'INNER JOIN "District" ON "District".id = "Cleaning".district_id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(3)
        self.labels = ['Название химчистки', 'Район', 'Услуга']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_8(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT firstname, lastname, "Order".id FROM "Customer" ' \
                'LEFT JOIN "Order" ON "Order".customer_id = "Customer".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(3)
        self.labels = ['Имя', 'Фамилия', 'ID заказа']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_9(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT firstname, lastname, "Order".id FROM "Customer" ' \
                'RIGHT JOIN "Order" ON "Order".customer_id = "Customer".id'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(3)
        self.labels = ['Имя', 'Фамилия', 'ID заказа']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_8_10(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT "Customer".id, firstname, lastname, order_date FROM "Customer" ' \
                'LEFT JOIN "Order" ON "Order".customer_id = "Customer".id ' \
                'WHERE lastname = ' \
                '(SELECT DISTINCT lastname FROM "Customer" WHERE lastname = \'Павловская\')'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(4)
        self.labels = ['ID заказчика', 'Имя', 'Фамилия', 'Дата заказа']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_9_1(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT cleaning_name, SUM(price) AS total_price FROM "Cleaning" ' \
                'LEFT JOIN "Cleaningservice" ON "Cleaningservice".cleaning_id = "Cleaning".id ' \
                'GROUP BY cleaning_name ' \
                'ORDER BY total_price DESC'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['Название химчистки', 'Сумма стоимости всех услуг']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_9_2(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT cleaning_name, SUM(price) AS total_price FROM "Cleaning" ' \
                'LEFT JOIN "Cleaningservice" ON "Cleaningservice".cleaning_id = "Cleaning".id ' \
                'WHERE cleaning_name NOT LIKE \'К%\' GROUP BY cleaning_name ' \
                'ORDER BY total_price DESC'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['Название химчистки', 'Сумма стоимости всех услуг']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_9_3(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT cleaning_name, SUM(price) AS total_price FROM "Cleaning" ' \
                'LEFT JOIN "Cleaningservice" ON "Cleaningservice".cleaning_id = "Cleaning".id ' \
                'GROUP BY cleaning_name ' \
                'HAVING SUM(price) > 2500 ' \
                'ORDER BY total_price DESC'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['Название химчистки', 'Сумма стоимости всех услуг']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_9_4(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT cleaning_name, SUM(price) AS total_price FROM "Cleaning" ' \
                'LEFT JOIN "Cleaningservice" ON "Cleaningservice".cleaning_id = "Cleaning".id ' \
                'WHERE cleaning_name NOT LIKE \'К%\' ' \
                'GROUP BY cleaning_name ' \
                'HAVING SUM(price) < 4000 ' \
                'ORDER BY total_price DESC'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['Название химчистки', 'Сумма стоимости всех услуг']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_9_5(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT "Customer".id, COUNT("Order".id) AS order_count FROM "Customer" ' \
                'LEFT JOIN "Order" ON "Order".customer_id = "Customer".id ' \
                'GROUP BY "Customer".id ' \
                'HAVING COUNT("Order".id) = ' \
                '(SELECT COUNT("Order".id) AS order_count FROM "Customer" ' \
                'GROUP BY order_count ' \
                'HAVING COUNT("Order".id) = 1) ' \
                'LIMIT 10'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(2)
        self.labels = ['ID заказчика', 'Количество заказов']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()

    def to_print_Q_3_9_6(self):
        self.cursor = connection.connection.cursor()
        query = 'SELECT cleaning_name, service, price FROM "Cleaningservice" ' \
                'LEFT JOIN "Cleaning" ON "Cleaning".id = "Cleaningservice".cleaning_id ' \
                'LEFT JOIN "Service" ON "Service".id = "Cleaningservice".service_id ' \
                'WHERE EXISTS ' \
                '(SELECT "Service".id FROM "Service" ' \
                'WHERE "Cleaningservice".cleaning_id = 2) ' \
                'ORDER BY price DESC'
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(3)
        self.labels = ['Название химчистки', 'Услуга', 'Стоимость']
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.to_print_table()


    def to_add_client(self):
        client = AddClient()
        client.exec_()

    def to_add_order(self):
        order = AddOrder()
        order.exec_()


class ClientWindow(PrintTable, Window.Ui_MainWindow):
    def __init__(self):
        super(ClientWindow, self).__init__()
        self.setupUi(self)
        self.setFixedSize(860, 1000)
        self.Print_cleaning.clicked.connect(self.to_print_cleaning)
        self.Print_customer.clicked.connect(self.to_print_customer)
        self.Print_service.clicked.connect(self.to_print_service)
        self.Print_cl_sv.clicked.connect(self.to_print_cl_sv)
        self.Print_dist.clicked.connect(self.to_print_dist)
        self.Print_prop.clicked.connect(self.to_print_prop)
        self.Print_rate.clicked.connect(self.to_print_rate)
        self.Print_order.clicked.connect(self.to_print_order)
        self.Q_3_8_1.clicked.connect(self.to_print_Q_3_8_1)
        self.Q_3_8_2.clicked.connect(self.to_print_Q_3_8_2)
        self.Q_3_8_3.clicked.connect(self.to_print_Q_3_8_3)
        self.Q_3_8_4.clicked.connect(self.to_print_Q_3_8_4)
        self.Q_3_8_5.clicked.connect(self.to_print_Q_3_8_5)
        self.Q_3_8_6.clicked.connect(self.to_print_Q_3_8_6)
        self.Q_3_8_7.clicked.connect(self.to_print_Q_3_8_7)
        self.Q_3_8_8.clicked.connect(self.to_print_Q_3_8_8)
        self.Q_3_8_9.clicked.connect(self.to_print_Q_3_8_9)
        self.Q_3_8_10.clicked.connect(self.to_print_Q_3_8_10)
        self.Q_3_9_1.clicked.connect(self.to_print_Q_3_9_1)
        self.Q_3_9_2.clicked.connect(self.to_print_Q_3_9_2)
        self.Q_3_9_3.clicked.connect(self.to_print_Q_3_9_3)
        self.Q_3_9_4.clicked.connect(self.to_print_Q_3_9_4)
        self.Q_3_9_5.clicked.connect(self.to_print_Q_3_9_5)
        self.Q_3_9_6.clicked.connect(self.to_print_Q_3_9_6)
        self.add_client.clicked.connect(self.to_add_client)
        self.add_order.clicked.connect(self.to_add_order)


class AdminWindow(PrintTable, AdminWindow.Ui_MainWindow):
    def __init__(self):
        super(AdminWindow, self).__init__()
        self.setupUi(self)
        self.setFixedSize(860, 1000)
        self.Print_cleaning.clicked.connect(self.to_print_cleaning)
        self.Print_customer.clicked.connect(self.to_print_customer)
        self.Print_service.clicked.connect(self.to_print_service)
        self.Print_cl_sv.clicked.connect(self.to_print_cl_sv)
        self.Print_dist.clicked.connect(self.to_print_dist)
        self.Print_prop.clicked.connect(self.to_print_prop)
        self.Print_rate.clicked.connect(self.to_print_rate)
        self.Print_order.clicked.connect(self.to_print_order)
        self.Q_3_8_1.clicked.connect(self.to_print_Q_3_8_1)
        self.Q_3_8_2.clicked.connect(self.to_print_Q_3_8_2)
        self.Q_3_8_3.clicked.connect(self.to_print_Q_3_8_3)
        self.Q_3_8_4.clicked.connect(self.to_print_Q_3_8_4)
        self.Q_3_8_5.clicked.connect(self.to_print_Q_3_8_5)
        self.Q_3_8_6.clicked.connect(self.to_print_Q_3_8_6)
        self.Q_3_8_7.clicked.connect(self.to_print_Q_3_8_7)
        self.Q_3_8_8.clicked.connect(self.to_print_Q_3_8_8)
        self.Q_3_8_9.clicked.connect(self.to_print_Q_3_8_9)
        self.Q_3_8_10.clicked.connect(self.to_print_Q_3_8_10)
        self.Q_3_9_1.clicked.connect(self.to_print_Q_3_9_1)
        self.Q_3_9_2.clicked.connect(self.to_print_Q_3_9_2)
        self.Q_3_9_3.clicked.connect(self.to_print_Q_3_9_3)
        self.Q_3_9_4.clicked.connect(self.to_print_Q_3_9_4)
        self.Q_3_9_5.clicked.connect(self.to_print_Q_3_9_5)
        self.Q_3_9_6.clicked.connect(self.to_print_Q_3_9_6)
        self.add_client.clicked.connect(self.to_add_client)
        self.add_order.clicked.connect(self.to_add_order)
        self.add_cleaning.clicked.connect(self.to_add_cleaning)
        self.add_dist.clicked.connect(self.to_add_dist)
        self.add_rate.clicked.connect(self.to_add_rate)
        self.add_prop.clicked.connect(self.to_add_prop)

    def to_add_cleaning(self):
        cleaning = AddCleaning()
        cleaning.exec_()

    def to_add_dist(self):
        dist = AddDistrict()
        dist.exec_()

    def to_add_rate(self):
        rate = AddRate()
        rate.exec_()

    def to_add_prop(self):
        prop = AddPropery()
        prop.exec_()


class AuthWindow(QDialog, LoginScreen.Ui_Auth):
    def __init__(self):
        super(AuthWindow, self).__init__()
        self.setupUi(self)
        self.setFixedSize(280, 290)
        self.login.clicked.connect(self.correct_login)

    def correct_login(self):
        user = self.loginfield.text()
        password = self.passwordfield.text()

        if len(user) == 0 or len(password) == 0:
            self.error.setText('Заполните все поля!')
        else:
            if user == 'admin' and password == 'admin':
                print('Connected as admin')
                global admin
                admin = AdminWindow()
                admin.show()
                self.close()
            elif user == 'customer' and password == 'customer':
                print('Connected as customer')
                global client
                client = ClientWindow()
                client.show()
                self.close()
            else:
                self.error.setText('Неверный пароль!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AuthWindow()

    window.show()
    sys.exit(app.exec_())
