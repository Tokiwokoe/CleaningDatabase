import datetime
from PyQt5.QtWidgets import QDialog
from UiClass import AddProp, AddDist, AddRate, AddCleaning, AddClient, AddOrder
import connection


class AddClient(QDialog, AddClient.Ui_Dialog):
    def __init__(self):
        super(AddClient, self).__init__()
        self.setupUi(self)
        self.setFixedSize(740, 140)
        self.OKbutton.clicked.connect(self.correct_data)

    def correct_data(self):
        self.cursor = connection.connection.cursor()
        firstname = self.firstname.text()
        lastname = self.lastname.text()
        birthdate = self.dateEdit.text()
        socialstatus = self.socialstatus.text()
        raw_phone = self.phone.text()
        address = self.addres.text()
        new_phone = raw_phone.replace('+', '').replace('-', '')
        if len(new_phone) == 12:
            phone = ''
            phone = phone + new_phone[0:2] + '(' + new_phone[2:5] + ')' + new_phone[5:8] + '-' + new_phone[8:10] + '-' + new_phone[10:12]
        else:
            phone = new_phone
        if len(firstname) == 0 or len(lastname) == 0 or len(socialstatus) == 0 or len(new_phone) == 0 or len(address) == 0:
            self.error.setText('Заполните все поля!')
        elif len(firstname) > 30 or len(lastname) > 30 or len(socialstatus) > 128 or len(new_phone) > 30 or len(address) > 128:
            self.error.setText('Проверьте корректность заполнения полей!')
        elif firstname.strip().isalpha() and lastname.strip().isalpha() and socialstatus.strip().isalpha() and new_phone.strip().isalnum():
            try:
                query = 'SELECT id FROM "Customer" ORDER BY id DESC LIMIT 1'
                self.cursor.execute(query)
                self.id = self.cursor.fetchone()
                query = f"INSERT INTO \"Customer\" VALUES({int(self.id[0])+1}, '{firstname}', '{lastname}', '{birthdate}', '{socialstatus}', '{phone}', '{address}')"
                self.cursor.execute(query)
                connection.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception:
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')


class AddOrder(QDialog, AddOrder.Ui_Dialog):
    def __init__(self):
        super(AddOrder, self).__init__()
        self.setupUi(self)
        self.setFixedSize(740, 140)
        self.OKbutton.clicked.connect(self.correct_data)
        self.cursor = connection.connection.cursor()
        query = 'SELECT "Cleaningservice".id, cleaning_name, district_name, service, price FROM "Cleaningservice" LEFT JOIN "Cleaning" ON "Cleaningservice".cleaning_id = "Cleaning".id LEFT JOIN "Service" ON "Cleaningservice".service_id = "Service".id LEFT JOIN "District" ON "District".id = "Cleaning".district_id'
        self.cursor.execute(query)
        for t in self.cursor.fetchall():
            self.cl_sv_id.addItem(str(t))
        query = 'SELECT id, rate FROM "Rate"'
        self.cursor.execute(query)
        for t in self.cursor.fetchall():
            self.rate_id.addItem(str(t))

    def correct_data(self):
        customer = self.customer_id.text()
        cl_sv = self.cl_sv_id.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        rate = self.rate_id.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        cl_sv_id = str(cl_sv[0])
        rate_id = str(rate[0])
        if customer.isalnum() and cl_sv_id.isalnum() and rate_id.isalnum():
            try:
                x = datetime.datetime.now()
                current_date = str(x.strftime("%d"+'.'"%m"+'.'"%y"))
                query = 'SELECT id FROM "Order" ORDER BY id DESC LIMIT 1'
                self.cursor.execute(query)
                self.id = self.cursor.fetchone()
                query = f"SELECT id FROM \"District\" WHERE district_name = {cl_sv[2]}"
                self.cursor.execute(query)
                self.dist_id = self.cursor.fetchone()
                query = f"SELECT id FROM \"Cleaning\" WHERE cleaning_name = {cl_sv[1]} AND district_id = {self.dist_id[0]}"
                self.cursor.execute(query)
                self.cleaning_id = self.cursor.fetchone()
                query = f"SELECT id FROM \"Service\" WHERE service = {cl_sv[3]}"
                self.cursor.execute(query)
                self.service_id = self.cursor.fetchone()
                query = f"INSERT INTO \"Order\" VALUES({int(self.id[0]) + 1}, '{current_date}', {self.cleaning_id[0]}, {customer}, {rate_id}, {self.service_id[0]})"
                self.cursor.execute(query)
                connection.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception:
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')


class AddCleaning(QDialog, AddCleaning.Ui_Dialog):
    def __init__(self):
        super(AddCleaning, self).__init__()
        self.setupUi(self)
        self.setFixedSize(740, 140)
        self.OKbutton.clicked.connect(self.correct_data)
        self.cursor = connection.connection.cursor()
        query = 'SELECT id, district_name FROM "District"'
        self.cursor.execute(query)
        for t in self.cursor.fetchall():
            self.dist.addItem(str(t))
        query = 'SELECT id, property_type FROM "Property"'
        self.cursor.execute(query)
        for t in self.cursor.fetchall():
            self.prop.addItem(str(t))

    def correct_data(self):
        cleaning = self.cleaning.text()
        year_opened = self.year_opened.text()
        raw_phone = self.phone.text()
        new_phone = raw_phone.replace('+', '').replace('-', '')
        dist = self.dist.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        dist_id = str(dist[0])
        prop = self.prop.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        prop_id = str(prop[0])
        if 0 < len(cleaning) < 129 and len(new_phone) > 0 and 1900 < int(year_opened) < 2023 and year_opened.isalnum() and new_phone.isalnum():
            try:
                if len(new_phone) == 12:
                    phone = ''
                    phone = '+' + phone + new_phone[0:2] + '(' + new_phone[2:5] + ')' + new_phone[5:8] + '-' + new_phone[8:10] + '-' + new_phone[10:12]
                else:
                    phone = new_phone
                query = 'SELECT id FROM "Cleaning" ORDER BY id DESC LIMIT 1'
                self.cursor.execute(query)
                self.id = self.cursor.fetchone()
                query = f"INSERT INTO \"Cleaning\" VALUES({int(self.id[0]) + 1}, '{cleaning}', '{year_opened}', '{phone}', {dist_id}, {prop_id})"
                self.cursor.execute(query)
                connection.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception:
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')


class AddCleaningservice(QDialog):
    def __init__(self):
        super(AddCleaningservice, self).__init__()
        self.OKbutton.clicked.connect(self.correct_data)

    def correct_data(self):
        pass


class AddDistrict(QDialog, AddDist.Ui_Dialog):
    def __init__(self):
        super(AddDistrict, self).__init__()
        self.setupUi(self)
        self.setFixedSize(560, 150)
        self.OKbutton.clicked.connect(self.correct_data)

    def correct_data(self):
        self.cursor = connection.connection.cursor()
        dist = self.dist.text()
        query = 'SELECT id FROM "District" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        if 0 < len(dist) < 30:
            try:
                query = f"INSERT INTO \"District\" VALUES ({int(self.id[0])+1}, '{dist}')"
                self.cursor.execute(query)
                connection.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception:
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')


class AddRate(QDialog, AddRate.Ui_Dialog):
    def __init__(self):
        super(AddRate, self).__init__()
        self.setupUi(self)
        self.setFixedSize(560, 150)
        self.OKbutton.clicked.connect(self.correct_data)

    def correct_data(self):
        self.cursor = connection.connection.cursor()
        rate = self.rate.text()
        query = 'SELECT id FROM "Rate" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        if 0 < len(rate) < 30:
            try:
                query = f"INSERT INTO \"Rate\" VALUES ({int(self.id[0])+1}, '{rate}')"
                self.cursor.execute(query)
                connection.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception:
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')


class AddService(QDialog):
    def __init__(self):
        super(AddService, self).__init__()
        self.OKbutton.clicked.connect(self.correct_data)


class AddPropery(QDialog, AddProp.Ui_Dialog):
    def __init__(self):
        super(AddPropery, self).__init__()
        self.setupUi(self)
        self.setFixedSize(560, 150)
        self.OKbutton.clicked.connect(self.correct_data)

    def correct_data(self):
        self.cursor = connection.connection.cursor()
        prop = self.prop.text()
        query = 'SELECT id FROM "Property" ORDER BY id DESC LIMIT 1'
        self.cursor.execute(query)
        self.id = self.cursor.fetchone()
        if 0 < len(prop) < 30:
            try:
                query = f"INSERT INTO \"Property\" VALUES ({int(self.id[0])+1}, '{prop}')"
                self.cursor.execute(query)
                connection.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception:
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')
