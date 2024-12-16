from PyQt6.QtWidgets import QApplication
from gui.login import Login

class Sales():
    def __init__(self):
        self.app = QApplication([])
        self.login = Login()
        self.app.exec()