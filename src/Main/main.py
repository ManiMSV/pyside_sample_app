import sys
import random
from PySide6 import QtCore as qtc, QtWidgets as qtw, QtGui as qtg
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from src.Main.UI.main_window_ui import Ui_mw_main
from src.Persons import add_person_window
from src.Login import login

class main_window(qtw.QMainWindow, Ui_mw_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionAdd_Person.triggered.connect(self.open_add_person)
        self.actionQuit.triggered.connect(self.close)

    @qtc.Slot()
    def open_add_person(self):
        self.form = add_person_window.add_person()
        self.form.exec()
        

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec())