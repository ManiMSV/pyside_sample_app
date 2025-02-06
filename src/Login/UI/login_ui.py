# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

from .icons import icons_rc

class Ui_w_loginform(object):
    def setupUi(self, w_loginform):
        if not w_loginform.objectName():
            w_loginform.setObjectName(u"w_loginform")
        w_loginform.resize(423, 422)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        w_loginform.setFont(font)
        self.gridLayout = QGridLayout(w_loginform)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 2)

        self.groupBox = QGroupBox(w_loginform)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setKerning(True)
        self.groupBox.setFont(font1)
        self.groupBox.setCursor(QCursor(Qt.ArrowCursor))
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_userid = QLabel(self.groupBox)
        self.label_userid.setObjectName(u"label_userid")
        self.label_userid.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_userid)

        self.lineedit_userid = QLineEdit(self.groupBox)
        self.lineedit_userid.setObjectName(u"lineedit_userid")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineedit_userid)

        self.label_password = QLabel(self.groupBox)
        self.label_password.setObjectName(u"label_password")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_password)

        self.lineedit_password = QLineEdit(self.groupBox)
        self.lineedit_password.setObjectName(u"lineedit_password")
        self.lineedit_password.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineedit_password)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.label_message = QLabel(w_loginform)
        self.label_message.setObjectName(u"label_message")

        self.gridLayout.addWidget(self.label_message, 5, 0, 1, 2)

        self.pushButton_cancel = QPushButton(w_loginform)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        icon = QIcon()
        icon.addFile(u":/Buttons/\u274c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_cancel.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_cancel, 3, 0, 1, 1)

        self.pushButton_ok = QPushButton(w_loginform)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/\u2714.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_ok.setIcon(icon1)

        self.gridLayout.addWidget(self.pushButton_ok, 3, 1, 1, 1)


        self.retranslateUi(w_loginform)

        QMetaObject.connectSlotsByName(w_loginform)
    # setupUi

    def retranslateUi(self, w_loginform):
        w_loginform.setWindowTitle(QCoreApplication.translate("w_loginform", u"SAMPLE APP", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_loginform", u"Welcome to Login", None))
        self.label_userid.setText(QCoreApplication.translate("w_loginform", u"USER ID", None))
        self.label_password.setText(QCoreApplication.translate("w_loginform", u"PASSWORD", None))
        self.label_message.setText("")
        self.pushButton_cancel.setText(QCoreApplication.translate("w_loginform", u"CANCEL", None))
        self.pushButton_ok.setText(QCoreApplication.translate("w_loginform", u"OK", None))
    # retranslateUi

