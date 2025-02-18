# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_start.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(699, 750)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 40, 291, 61))
        self.label.setStyleSheet(u"font: 26pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 350, 121, 71))
        self.btn_x = QPushButton(self.centralwidget)
        self.btn_x.setObjectName(u"btn_x")
        self.btn_x.setGeometry(QRect(240, 430, 121, 71))
        self.sel_screen = QFrame(self.centralwidget)
        self.sel_screen.setObjectName(u"sel_screen")
        self.sel_screen.setGeometry(QRect(70, 170, 541, 521))
        self.sel_screen.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.471591 rgba(255, 255, 255, 212));")
        self.sel_screen.setFrameShape(QFrame.StyledPanel)
        self.sel_screen.setFrameShadow(QFrame.Raised)
        self.btn_tutorial = QPushButton(self.sel_screen)
        self.btn_tutorial.setObjectName(u"btn_tutorial")
        self.btn_tutorial.setGeometry(QRect(220, 90, 75, 24))
        self.btn_lvl1 = QPushButton(self.sel_screen)
        self.btn_lvl1.setObjectName(u"btn_lvl1")
        self.btn_lvl1.setGeometry(QRect(220, 160, 75, 24))
        self.btn_lvl2 = QPushButton(self.sel_screen)
        self.btn_lvl2.setObjectName(u"btn_lvl2")
        self.btn_lvl2.setGeometry(QRect(220, 230, 75, 24))
        self.btn_lvl3 = QPushButton(self.sel_screen)
        self.btn_lvl3.setObjectName(u"btn_lvl3")
        self.btn_lvl3.setGeometry(QRect(220, 290, 75, 24))
        self.btn_inf = QPushButton(self.sel_screen)
        self.btn_inf.setObjectName(u"btn_inf")
        self.btn_inf.setGeometry(QRect(220, 340, 75, 24))
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(-190, -10, 1601, 800))
        self.label_16.setText(u"")
        self.label_16.setPixmap(QPixmap(u"../../images/sky.png"))
        self.enter = QFrame(self.centralwidget)
        self.enter.setObjectName(u"enter")
        self.enter.setGeometry(QRect(0, 0, 701, 801))
        self.enter.setStyleSheet(u"background-color: rgb(255,255,255)\n"
"")
        self.enter.setFrameShape(QFrame.StyledPanel)
        self.enter.setFrameShadow(QFrame.Raised)
        self.txt_name = QLineEdit(self.enter)
        self.txt_name.setObjectName(u"txt_name")
        self.txt_name.setGeometry(QRect(330, 280, 191, 41))
        self.txt_name.setStyleSheet(u"")
        self.label_2 = QLabel(self.enter)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 170, 421, 71))
        self.label_3 = QLabel(self.enter)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 180, 121, 261))
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_3.setPixmap(QPixmap(u"../../images/friend.png"))
        self.enter_2 = QPushButton(self.enter)
        self.enter_2.setObjectName(u"enter_2")
        self.enter_2.setGeometry(QRect(380, 330, 75, 24))
        self.lbl_name = QLabel(self.centralwidget)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setGeometry(QRect(211, 110, 241, 31))
        font = QFont()
        font.setPointSize(14)
        self.lbl_name.setFont(font)
        self.lbl_name.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_16.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.btn_x.raise_()
        self.sel_screen.raise_()
        self.enter.raise_()
        self.lbl_name.raise_()

        self.retranslateUi(MainWindow)
        self.btn_x.clicked.connect(MainWindow.btn_x_a)
        self.pushButton.clicked.connect(MainWindow.level_select)
        self.btn_tutorial.clicked.connect(MainWindow.level_select)
        self.btn_lvl1.clicked.connect(MainWindow.level_select)
        self.btn_lvl2.clicked.connect(MainWindow.level_select)
        self.btn_lvl3.clicked.connect(MainWindow.level_select)
        self.btn_inf.clicked.connect(MainWindow.level_select)
        self.enter_2.clicked.connect(MainWindow.enter_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Jump!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Jump!", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_x.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btn_tutorial.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.btn_lvl1.setText(QCoreApplication.translate("MainWindow", u"Level 1", None))
        self.btn_lvl2.setText(QCoreApplication.translate("MainWindow", u"Level 2", None))
        self.btn_lvl3.setText(QCoreApplication.translate("MainWindow", u"Level 3", None))
        self.btn_inf.setText(QCoreApplication.translate("MainWindow", u"Editor (WIP)", None))
        self.txt_name.setText(QCoreApplication.translate("MainWindow", u"Friend", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"What's his name?", None))
        self.label_3.setText("")
        self.enter_2.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.lbl_name.setText("")
    # retranslateUi

