import sys
import random
from PySide6 import QtCore as qtc, QtWidgets as qtw, QtGui as qtg

from UI.add_person_window_ui import Ui_d_persons

class add_person(qtw.QDialog, Ui_d_persons):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.gb_persons.setTitle("Add Person")
        self.label_message.clear()
        self.pb_close.clicked.connect(self.reject)
        self.pb_submit.clicked.connect(self.process_entry)

    @qtc.Slot()
    def process_entry(self):
        self.lineEdit_firstname.text()
        self.lineEdit_lastname.text()
        self.lineEdit_firstname.setFocus()
        self.label_message.setText("Person Added Successfully")
        self.lineEdit_firstname.clear()
        self.lineEdit_lastname.clear() 

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    form = add_person()
    form.open()
    sys.exit(app.exec())