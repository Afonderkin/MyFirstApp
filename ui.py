# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import res_rc
from db import DataBase

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(640, 480)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(174, 0, 255, 255), stop:0.681818 rgba(45, 27, 102, 255));\n"
"font: 12pt \"Calibri\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.balance_name = QtWidgets.QFrame(self.centralwidget)
        self.balance_name.setStyleSheet("background-color: rgba(255, 255, 255, 50);\n"
"border: 1px solid rgba(255, 255, 255, 60);\n"
"border-radius: 7px;")
        self.balance_name.setObjectName("balance_name")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.balance_name)
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_current_balance = QtWidgets.QLabel(self.balance_name)
        self.lbl_current_balance.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_current_balance.setObjectName("lbl_current_balance")
        self.verticalLayout.addWidget(self.lbl_current_balance)
        self.lbl_balance = QtWidgets.QLabel(self.balance_name)
        self.lbl_balance.setStyleSheet("color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_balance.setObjectName("lbl_balance")
        self.verticalLayout.addWidget(self.lbl_balance)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon_up_arrow = QtWidgets.QLabel(self.balance_name)
        self.icon_up_arrow.setMaximumSize(QtCore.QSize(24, 24))
        self.icon_up_arrow.setStyleSheet("background-color: none;\n"
"border: none;\n"
"padding-top: 10px;\n"
"")
        self.icon_up_arrow.setText("")
        self.icon_up_arrow.setPixmap(QtGui.QPixmap(":/icons/icons/north_east_FILL0_wght400_GRAD0_opsz48.svg"))
        self.icon_up_arrow.setScaledContents(False)
        self.icon_up_arrow.setObjectName("icon_up_arrow")
        self.horizontalLayout.addWidget(self.icon_up_arrow)
        self.lbl_income = QtWidgets.QLabel(self.balance_name)
        self.lbl_income.setStyleSheet("color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")
        self.lbl_income.setObjectName("lbl_income")
        self.horizontalLayout.addWidget(self.lbl_income)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lbl_income_balance = QtWidgets.QLabel(self.balance_name)
        self.lbl_income_balance.setStyleSheet("color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_income_balance.setObjectName("lbl_income_balance")
        self.verticalLayout.addWidget(self.lbl_income_balance)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.icon_down_arrow = QtWidgets.QLabel(self.balance_name)
        self.icon_down_arrow.setMaximumSize(QtCore.QSize(24, 24))
        self.icon_down_arrow.setStyleSheet("background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.icon_down_arrow.setText("")
        self.icon_down_arrow.setPixmap(QtGui.QPixmap(":/icons/icons/south_east_FILL0_wght400_GRAD0_opsz48.svg"))
        self.icon_down_arrow.setObjectName("icon_down_arrow")
        self.horizontalLayout_2.addWidget(self.icon_down_arrow)
        self.lbl_outcome = QtWidgets.QLabel(self.balance_name)
        self.lbl_outcome.setStyleSheet("color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")
        self.lbl_outcome.setObjectName("lbl_outcome")
        self.horizontalLayout_2.addWidget(self.lbl_outcome)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lbl_outcome_balance = QtWidgets.QLabel(self.balance_name)
        self.lbl_outcome_balance.setStyleSheet("color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_outcome_balance.setObjectName("lbl_outcome_balance")
        self.verticalLayout.addWidget(self.lbl_outcome_balance)
        self.horizontalLayout_7.addWidget(self.balance_name)
        self.category_frame = QtWidgets.QWidget(self.centralwidget)
        self.category_frame.setStyleSheet("background-color: rgba(255, 255, 255, 50);\n"
"border: 1px solid rgba(255, 255, 255, 60);\n"
"border-radius: 7px;")
        self.category_frame.setObjectName("category_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.category_frame)
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_expenses_category = QtWidgets.QLabel(self.category_frame)
        self.lbl_expenses_category.setStyleSheet("color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_expenses_category.setObjectName("lbl_expenses_category")
        self.verticalLayout_2.addWidget(self.lbl_expenses_category)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.icon_groceries = QtWidgets.QLabel(self.category_frame)
        self.icon_groceries.setMaximumSize(QtCore.QSize(24, 24))
        self.icon_groceries.setStyleSheet("background-color: none;\n"
"border: none;\n"
"")
        self.icon_groceries.setText("")
        self.icon_groceries.setPixmap(QtGui.QPixmap(":/icons/icons/shopping_cart_FILL0_wght400_GRAD0_opsz48.svg"))
        self.icon_groceries.setObjectName("icon_groceries")
        self.horizontalLayout_3.addWidget(self.icon_groceries)
        self.lbl_groceries = QtWidgets.QLabel(self.category_frame)
        self.lbl_groceries.setStyleSheet("color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;")
        self.lbl_groceries.setObjectName("lbl_groceries")
        self.horizontalLayout_3.addWidget(self.lbl_groceries)
        self.lbl_groceries_balance = QtWidgets.QLabel(self.category_frame)
        self.lbl_groceries_balance.setStyleSheet("color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.lbl_groceries_balance.setObjectName("lbl_groceries_balance")
        self.horizontalLayout_3.addWidget(self.lbl_groceries_balance)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.icon_salary = QtWidgets.QLabel(self.category_frame)
        self.icon_salary.setMaximumSize(QtCore.QSize(24, 24))
        self.icon_salary.setStyleSheet("background-color: none;\n"
"border: none;")
        self.icon_salary.setText("")
        self.icon_salary.setPixmap(QtGui.QPixmap(":/icons/icons/currency_ruble_FILL0_wght400_GRAD0_opsz48.svg"))
        self.icon_salary.setObjectName("icon_salary")
        self.horizontalLayout_4.addWidget(self.icon_salary)
        self.lbl_salary = QtWidgets.QLabel(self.category_frame)
        self.lbl_salary.setStyleSheet("color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;")
        self.lbl_salary.setObjectName("lbl_salary")
        self.horizontalLayout_4.addWidget(self.lbl_salary)
        self.lbl_salary_balance = QtWidgets.QLabel(self.category_frame)
        self.lbl_salary_balance.setStyleSheet("color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.lbl_salary_balance.setObjectName("lbl_salary_balance")
        self.horizontalLayout_4.addWidget(self.lbl_salary_balance)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.icon_electro = QtWidgets.QLabel(self.category_frame)
        self.icon_electro.setMaximumSize(QtCore.QSize(24, 24))
        self.icon_electro.setStyleSheet("background-color: none;\n"
"border: none;")
        self.icon_electro.setText("")
        self.icon_electro.setPixmap(QtGui.QPixmap(":/icons/icons/flash_on_FILL0_wght400_GRAD0_opsz48.svg"))
        self.icon_electro.setObjectName("icon_electro")
        self.horizontalLayout_5.addWidget(self.icon_electro)
        self.lbl_electro = QtWidgets.QLabel(self.category_frame)
        self.lbl_electro.setStyleSheet("color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;")
        self.lbl_electro.setObjectName("lbl_electro")
        self.horizontalLayout_5.addWidget(self.lbl_electro)
        self.lbl_electro_balance = QtWidgets.QLabel(self.category_frame)
        self.lbl_electro_balance.setStyleSheet("color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.lbl_electro_balance.setObjectName("lbl_electro_balance")
        self.horizontalLayout_5.addWidget(self.lbl_electro_balance)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.icon_other = QtWidgets.QLabel(self.category_frame)
        self.icon_other.setMaximumSize(QtCore.QSize(24, 24))
        self.icon_other.setStyleSheet("background-color: none;\n"
"border: none;")
        self.icon_other.setText("")
        self.icon_other.setPixmap(QtGui.QPixmap(":/icons/icons/other_admission_FILL0_wght400_GRAD0_opsz48.svg"))
        self.icon_other.setObjectName("icon_other")
        self.horizontalLayout_6.addWidget(self.icon_other)
        self.lbl_other = QtWidgets.QLabel(self.category_frame)
        self.lbl_other.setStyleSheet("color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;")
        self.lbl_other.setObjectName("lbl_other")
        self.horizontalLayout_6.addWidget(self.lbl_other)
        self.lbl_other_balance = QtWidgets.QLabel(self.category_frame)
        self.lbl_other_balance.setStyleSheet("color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.lbl_other_balance.setObjectName("lbl_other_balance")
        self.horizontalLayout_6.addWidget(self.lbl_other_balance)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addWidget(self.category_frame)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 50);\n"
"border: 1px solid rgba(255, 255, 255, 60);\n"
"border-radius: 7px;\n"
"widht: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 60);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 90);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/add_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add.setIcon(icon)
        self.btn_add.setIconSize(QtCore.QSize(24, 24))
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout_8.addWidget(self.btn_add)
        self.btn_edit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edit.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 50);\n"
"border: 1px solid rgba(255, 255, 255, 60);\n"
"border-radius: 7px;\n"
"widht: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 60);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 90);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/edit_square_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_edit.setIcon(icon1)
        self.btn_edit.setIconSize(QtCore.QSize(24, 24))
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout_8.addWidget(self.btn_edit)
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 50);\n"
"border: 1px solid rgba(255, 255, 255, 60);\n"
"border-radius: 7px;\n"
"widht: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 60);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 90);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/delete_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon2)
        self.btn_delete.setIconSize(QtCore.QSize(24, 24))
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout_8.addWidget(self.btn_delete)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"background-color: rgba(255, 255, 255, 50);\n"
"border: 1px solid rgba(255, 255, 255, 60);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"QHeaderView::section{\n"
"background-color: rgba(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"QTableWidget::item{\n"
"color: white;\n"
"border-style: none;\n"
"border-bottom: 1px solid rgba(255, 255, 255, 70);\n"
"}\n"
"QTableWidget::item:selected{\n"
"border: none;\n"
"color: rgba(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(105)
        self.verticalLayout_3.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Expense tracker"))
        self.lbl_current_balance.setText(_translate("MainWindow", "Текущий баланс"))
        self.lbl_balance.setText(_translate("MainWindow", f"{DataBase.select_balance(self, 1)} р"))
        self.lbl_income.setText(_translate("MainWindow", "Прибыль"))
        self.lbl_income_balance.setText(_translate("MainWindow", f"{DataBase.select_balance(self, 2)} р"))
        self.lbl_outcome.setText(_translate("MainWindow", "Расход"))
        self.lbl_outcome_balance.setText(_translate("MainWindow", f"{DataBase.select_balance(self, 3)} р"))
        self.lbl_expenses_category.setText(_translate("MainWindow", "Категория расходов"))
        self.lbl_groceries.setText(_translate("MainWindow", "Сырьё"))
        self.lbl_groceries_balance.setText(_translate("MainWindow", f"{DataBase.select_outcome(self, 0)} р"))
        self.lbl_salary.setText(_translate("MainWindow", "Зарплата"))
        self.lbl_salary_balance.setText(_translate("MainWindow", f"{DataBase.select_outcome(self, 1)} р"))
        self.lbl_electro.setText(_translate("MainWindow", "Электр-во"))
        self.lbl_electro_balance.setText(_translate("MainWindow", f"{DataBase.select_outcome(self, 2)} р"))
        self.lbl_other.setText(_translate("MainWindow", "Прочее"))
        self.lbl_other_balance.setText(_translate("MainWindow", f"{DataBase.select_outcome(self, 3)} р"))
        self.btn_add.setText(_translate("MainWindow", "Добавить операцию"))
        self.btn_edit.setText(_translate("MainWindow", "Изменить операцию"))
        self.btn_delete.setText(_translate("MainWindow", "Удалить операцию"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Категория"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Описание"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Баланс"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Статус"))