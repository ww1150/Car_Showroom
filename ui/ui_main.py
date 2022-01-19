# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainULtABE.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QComboBox, QHBoxLayout, QLabel, QMenuBar, QPushButton,
                               QStatusBar, QTableWidget, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(741, 524)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(610, 20, 111, 31))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.saveButton = QPushButton(self.verticalLayoutWidget_3)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout_3.addWidget(self.saveButton)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 20, 581, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableName = QLabel(self.horizontalLayoutWidget)
        self.tableName.setObjectName(u"tableName")
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.tableName.setFont(font)
        self.tableName.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.tableName)

        self.tableSelect = QComboBox(self.horizontalLayoutWidget)
        self.tableSelect.setObjectName(u"tableSelect")

        self.horizontalLayout.addWidget(self.tableSelect)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 8)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(610, 430, 111, 31))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.updateButton = QPushButton(self.verticalLayoutWidget_2)
        self.updateButton.setObjectName(u"updateButton")

        self.verticalLayout_2.addWidget(self.updateButton)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 50, 581, 411))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(610, 60, 111, 71))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.addButton = QPushButton(self.verticalLayoutWidget)
        self.addButton.setObjectName(u"addButton")

        self.verticalLayout.addWidget(self.addButton)

        self.removeButton = QPushButton(self.verticalLayoutWidget)
        self.removeButton.setObjectName(u"removeButton")

        self.verticalLayout.addWidget(self.removeButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 741, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.saveButton.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tableName.setText(
            QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430:", None))
        # if QT_CONFIG(tooltip)
        self.tableSelect.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.tableSelect.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                       u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443",
                                                                       None))
        self.updateButton.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.addButton.setText(
            QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.removeButton.setText(
            QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi
