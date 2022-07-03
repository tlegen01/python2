import sys
from threading import Thread

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QGridLayout, QCheckBox, QPushButton
import time


class MainWindow(QWidget):
    def __init__(self, width, height, title):
        QWidget.__init__(self)
        self.setWindowTitle(title)
        self.resize(width, height)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
###########################################
        self.pause = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        ##################################
        self.lable_path_hours = QLabel("00")
        self.layout.addWidget(self.lable_path_hours, 0, 0)
        self.lable_path1 = QLabel(":")
        self.layout.addWidget(self.lable_path1, 0, 1)
        self.lable_path_minutes = QLabel("00")
        self.layout.addWidget(self.lable_path_minutes, 0, 2)
        self.lable_path2 = QLabel(":")
        self.layout.addWidget(self.lable_path2, 0, 3)
        self.lable_path_seconds = QLabel("00")
        self.layout.addWidget(self.lable_path_seconds, 0, 4)
        ####################################
        self.push_button_check = QPushButton('Start')
        self.push_button_check.clicked.connect(self.start_new_thread)
        self.layout.addWidget(self.push_button_check, 1, 1)
        self.push_button_check = QPushButton('Stop')
        self.push_button_check.clicked.connect(self.stop_timer)
        self.layout.addWidget(self.push_button_check, 1, 2)
        self.push_button_check = QPushButton('Reset')
        self.push_button_check.clicked.connect(self.reset_timer)
        self.layout.addWidget(self.push_button_check, 1, 3)
        #########################################
        self.show()

    def stop_timer(self):
        self.pause = False

    def reset_timer(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.lable_path_hours.setText(str(self.hours))
        self.lable_path_minutes.setText(str(self.minutes))
        self.lable_path_seconds.setText(str(self.seconds))

    def start_timer(self):
        self.pause = True
        self.hours = self.hours
        self.minutes = self.minutes
        self.seconds = self.seconds

        while self.pause:
            self.seconds += 1
            if self.seconds > 59:
                self.minutes += 1
                self.seconds = 0
                if self.minutes > 59:
                    self.hours += 1
                    self.minutes = 0
                    if self.hours > 23:
                        self.seconds = 0
                        self.minutes = 0
                        self.hours = 0
            time.sleep(0.01)
            # self.pause = pause
            self.lable_path_hours.setText(str(self.hours))
            self.lable_path_minutes.setText(str(self.minutes))
            self.lable_path_seconds.setText(str(self.seconds))
            print(f"{self.hours}:{self.minutes}:{self.seconds}")

    def start_new_thread(self):
        Thread(target=self.start_timer).start()


app = QApplication(sys.argv)
mw = MainWindow(640, 480, "Sekundomer")
app.exec()
