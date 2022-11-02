# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 1000)
        MainWindow.setStyleSheet("background-color: rgb(3, 125, 107)")
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 861, 371))
        self.tableWidget.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.Print_cleaning = QtWidgets.QPushButton(self.centralwidget)
        self.Print_cleaning.setGeometry(QtCore.QRect(210, 580, 31, 23))
        self.Print_cleaning.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_cleaning.setObjectName("Print_cleaning")
        self.Print_customer = QtWidgets.QPushButton(self.centralwidget)
        self.Print_customer.setGeometry(QtCore.QRect(210, 630, 31, 23))
        self.Print_customer.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_customer.setObjectName("Print_customer")
        self.Print_service = QtWidgets.QPushButton(self.centralwidget)
        self.Print_service.setGeometry(QtCore.QRect(210, 880, 31, 23))
        self.Print_service.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_service.setObjectName("Print_service")
        self.Print_cl_sv = QtWidgets.QPushButton(self.centralwidget)
        self.Print_cl_sv.setGeometry(QtCore.QRect(210, 730, 31, 23))
        self.Print_cl_sv.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_cl_sv.setObjectName("Print_cl_sv")
        self.Print_dist = QtWidgets.QPushButton(self.centralwidget)
        self.Print_dist.setGeometry(QtCore.QRect(210, 780, 31, 23))
        self.Print_dist.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_dist.setObjectName("Print_dist")
        self.Print_rate = QtWidgets.QPushButton(self.centralwidget)
        self.Print_rate.setGeometry(QtCore.QRect(210, 830, 31, 23))
        self.Print_rate.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_rate.setObjectName("Print_rate")
        self.Print_prop = QtWidgets.QPushButton(self.centralwidget)
        self.Print_prop.setGeometry(QtCore.QRect(210, 930, 31, 23))
        self.Print_prop.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_prop.setObjectName("Print_prop")
        self.Print_order = QtWidgets.QPushButton(self.centralwidget)
        self.Print_order.setGeometry(QtCore.QRect(210, 680, 31, 23))
        self.Print_order.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_order.setObjectName("Print_order")
        self.Q_3_8_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Q_3_8_8.setGeometry(QtCore.QRect(430, 600, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Q_3_8_8.setFont(font)
        self.Q_3_8_8.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Q_3_8_8.setObjectName("Q_3_8_8")
        self.Q_3_8_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Q_3_8_9.setGeometry(QtCore.QRect(430, 640, 401, 31))
        self.Q_3_8_9.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Q_3_8_9.setObjectName("Q_3_8_9")
        self.Q_3_8_10 = QtWidgets.QPushButton(self.centralwidget)
        self.Q_3_8_10.setGeometry(QtCore.QRect(430, 680, 401, 31))
        self.Q_3_8_10.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Q_3_8_10.setObjectName("Q_3_8_10")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 510, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 16px;\n"
"font: \"Arial Black\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.Q_3_8_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Q_3_8_7.setGeometry(QtCore.QRect(670, 550, 41, 31))
        self.Q_3_8_7.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Q_3_8_7.setObjectName("Q_3_8_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 380, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 32px;\n"
"font: \"Arial Black\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.Q_3_8_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Q_3_8_1.setGeometry(QtCore.QRect(450, 470, 41, 31))
        self.Q_3_8_1.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Q_3_8_1.setObjectName("Q_3_8_1")
        self.Q_3_8_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Q_3_8_4.setGeometry(QtCore.QRect(780, 470, 41, 31))
        self.Q_3_8_4.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Q_3_8_4.setObjectName("Q_3_8_4")
        self.Q_3_8_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Q_3_8_6.setGeometry(QtCore.QRect(560, 550, 41, 31))
        self.Q_3_8_6.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Q_3_8_6.setObjectName("Q_3_8_6")
        self.Q_3_8_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Q_3_8_5.setGeometry(QtCore.QRect(450, 550, 41, 31))
        self.Q_3_8_5.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Q_3_8_5.setObjectName("Q_3_8_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(440, 429, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 16px;\n"
"font: \"Arial Black\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.Q_3_8_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Q_3_8_3.setGeometry(QtCore.QRect(670, 470, 41, 31))
        self.Q_3_8_3.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Q_3_8_3.setObjectName("Q_3_8_3")
        self.Q_3_8_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Q_3_8_2.setGeometry(QtCore.QRect(560, 470, 41, 31))
        self.Q_3_8_2.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Q_3_8_2.setObjectName("Q_3_8_2")
        self.Q_3_9_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Q_3_9_1.setGeometry(QtCore.QRect(430, 720, 401, 31))
        self.Q_3_9_1.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Q_3_9_1.setObjectName("Q_3_9_1")
        self.Q_3_9_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Q_3_9_3.setGeometry(QtCore.QRect(430, 800, 401, 31))
        self.Q_3_9_3.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Q_3_9_3.setObjectName("Q_3_9_3")
        self.Q_3_9_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Q_3_9_2.setGeometry(QtCore.QRect(430, 760, 401, 31))
        self.Q_3_9_2.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Q_3_9_2.setObjectName("Q_3_9_2")
        self.Q_3_9_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Q_3_9_4.setGeometry(QtCore.QRect(430, 840, 401, 31))
        self.Q_3_9_4.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Q_3_9_4.setObjectName("Q_3_9_4")
        self.Q_3_9_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Q_3_9_6.setGeometry(QtCore.QRect(430, 920, 401, 31))
        self.Q_3_9_6.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Q_3_9_6.setObjectName("Q_3_9_6")
        self.Q_3_9_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Q_3_9_5.setGeometry(QtCore.QRect(430, 880, 401, 31))
        self.Q_3_9_5.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Q_3_9_5.setObjectName("Q_3_9_5")
        self.add_client = QtWidgets.QPushButton(self.centralwidget)
        self.add_client.setGeometry(QtCore.QRect(280, 630, 31, 23))
        self.add_client.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.add_client.setObjectName("add_client")
        self.add_order = QtWidgets.QPushButton(self.centralwidget)
        self.add_order.setGeometry(QtCore.QRect(280, 680, 31, 23))
        self.add_order.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.add_order.setObjectName("add_order")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 380, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font: \"Arial Black\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 580, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font: \"Arial Black\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 630, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font: \"Arial Black\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 680, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font: \"Arial Black\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 730, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font: \"Arial Black\";")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 780, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font: \"Arial Black\";")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 880, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font: \"Arial Black\";")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 930, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font: \"Arial Black\";")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 830, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font: \"Arial Black\";")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.add_cleaning = QtWidgets.QPushButton(self.centralwidget)
        self.add_cleaning.setGeometry(QtCore.QRect(280, 580, 31, 23))
        self.add_cleaning.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.add_cleaning.setObjectName("add_cleaning")
        self.add_cl_sv = QtWidgets.QPushButton(self.centralwidget)
        self.add_cl_sv.setGeometry(QtCore.QRect(280, 730, 31, 23))
        self.add_cl_sv.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.add_cl_sv.setObjectName("add_cl_sv")
        self.add_dist = QtWidgets.QPushButton(self.centralwidget)
        self.add_dist.setGeometry(QtCore.QRect(280, 780, 31, 23))
        self.add_dist.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.add_dist.setObjectName("add_dist")
        self.add_rate = QtWidgets.QPushButton(self.centralwidget)
        self.add_rate.setGeometry(QtCore.QRect(280, 830, 31, 23))
        self.add_rate.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.add_rate.setObjectName("add_rate")
        self.add_service = QtWidgets.QPushButton(self.centralwidget)
        self.add_service.setGeometry(QtCore.QRect(280, 880, 31, 23))
        self.add_service.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.add_service.setObjectName("add_service")
        self.add_prop = QtWidgets.QPushButton(self.centralwidget)
        self.add_prop.setGeometry(QtCore.QRect(280, 930, 31, 23))
        self.add_prop.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.add_prop.setObjectName("add_prop")
        self.print = QtWidgets.QPushButton(self.centralwidget)
        self.print.setGeometry(QtCore.QRect(30, 450, 41, 31))
        self.print.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.print.setObjectName("print")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(30, 510, 41, 31))
        self.add.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.add.setObjectName("add")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(90, 450, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font: \"Arial Black\";")
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(90, 510, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font: \"Arial Black\";")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.print_2 = QtWidgets.QPushButton(self.centralwidget)
        self.print_2.setGeometry(QtCore.QRect(240, 450, 41, 31))
        self.print_2.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.print_2.setObjectName("print_2")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(300, 450, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"font: \"Arial Black\";")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.delete_cleaning = QtWidgets.QPushButton(self.centralwidget)
        self.delete_cleaning.setGeometry(QtCore.QRect(350, 580, 31, 23))
        self.delete_cleaning.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.delete_cleaning.setObjectName("delete_cleaning")
        self.delete_customer = QtWidgets.QPushButton(self.centralwidget)
        self.delete_customer.setGeometry(QtCore.QRect(350, 630, 31, 23))
        self.delete_customer.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.delete_customer.setObjectName("delete_customer")
        self.delete_order = QtWidgets.QPushButton(self.centralwidget)
        self.delete_order.setGeometry(QtCore.QRect(350, 680, 31, 23))
        self.delete_order.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.delete_order.setObjectName("delete_order")
        self.delete_cl_sv = QtWidgets.QPushButton(self.centralwidget)
        self.delete_cl_sv.setGeometry(QtCore.QRect(350, 730, 31, 23))
        self.delete_cl_sv.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.delete_cl_sv.setObjectName("delete_cl_sv")
        self.delete_dist = QtWidgets.QPushButton(self.centralwidget)
        self.delete_dist.setGeometry(QtCore.QRect(350, 780, 31, 23))
        self.delete_dist.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.delete_dist.setObjectName("delete_dist")
        self.delete_service = QtWidgets.QPushButton(self.centralwidget)
        self.delete_service.setGeometry(QtCore.QRect(350, 880, 31, 23))
        self.delete_service.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.delete_service.setObjectName("delete_service")
        self.delete_prop = QtWidgets.QPushButton(self.centralwidget)
        self.delete_prop.setGeometry(QtCore.QRect(350, 930, 31, 23))
        self.delete_prop.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.delete_prop.setObjectName("delete_prop")
        self.delete_rate = QtWidgets.QPushButton(self.centralwidget)
        self.delete_rate.setGeometry(QtCore.QRect(350, 830, 31, 23))
        self.delete_rate.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.delete_rate.setObjectName("delete_rate")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(240, 510, 161, 31))
        self.searchButton.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.searchButton.setObjectName("searchButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Курсовая работа БД Мамчур ПИ-20а"))
        self.Print_cleaning.setText(_translate("MainWindow", "П"))
        self.Print_customer.setText(_translate("MainWindow", "П"))
        self.Print_service.setText(_translate("MainWindow", "П"))
        self.Print_cl_sv.setText(_translate("MainWindow", "П"))
        self.Print_dist.setText(_translate("MainWindow", "П"))
        self.Print_rate.setText(_translate("MainWindow", "П"))
        self.Print_prop.setText(_translate("MainWindow", "П"))
        self.Print_order.setText(_translate("MainWindow", "П"))
        self.Q_3_8_8.setText(_translate("MainWindow", "левое внешнее соединение"))
        self.Q_3_8_9.setText(_translate("MainWindow", "правое внешнее соединение"))
        self.Q_3_8_10.setText(_translate("MainWindow", "запрос на запросе по принципу левого соединения "))
        self.label_5.setText(_translate("MainWindow", "симметричное внутреннее соединение без условия "))
        self.Q_3_8_7.setText(_translate("MainWindow", "3"))
        self.label_6.setText(_translate("MainWindow", "Выполнить запрос"))
        self.Q_3_8_1.setText(_translate("MainWindow", "1"))
        self.Q_3_8_4.setText(_translate("MainWindow", "4"))
        self.Q_3_8_6.setText(_translate("MainWindow", "2"))
        self.Q_3_8_5.setText(_translate("MainWindow", "1"))
        self.label_7.setText(_translate("MainWindow", "симметричное внутреннее соединение с условием"))
        self.Q_3_8_3.setText(_translate("MainWindow", "3"))
        self.Q_3_8_2.setText(_translate("MainWindow", "2"))
        self.Q_3_9_1.setText(_translate("MainWindow", "итоговый запрос без условия "))
        self.Q_3_9_3.setText(_translate("MainWindow", "итоговый запрос с условием на группы"))
        self.Q_3_9_2.setText(_translate("MainWindow", "итоговый запрос с условием на данные"))
        self.Q_3_9_4.setText(_translate("MainWindow", "итоговый запрос с условием на данные и на группы "))
        self.Q_3_9_6.setText(_translate("MainWindow", "запрос с подзапросом "))
        self.Q_3_9_5.setText(_translate("MainWindow", "запрос на запросе по принципу итогового запроса "))
        self.add_client.setText(_translate("MainWindow", "Д"))
        self.add_order.setText(_translate("MainWindow", "Д"))
        self.label_2.setText(_translate("MainWindow", "Вы работаете в режиме администратора!"))
        self.label_3.setText(_translate("MainWindow", "Химчистки"))
        self.label_4.setText(_translate("MainWindow", "Заказчики"))
        self.label_8.setText(_translate("MainWindow", "Заказы"))
        self.label_9.setText(_translate("MainWindow", "Услуги химчистки"))
        self.label_10.setText(_translate("MainWindow", "Районы"))
        self.label_11.setText(_translate("MainWindow", "Услуги"))
        self.label_12.setText(_translate("MainWindow", "Тип собственности"))
        self.label_13.setText(_translate("MainWindow", "Тарифы"))
        self.add_cleaning.setText(_translate("MainWindow", "Д"))
        self.add_cl_sv.setText(_translate("MainWindow", "Д"))
        self.add_dist.setText(_translate("MainWindow", "Д"))
        self.add_rate.setText(_translate("MainWindow", "Д"))
        self.add_service.setText(_translate("MainWindow", "Д"))
        self.add_prop.setText(_translate("MainWindow", "Д"))
        self.print.setText(_translate("MainWindow", "П"))
        self.add.setText(_translate("MainWindow", "Д"))
        self.label_14.setText(_translate("MainWindow", "- просмотреть"))
        self.label_15.setText(_translate("MainWindow", "- добавить"))
        self.print_2.setText(_translate("MainWindow", "У"))
        self.label_16.setText(_translate("MainWindow", "- удалить"))
        self.delete_cleaning.setText(_translate("MainWindow", "У"))
        self.delete_customer.setText(_translate("MainWindow", "У"))
        self.delete_order.setText(_translate("MainWindow", "У"))
        self.delete_cl_sv.setText(_translate("MainWindow", "У"))
        self.delete_dist.setText(_translate("MainWindow", "У"))
        self.delete_service.setText(_translate("MainWindow", "У"))
        self.delete_prop.setText(_translate("MainWindow", "У"))
        self.delete_rate.setText(_translate("MainWindow", "У"))
        self.searchButton.setText(_translate("MainWindow", "Поиск"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
