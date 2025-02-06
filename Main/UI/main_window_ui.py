# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_mw_main(object):
    def setupUi(self, mw_main):
        if not mw_main.objectName():
            mw_main.setObjectName(u"mw_main")
        mw_main.resize(800, 600)
        font = QFont()
        font.setPointSize(12)
        mw_main.setFont(font)
        self.actionQuit = QAction(mw_main)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAdd_Person = QAction(mw_main)
        self.actionAdd_Person.setObjectName(u"actionAdd_Person")
        self.centralwidget = QWidget(mw_main)
        self.centralwidget.setObjectName(u"centralwidget")
        mw_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mw_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 28))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuPerson = QMenu(self.menubar)
        self.menuPerson.setObjectName(u"menuPerson")
        mw_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mw_main)
        self.statusbar.setObjectName(u"statusbar")
        mw_main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPerson.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuPerson.addAction(self.actionAdd_Person)

        self.retranslateUi(mw_main)

        QMetaObject.connectSlotsByName(mw_main)
    # setupUi

    def retranslateUi(self, mw_main):
        mw_main.setWindowTitle(QCoreApplication.translate("mw_main", u"Sample_App", None))
        self.actionQuit.setText(QCoreApplication.translate("mw_main", u"Quit", None))
        self.actionAdd_Person.setText(QCoreApplication.translate("mw_main", u"Add Person", None))
        self.menuFile.setTitle(QCoreApplication.translate("mw_main", u"File", None))
        self.menuPerson.setTitle(QCoreApplication.translate("mw_main", u"Person", None))
    # retranslateUi

