# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QObject, Signal, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import views.resource_rc

from views.list_item import ListItem
from views.quiz_page import QuizPage
from views.calendar import Calendar
from views.lesson_pdf import LessonPDF
from views.course_list import Course_list
from views.lesson_quiz_list import Lesson_Quiz_list
from views.stacked_course import Stacked_Course
from views.teacher_stacked_course import Teacher_Stacked_Course
from views.stacked_certificate import Stacked_Certificate
from views.dashboard import Dashboard

class Sidebar(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 600)
        self.role = MainWindow.role
        self.username = MainWindow.username

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.logo_label_1 = QLabel(self.icon_only_widget)
        self.logo_label_1.setObjectName(u"logo_label_1")
        self.logo_label_1.setMinimumSize(QSize(50, 50))
        self.logo_label_1.setMaximumSize(QSize(50, 50))
        self.logo_label_1.setPixmap(QPixmap(u":/icon/icon/Logo.png"))
        self.logo_label_1.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.logo_label_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dashboard_btn_1 = QPushButton(self.icon_only_widget)
        self.dashboard_btn_1.setObjectName(u"dashboard_btn_1")
        icon = QIcon()
        icon.addFile(u":/icon/icon/home-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icon/icon/home-4-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_btn_1.setIcon(icon)
        self.dashboard_btn_1.setIconSize(QSize(20, 20))
        self.dashboard_btn_1.setCheckable(True)
        self.dashboard_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_btn_1)

        self.calendar_btn_1 = QPushButton(self.icon_only_widget)
        self.calendar_btn_1.setObjectName(u"calendar_btn_1")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/dashboard-5-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icon/icon/dashboard-5-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.calendar_btn_1.setIcon(icon1)
        self.calendar_btn_1.setIconSize(QSize(20, 20))
        self.calendar_btn_1.setCheckable(True)
        self.calendar_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.calendar_btn_1)

        self.mycourses_btn_1 = QPushButton(self.icon_only_widget)
        self.mycourses_btn_1.setObjectName(u"mycourses_btn_1")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/activity-feed-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icon/icon/activity-feed-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.mycourses_btn_1.setIcon(icon2)
        self.mycourses_btn_1.setIconSize(QSize(20, 20))
        self.mycourses_btn_1.setCheckable(True)
        self.mycourses_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.mycourses_btn_1)

        self.certificates_btn_1 = QPushButton(self.icon_only_widget)
        self.certificates_btn_1.setObjectName(u"certificates_btn_1")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/product-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icon/icon/product-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.certificates_btn_1.setIcon(icon3)
        self.certificates_btn_1.setIconSize(QSize(20, 20))
        self.certificates_btn_1.setCheckable(True)
        self.certificates_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.certificates_btn_1)

        # self.customers_btn_1 = QPushButton(self.icon_only_widget)
        # self.customers_btn_1.setObjectName(u"customers_btn_1")
        # icon4 = QIcon()
        # icon4.addFile(u":/icon/icon/group-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        # icon4.addFile(u":/icon/icon/group-48.ico", QSize(), QIcon.Normal, QIcon.On)
        # self.customers_btn_1.setIcon(icon4)
        # self.customers_btn_1.setIconSize(QSize(20, 20))
        # self.customers_btn_1.setCheckable(True)
        # self.customers_btn_1.setAutoExclusive(True)

        # self.verticalLayout.addWidget(self.customers_btn_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 375, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exit_btn_1 = QPushButton(self.icon_only_widget)
        self.exit_btn_1.setObjectName(u"exit_btn_1")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/account-logout-64.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn_1.setIcon(icon5)
        self.exit_btn_1.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.exit_btn_1)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.full_menu_widget = QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName(u"full_menu_widget")
        self.verticalLayout_4 = QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo_label_2 = QLabel(self.full_menu_widget)
        self.logo_label_2.setObjectName(u"logo_label_2")
        self.logo_label_2.setMinimumSize(QSize(40, 40))
        self.logo_label_2.setMaximumSize(QSize(40, 40))
        self.logo_label_2.setPixmap(QPixmap(u":/icon/icon/Logo.png"))
        self.logo_label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo_label_2)

        self.logo_label_3 = QLabel(self.full_menu_widget)
        self.logo_label_3.setObjectName(u"logo_label_3")
        font = QFont()
        font.setPointSize(15)
        self.logo_label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.logo_label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dashboard_btn_2 = QPushButton(self.full_menu_widget)
        self.dashboard_btn_2.setObjectName(u"dashboard_btn_2")
        self.dashboard_btn_2.setIcon(icon)
        self.dashboard_btn_2.setIconSize(QSize(14, 14))
        self.dashboard_btn_2.setCheckable(True)
        self.dashboard_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_btn_2)

        self.calendar_btn_2 = QPushButton(self.full_menu_widget)
        self.calendar_btn_2.setObjectName(u"calendar_btn_2")
        self.calendar_btn_2.setIcon(icon1)
        self.calendar_btn_2.setIconSize(QSize(14, 14))
        self.calendar_btn_2.setCheckable(True)
        self.calendar_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.calendar_btn_2)

        self.mycourses_btn_2 = QPushButton(self.full_menu_widget)
        self.mycourses_btn_2.setObjectName(u"mycourses_btn_2")
        self.mycourses_btn_2.setIcon(icon2)
        self.mycourses_btn_2.setIconSize(QSize(14, 14))
        self.mycourses_btn_2.setCheckable(True)
        self.mycourses_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.mycourses_btn_2)

        self.certificates_btn_2 = QPushButton(self.full_menu_widget)
        self.certificates_btn_2.setObjectName(u"certificates_btn_2")
        self.certificates_btn_2.setIcon(icon3)
        self.certificates_btn_2.setIconSize(QSize(14, 14))
        self.certificates_btn_2.setCheckable(True)
        self.certificates_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.certificates_btn_2)

        # self.customers_btn_2 = QPushButton(self.full_menu_widget)
        # self.customers_btn_2.setObjectName(u"customers_btn_2")
        # self.customers_btn_2.setIcon(icon4)
        # self.customers_btn_2.setIconSize(QSize(14, 14))
        # self.customers_btn_2.setCheckable(True)
        # self.customers_btn_2.setAutoExclusive(True)

        # self.verticalLayout_2.addWidget(self.customers_btn_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 373, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.exit_btn_2 = QPushButton(self.full_menu_widget)
        self.exit_btn_2.setObjectName(u"exit_btn_2")
        self.exit_btn_2.setIcon(icon5)
        self.exit_btn_2.setIconSize(QSize(14, 14))

        self.verticalLayout_4.addWidget(self.exit_btn_2)


        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.change_btn = QPushButton(self.widget)
        self.change_btn.setObjectName(u"change_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/menu-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.change_btn.setIcon(icon6)
        self.change_btn.setIconSize(QSize(14, 14))
        self.change_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.change_btn)

        self.horizontalSpacer = QSpacerItem(236, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(236, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        # self.user_btn = QPushButton(self.widget)
        # self.user_btn.setObjectName(u"user_btn")
        # icon8 = QIcon()
        # icon8.addFile(u":/icon/icon/user-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        # self.user_btn.setIcon(icon8)

        # self.horizontalLayout_4.addWidget(self.user_btn)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        
        ################################################
        dashboard = Dashboard(self.username)
        self.page = dashboard
        
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        
        #################
        calendar = Calendar(None)
        self.page_2 = calendar

        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        ###################
        
        if self.role == "teacher":
            stack_course = Teacher_Stacked_Course()
        else:
            stack_course = Stacked_Course(self.username)

        self.page_3 = stack_course
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)
        
        # self.page_3 = QStackedWidget()
        # self.course_list = Course_list()
        # self.course_list.setObjectName(u"page_3")
        # self.gridLayout_4 = QGridLayout(self.course_list)
        # self.gridLayout_4.setObjectName(u"gridLayout_4")
        # self.label_6 = QLabel(self.course_list)
        # self.label_6.setObjectName(u"label_6")
        # self.label_6.setFont(font1)
        # self.label_6.setAlignment(Qt.AlignCenter)

        # self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
    
        
        # self.page_3.addWidget(self.course_list)
        
        # self.lq_list = Lesson_Quiz_list()
        # self.lq_list.setObjectName(u"page_3_5")
        # self.gridLayout_4 = QGridLayout(self.lq_list)
        # self.gridLayout_4.setObjectName(u"gridLayout_4")
        # self.label_6 = QLabel(self.lq_list)
        # self.label_6.setObjectName(u"label_6")
        # self.label_6.setFont(font1)
        # self.label_6.setAlignment(Qt.AlignCenter)
        
        # self.page_3.addWidget(self.lq_list)
        
        #####################
        
        stack_certificate = Stacked_Certificate(self.username)
        self.page_4 = stack_certificate
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_5 = QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        #####################
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_6 = QGridLayout(self.page_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_8 = QLabel(self.page_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        #####################
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_7 = QGridLayout(self.page_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_9 = QLabel(self.page_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_6)
        ####################
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_8 = QGridLayout(self.page_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_10 = QLabel(self.page_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_7)
        #####################

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.change_btn.toggled.connect(self.icon_only_widget.setVisible)
        self.change_btn.toggled.connect(self.full_menu_widget.setHidden)
        self.dashboard_btn_1.toggled.connect(self.dashboard_btn_2.setChecked)
        self.calendar_btn_1.toggled.connect(self.calendar_btn_2.setChecked)
        self.mycourses_btn_1.toggled.connect(self.mycourses_btn_2.setChecked)
        self.certificates_btn_1.toggled.connect(self.certificates_btn_2.setChecked)
        # self.customers_btn_1.toggled.connect(self.customers_btn_2.setChecked)
        self.dashboard_btn_2.toggled.connect(self.dashboard_btn_1.setChecked)
        self.calendar_btn_2.toggled.connect(self.calendar_btn_1.setChecked)
        self.mycourses_btn_2.toggled.connect(self.mycourses_btn_1.setChecked)
        self.certificates_btn_2.toggled.connect(self.certificates_btn_1.setChecked)
        # self.customers_btn_2.toggled.connect(self.customers_btn_1.setChecked)
        self.exit_btn_2.clicked.connect(MainWindow.close)
        self.exit_btn_1.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(4)

        MainWindow.calendarResizeSignal.connect(calendar.handle_calendar_resize)  # Connect slot
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_label_1.setText("")
        self.dashboard_btn_1.setText("")
        self.calendar_btn_1.setText("")
        self.mycourses_btn_1.setText("")
        self.certificates_btn_1.setText("")
        # self.customers_btn_1.setText("")
        self.exit_btn_1.setText("")
        self.logo_label_2.setText("")
        self.logo_label_3.setText(QCoreApplication.translate("MainWindow", u"PyQuizT", None))
        self.dashboard_btn_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.calendar_btn_2.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.mycourses_btn_2.setText(QCoreApplication.translate("MainWindow", u"My Courses", None))
        self.certificates_btn_2.setText(QCoreApplication.translate("MainWindow", u"Certificates", None))
        self.exit_btn_2.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.change_btn.setText("")
        
        # self.user_btn.setText("")
        # self.label_4.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        # self.label_5.setText(QCoreApplication.translate("MainWindow", u"Calendar Page", None))
        # self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enrolled Page", None))
        # self.label_7.setText(QCoreApplication.translate("MainWindow", u"Teaching Page", None))
    # retranslateUi

    def set_user(self, role, username):
        self.role = role
        self.username = username
        
        self.page = Dashboard(username)
        self.stackedWidget.removeWidget(self.stackedWidget.widget(0))
        self.stackedWidget.insertWidget(0, self.page)
        
        if self.role == "teacher":
            stack_course = Teacher_Stacked_Course(username)
        else:
            stack_course = Stacked_Course(username)

        self.page_2 = Calendar(self.username)
        self.stackedWidget.removeWidget(self.stackedWidget.widget(1))
        self.stackedWidget.insertWidget(1, self.page_2)
        
        self.page_3 = stack_course
        self.stackedWidget.removeWidget(self.stackedWidget.widget(2))  # Remove the current page_3
        self.stackedWidget.insertWidget(2, self.page_3)

        self.page_4 = Stacked_Certificate(username)
        
        self.stackedWidget.removeWidget(self.stackedWidget.widget(3))  # Remove the current page_4
        self.stackedWidget.insertWidget(3, self.page_4)
        self.certificates_btn_2.clicked.connect(self.page_4.go_to_certificate_list)

        self.stackedWidget.setCurrentIndex(0)
        self.dashboard_btn_1.setChecked(True) # Toggle UI index selection
