# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_person_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_d_persons(object):
    def setupUi(self, d_persons):
        if not d_persons.objectName():
            d_persons.setObjectName(u"d_persons")
        d_persons.resize(609, 389)
        font = QFont()
        font.setPointSize(12)
        d_persons.setFont(font)
        self.gridLayout = QGridLayout(d_persons)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_submit = QPushButton(d_persons)
        self.pb_submit.setObjectName(u"pb_submit")

        self.gridLayout.addWidget(self.pb_submit, 1, 1, 1, 1)

        self.pb_close = QPushButton(d_persons)
        self.pb_close.setObjectName(u"pb_close")

        self.gridLayout.addWidget(self.pb_close, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.gb_persons = QGroupBox(d_persons)
        self.gb_persons.setObjectName(u"gb_persons")
        self.gb_persons.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout = QFormLayout(self.gb_persons)
        self.formLayout.setObjectName(u"formLayout")
        self.label_firstname = QLabel(self.gb_persons)
        self.label_firstname.setObjectName(u"label_firstname")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_firstname)

        self.lineEdit_firstname = QLineEdit(self.gb_persons)
        self.lineEdit_firstname.setObjectName(u"lineEdit_firstname")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_firstname)

        self.label_lastname = QLabel(self.gb_persons)
        self.label_lastname.setObjectName(u"label_lastname")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_lastname)

        self.lineEdit_lastname = QLineEdit(self.gb_persons)
        self.lineEdit_lastname.setObjectName(u"lineEdit_lastname")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_lastname)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.SpanningRole, self.verticalSpacer)


        self.gridLayout.addWidget(self.gb_persons, 0, 0, 1, 3)

        self.label_message = QLabel(d_persons)
        self.label_message.setObjectName(u"label_message")
        self.label_message.setEnabled(False)
        self.label_message.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_message, 2, 0, 1, 3)


        self.retranslateUi(d_persons)

        QMetaObject.connectSlotsByName(d_persons)
    # setupUi

    def retranslateUi(self, d_persons):
        d_persons.setWindowTitle(QCoreApplication.translate("d_persons", u"Dialog", None))
        self.pb_submit.setText(QCoreApplication.translate("d_persons", u"Submit", None))
        self.pb_close.setText(QCoreApplication.translate("d_persons", u"Close", None))
        self.gb_persons.setTitle(QCoreApplication.translate("d_persons", u"GroupBox", None))
        self.label_firstname.setText(QCoreApplication.translate("d_persons", u"First Name", None))
        self.label_lastname.setText(QCoreApplication.translate("d_persons", u"Last Name", None))
        self.label_message.setText(QCoreApplication.translate("d_persons", u"Message", None))
    # retranslateUi

