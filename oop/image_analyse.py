import sys
import requests
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QGridLayout, QCheckBox, QPushButton
from PySide6 import QtCore
import cv2

class MainWindow(QWidget):
    def __init__(self, width, height, title):
        QWidget.__init__(self) #
        self.setWindowTitle(title)  # название титла
        self.resize(width, height) #размер окна

        self.image_data = None

        self.layout = QGridLayout() # экземпляр класса интерфейса grid (сетка)
        self.setLayout(self.layout)  # глобальная ячейка, вкладываем QGrid в MainWindow(QWidget)

        self.lable_path = QLabel("путь к файлу: ") # ячейка для отображения текста
        self.layout.addWidget(self.lable_path, 1, 1) # вкладываем QLabel в QGridLayout

        self.line_edit_path = QLineEdit("Ali.jpeg") # экземпляр строки ввода текста
        self.layout.addWidget(self.line_edit_path, 2, 1) # ячейка для ввода текста, вкладываем QLineEdit в QGridLayout

        self.lable_chec = QLabel("Статус: ") # ячейка для отображения текста
        self.layout.addWidget(self.lable_chec, 1, 2) # вкладываем QLabel в QGridLayout

        self.check_box_status = QCheckBox()  # галочка
        self.check_box_status.setChecked(False)
        self.layout.addWidget(self.check_box_status, 2, 2)  # ячейка галочка, вкладываем QCheckBox в QGridLayout

        self.push_button_check = QPushButton('Проверить наличие фаила') # кнопка
        self.push_button_check.clicked.connect(self.read_and_check_image_in_path) # запускаем нажатие кнопки функцию changelabeltext
        # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 200, 28))
        self.layout.addWidget(self.push_button_check, 2, 3) # ячейка для ввода текста, вкладываем QPushButton в QGridLayout

        self.show() # метод для отрисовки интерфейса

    def read_and_check_image_in_path(self):
        value = self.line_edit_path.text() # путь к файлу
        print(value)
        ################################################## #обработка изображения
        try:
            # img = cv2.imread(value, cv2.IMREAD_GRAYSCALE) # читаем фаил  в сером 0 - серый, 1, cv2.IMREAD_COLOR - цветной
            img = cv2.imread(value, cv2.IMREAD_COLOR) # читаем фаил  в сером 0 - серый, 1, cv2.IMREAD_COLOR - цветной
            # cv2.imshow("Ali_window", img) # открываем окно с именем  volf_window
            cv2.imshow("Ali_window1", img) # открываем окно с именем  volf_window
        except Exception as error:
            print(error)
            img = []
        cv2.waitKey(1) # задержка изображения
        cv2.imwrite("Ali2.jpg", img)
        ###################################################
        if len(img) > 0:
            has_file = True
            print("Изображение успешно прочитано")
            self.image_data = img
        else:
            has_file = False
            print("Изображение не прочитано")
        self.check_box_status.setChecked(has_file)  # меняем статус check_box_status на True
        # if has_file:
        #     self.check_box_status.setChecked(True)  # меняем статус check_box_status на True
        # else:
        #     self.check_box_status.setChecked(False) # меняем статус check_box_status на False
        ########################################################
        # self.push_button_check.hide() # после нажатия кнопка исчезает


app = QApplication(sys.argv)
mw = MainWindow(640, 480, "Image Analyse")
app.exec()

