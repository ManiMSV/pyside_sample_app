import sys
import random
from PySide6 import QtCore as qtc, QtWidgets as qtw, QtGui as qtg

from UI.login_ui import Ui_w_loginform

class login_form(qtw.QWidget, Ui_w_loginform):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_ok.clicked.connect(self.on_pushButton_ok_clicked)
        self.pushButton_cancel.clicked.connect(self.close)

    @qtc.Slot()
    def on_pushButton_ok_clicked(self):
        username = self.lineedit_userid.text()
        password = self.lineedit_password.text()

        if username == "Manikandan" and password == "Mani2503@":
            self.label_message.setText("Login Successful")
        else:
            self.label_message.setText("Login Failed")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = login_form()
    window.show()
    sys.exit(app.exec())
