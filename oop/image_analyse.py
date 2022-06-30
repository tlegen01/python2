import sys
import requests
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QGridLayout


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Image Analyse")  # название титла

        # layout = QVBoxLayout()
        # self.setLayout(layout)
        #
        # self.line_edit = QLineEdit()
        # layout.addWidget(self.line_edit)
        # self.line_edit1 = QLineEdit()
        # layout.addWidget(self.line_edit1)

        layout2 = QGridLayout()
        self.show()


app = QApplication(sys.argv)
mw = MainWindow
app.exec()
