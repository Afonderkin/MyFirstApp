import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from ui import Ui_MainWindow
from new_transaction import Ui_Dialog
from db import DataBase


class NewTransaction(QDialog):
    def __init__(self):
        super(NewTransaction, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = DataBase()
        self.et = ExpensesTracker()
        self.et.show()

        self.ui.button_new_transaction.clicked.connect(self.add_new_transaction)

    def add_new_transaction(self):
        index = self.ui.cb_category.currentIndex()
        item = self.ui.cb_category.itemText(index)
        data = self.ui.data.text()
        ld = self.ui.le_description.text()
        lb = self.ui.le_balance.text()
        status_index = self.ui.comboBox_2.currentIndex()
        status = self.ui.comboBox_2.itemText(status_index)
        if ld and lb is not None:
            items = [item, data, ld, lb, status]
            row = self.et.ui.tableWidget.rowCount()
            column = self.et.ui.tableWidget.columnCount()
            self.et.ui.tableWidget.insertRow(row)
            self.et.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(row+1)))
            for i in range(len(items)):
                self.et.ui.tableWidget.setItem(row, i+1, QTableWidgetItem(str(items[i])))
            self.add_item_in_db(items)
            self.close()

    def add_item_in_db(self, items):
        self.db.add_row(items[0], items[1], items[2], items[3], items[4])
        self.et.update_db()

class EditTransaction(QDialog):
    def __init__(self, selectRow):
        super(EditTransaction, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.selectedRow = selectRow
        self.db = DataBase()
        self.et = ExpensesTracker()
        self.et.ui.tableWidget.selectRow(self.selectedRow)
        self.et.show()

        self.ui.lbl_new_transaction.setText('Изменить операцию')
        self.ui.button_new_transaction.setText('Изменить операцию')
        self.ui.button_new_transaction.clicked.connect(self.edit_transaction)

    def edit_transaction(self):
        index = self.ui.cb_category.currentIndex()
        item = self.ui.cb_category.itemText(index)
        data = self.ui.data.text()
        ld = self.ui.le_description.text()
        lb = self.ui.le_balance.text()
        status_index = self.ui.comboBox_2.currentIndex()
        status = self.ui.comboBox_2.itemText(status_index)
        if ld and lb is not None:
            items = [item, data, ld, lb, status]
            column = self.et.ui.tableWidget.columnCount()
            for i in range(len(items)):
                self.et.ui.tableWidget.setItem(self.selectedRow, i + 1, QTableWidgetItem(str(items[i])))
            self.edit_item_in_db(items)
            self.close()

    def edit_item_in_db(self, items):
        header_db = ['category', 'date', 'descriptions', 'balance', 'status']
        for i in range(len(items)):
            self.db.edit_row(self.selectedRow+1, header_db[i], items[i])
        self.et.update_db()


class ExpensesTracker(QMainWindow):
    def __init__(self):
        super(ExpensesTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = DataBase()

        self.ui.btn_add.clicked.connect(self.add_new_transaction)
        self.ui.btn_delete.clicked.connect(self.delete_transaction)
        self.ui.btn_edit.clicked.connect(self.edit_transaction)

        self.ui.tableWidget.setRowCount(len(self.db.select_transactions()))
        rows = self.ui.tableWidget.rowCount()
        columns = self.ui.tableWidget.columnCount()
        item = self.db.select_transactions()
        for row in range(rows):
            for column in range(columns):
                self.ui.tableWidget.setItem(row, column, QTableWidgetItem(str(item[row][column])))

    def add_new_transaction(self):
        self.other_window = NewTransaction()
        self.other_window.exec_()
        self.close()

    def delete_transaction(self):
        self.db = DataBase()
        row = self.ui.tableWidget.currentRow()
        if row > -1:
            self.ui.tableWidget.removeRow(row)
            self.ui.tableWidget.selectionModel().clearCurrentIndex()
            self.db.delete_row(row+1)
            self.update_db()

    def edit_transaction(self):
        row = self.ui.tableWidget.currentRow()
        if row > -1:
            self.other_window = EditTransaction(row)
            self.other_window.exec_()
            self.close()

    def update_db(self):
        self.db = DataBase()
        _translate = QCoreApplication.translate
        self.ui.lbl_balance.setText(_translate("MainWindow", f"{self.db.select_balance(1)} р"))
        self.ui.lbl_income_balance.setText(_translate("MainWindow", f"{self.db.select_balance(2)} р"))
        self.ui.lbl_outcome_balance.setText(_translate("MainWindow", f"{self.db.select_balance(3)} р"))
        self.ui.lbl_groceries_balance.setText(_translate("MainWindow", f"{self.db.select_outcome(0)} р"))
        self.ui.lbl_salary_balance.setText(_translate("MainWindow", f"{self.db.select_outcome(1)} р"))
        self.ui.lbl_electro_balance.setText(_translate("MainWindow", f"{self.db.select_outcome(2)} р"))
        self.ui.lbl_other_balance.setText(_translate("MainWindow", f"{self.db.select_outcome(3)} р"))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    db = DataBase()
    window = ExpensesTracker()
    window.show()
    sys.exit(app.exec())