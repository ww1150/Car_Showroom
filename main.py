import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem

from ui import ui_main
from database import Database

db = Database()


class MainWindow(QtWidgets.QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)

        self.addButton.clicked.connect(self.add_button_action)
        self.updateButton.clicked.connect(self.update_button_action)
        self.removeButton.clicked.connect(self.remove_button_action)
        self.saveButton.clicked.connect(self.save_button_action)

        self.tableSelect.addItems(db.get_table_comments())
        self.tableSelect.currentIndexChanged.connect(self.table_select_action)

        self.addButton.setDisabled(True)
        self.updateButton.setDisabled(True)
        self.removeButton.setDisabled(True)
        self.saveButton.setDisabled(True)

        self.index = self.tableSelect.currentIndex
        self.rows = None

    def update(self):
        # Вывод записей
        self.rows = db.get_table_rows(self.index())
        self.tableWidget.setRowCount(len(self.rows))
        for ri, row in enumerate(self.rows):
            for ci, col in enumerate(row):
                self.tableWidget.setItem(ri, ci, QTableWidgetItem(str(col)))

    def table_select_action(self, index):
        # Установка названий колонок
        column_names = db.get_table_column_names(index)
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setHorizontalHeaderLabels(column_names)
        self.addButton.setDisabled(False)
        self.updateButton.setDisabled(False)
        self.removeButton.setDisabled(False)
        self.saveButton.setDisabled(False)
        self.update()

    def add_button_action(self):
        row_pos = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_pos)
        self.tableWidget.setItem(row_pos, 0, QTableWidgetItem(str(row_pos + 1)))

    def update_button_action(self):
        self.table_select_action(self.index())

    def remove_button_action(self):
        el = self.tableWidget.item(self.tableWidget.currentRow(), 0)
        if el:
            db.remove_row_in_table(self.index(), el.text())
        self.update()

    def save_button_action(self):
        tw = self.tableWidget
        col_len = len(db.get_table_column_names(self.index()))
        items = list()
        for r in range(tw.rowCount()):
            temp = list()
            for c in range(col_len):
                temp.append(tw.item(r, c).text())
            items.append(temp)
        db.update_data(self.index(), items)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(753, 504)
    window.setWindowTitle('База данных: Автосалон')
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
