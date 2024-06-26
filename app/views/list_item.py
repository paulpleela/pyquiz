# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_item.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget, QMainWindow, QLineEdit, QGridLayout, QLabel)

from PySide6 import QtCore, QtGui, QtWidgets
import requests

class ListItem(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.name = []
        self.buttons = []
        self.index = 0
        self.setupUi()  # Call setupUi here instead of updateAPI

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"MainWindow")
        self.resize(801, 551)
        
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 781, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 779, 489))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.updateAPI()  # Move updateAPI call here

        QMetaObject.connectSlotsByName(self)

    def updateAPI(self):
        self.buttons = []
        response = requests.get(f"http://127.0.0.1:8000/certifications/{self.username}")

        if response.status_code == 200:
            data = response.json()
            self.name = data["certifications"]

            # for loop making pushButton and Label
            self.index = 0
            for _ in range(len(self.name)):
                button = QPushButton(self.scrollAreaWidgetContents)
                button.setObjectName(f"pushButton_{self.index + 1}")
                button.setText(self.name[self.index]["courseName"])
                self.gridLayout.addWidget(button, self.index, 0, 1, 1)
                self.buttons.append(button)
                
                self.index += 1

            # makes verticalSpacer
            self.verticalSpacer = QSpacerItem(20, 378, QSizePolicy.Minimum, QSizePolicy.Expanding)
            self.gridLayout.addItem(self.verticalSpacer, self.index, 0, 1, 1)
