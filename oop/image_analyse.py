import sys
import cv2
import requests
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QGridLayout, QCheckBox, \
    QPushButton, QSlider, QComboBox





class MainWindow(QWidget):
    def __init__(self, width, height, title):
        QWidget.__init__(self)  #
        self.setWindowTitle(title)  # название титла
        self.resize(width, height)  # размер окна

        self.image_data = None

        self.layout = QGridLayout()  # экземпляр класса интерфейса grid (сетка)
        self.setLayout(self.layout)  # глобальная ячейка, вкладываем QGrid в MainWindow(QWidget)

        self.lable_path = QLabel("путь к файлу: ")  # ячейка для отображения текста
        self.layout.addWidget(self.lable_path, 1, 1)  # вкладываем QLabel в QGridLayout

        self.line_edit_path = QLineEdit("Ali.jpeg")  # экземпляр строки ввода текста
        self.layout.addWidget(self.line_edit_path, 2, 1)  # ячейка для ввода текста, вкладываем QLineEdit в QGridLayout

        self.lable_chec = QLabel("Статус: ")  # ячейка для отображения текста
        self.layout.addWidget(self.lable_chec, 1, 2)  # вкладываем QLabel в QGridLayout

        self.check_box_status = QCheckBox()  # галочка
        self.check_box_status.setChecked(False)
        self.layout.addWidget(self.check_box_status, 2, 2)  # ячейка галочка, вкладываем QCheckBox в QGridLayout

        self.push_button_check = QPushButton('Проверить наличие фаила')  # кнопка
        self.push_button_check.clicked.connect(
            self.read_and_check_image_in_path)  # запускаем нажатие кнопки функцию changelabeltext
        # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 200, 28))
        self.layout.addWidget(self.push_button_check, 2,
                              3)  # ячейка для ввода текста, вкладываем QPushButton в QGridLayout
        ######################################################################
        self.lable_widht = QLabel("ширина: ")  # ячейка для отображения текста
        self.layout.addWidget(self.lable_widht, 3, 1)  # вкладываем QLabel в QGridLayout

        self.lable_height = QLabel("Высота: ")  # ячейка для отображения текста
        self.layout.addWidget(self.lable_height, 3, 2)  # вкладываем QLabel в QGridLayout

        self.line_edit_widht = QLineEdit("0")  # экземпляр строки ввода текста
        self.layout.addWidget(self.line_edit_widht, 4, 1)  # ячейка для ввода текста, вкладываем QLineEdit в QGridLayout

        self.line_edit_height = QLineEdit("0")  # экземпляр строки ввода текста
        self.layout.addWidget(self.line_edit_height, 4,
                              2)  # ячейка для ввода текста, вкладываем QLineEdit в QGridLayout

        self.check_box_wb = QCheckBox()  # галочка ч/б
        self.check_box_wb.setChecked(False)
        self.layout.addWidget(self.check_box_wb, 5, 1)  # ячейка галочка, вкладываем QCheckBox в QGridLayout

        self.lable_chec_wb = QLabel("Превратить в ч/б: ")  # ячейка для отображения текста
        self.layout.addWidget(self.lable_chec_wb, 5, 2)  # вкладываем QLabel в QGridLayout

        self.check_box_protect = QCheckBox()  # галочка ч/б
        self.check_box_protect.setChecked(False)  # ufkjxrf yt frnbdyf
        self.check_box_protect.stateChanged.connect(self.protect)
        self.layout.addWidget(self.check_box_protect, 5, 3)  # ячейка галочка, вкладываем QCheckBox в QGridLayout

        self.lable_check_box_protect = QLabel("Подтвердить изменения: ")  # ячейка для отображения текста
        self.layout.addWidget(self.lable_check_box_protect, 5, 4)  # вкладываем QLabel в QGridLayout

        self.push_button_start = QPushButton('выполнить')  # кнопка
        self.push_button_start.clicked.connect(self.start)  # запускаем нажатие кнопки функцию changelabeltext
        self.push_button_start.setEnabled(False)  # кнопка не активна
        # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 200, 28))
        self.layout.addWidget(self.push_button_start, 6,
                              1)  # ячейка для ввода текста, вкладываем QPushButton в QGridLayout

        self.push_button_stop = QPushButton('отменить')  # кнопка
        self.push_button_stop.clicked.connect(self.stop)  # запускаем нажатие кнопки функцию changelabeltext
        # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 200, 28))
        self.layout.addWidget(self.push_button_stop, 6,
                              3)  # ячейка для ввода текста, вкладываем QPushButton в QGridLayout

        self.slider_quality = QSlider()  # ползунок
        self.slider_quality.setMinimum(1)  # значения слайдера минимум
        self.slider_quality.setMaximum(100)  # значения слайдера максимум
        self.slider_quality.setValue(95)  # значения слайдера
        self.layout.addWidget(self.slider_quality, 4, 5)

        self.lable_slider_quality = QLabel("Выбрать качество: ")  # ячейка для отображения текста
        self.layout.addWidget(self.lable_slider_quality, 5, 5)  # вкладываем QLabel в QGridLayout
        ######################################################################
        self.combo_box_filter = QComboBox() # Для примера список
        self.combo_box_filter.addItem("гаус")
        self.combo_box_filter.addItem("фильтр 2")
        self.combo_box_filter.addItem("фильтр 3")
        self.combo_box_filter.addItems(["фильтр 4", "фильтр 5", "фильтр 6"])
        self.layout.addWidget(self.combo_box_filter, 7, 4)
        #######################################################################
        self.show()  # метод для отрисовки интерфейса

    def read_and_check_image_in_path(self):
        value = self.line_edit_path.text()  # путь к файлу
        print(value)
        ################################################## #обработка изображения
        try:
            # img = cv2.imread(value, cv2.IMREAD_GRAYSCALE) # читаем фаил  в сером 0 - серый, 1, cv2.IMREAD_COLOR -
            # цветной
            img = cv2.imread(value, cv2.IMREAD_COLOR)  # читаем фаил  в сером 0 - серый, 1, cv2.IMREAD_COLOR - цветной
            # cv2.imshow("Ali_window", img) # открываем окно с именем  volf_window
            cv2.imshow("Ali_window1", img)  # открываем окно с именем  volf_window
            cv2.waitKey(1)  # задержка изображения
        except Exception as error:
            print(error)
            img = []
        cv2.imwrite("Ali2.jpg", img)
        ###################################################
        if len(img) > 0:
            has_file = True
            print("Изображение успешно прочитано")
            self.image_data = img
            height, width = self.image_data.shape[:2]  # читаем изображения с self.image_data (возврощает tuple)
            self.line_edit_widht.setText(str(width))  # устанавливае значение для line_edit_widht
            self.line_edit_height.setText(str(height))  # устанавливае значение для line_edit_height
        else:
            has_file = False
            print("Изображение не прочитано")
            self.line_edit_widht.setText("0")
            self.line_edit_height.setText("0")
        self.check_box_status.setChecked(has_file)  # меняем статус check_box_status на True
        # if has_file:
        #     self.check_box_status.setChecked(True)  # меняем статус check_box_status на True
        # else:
        #     self.check_box_status.setChecked(False) # меняем статус check_box_status на False
        ########################################################
        # self.push_button_check.hide() # после нажатия кнопка исчезает

    def start(self):
        print("start")

        combo = self.combo_box_filter.currentText()
        print(combo)

        white_black = bool(self.check_box_wb.isChecked())
        quality = int(self.slider_quality.value())  # Выводит значения слайдера
        widht = int(self.line_edit_widht.text())
        height = int(self.line_edit_height.text())
        image = self.image_data

        if white_black:
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # cv2.equalizeHist(image)

            image = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)[1]

        # image = cv2.imread(self.line_edit_path.text(), 0)
        # cv2.imshow('grey scale image', image)
        image = cv2.resize(image, (widht, height))
        cv2.imwrite("Ali_new.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, quality])

        pass

    def stop(self):
        print("stop")
        pass

    def protect(self):
        self.push_button_start.setEnabled(self.check_box_protect.isChecked())


app = QApplication(sys.argv)
mw = MainWindow(640, 480, "Image Analyse") # создаем инстанс (экземпляр) класса
app.exec()
