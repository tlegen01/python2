import time
from datetime import date
import datetime as dt
from threading import Thread
import requests
from bs4 import BeautifulSoup
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel

from work_datetime import today

url = "https://myfin.by/converter.html"

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/102.0.0.0 Safari/537.36'}

def get_course():
    global course_usd
    global course_eur
    global course_gbp
    global course_cny
    global course_pln
    global course_rub
    while True:
        response = requests.get(url=url, headers=headers)
        status = response.status_code
        if status == 200:
            content = response.content  # позволяет прочитать html фаил
            with open("temp/hw.html", "wb") as file:  # создаем фаил куда запишем html код
                file.write(content)  # записывае фаил
            soup = BeautifulSoup(response.text, "lxml")  # парсим саит через BeautifulSoup
            # print(type(soup))
            data = soup.findAll("input", class_="input_calc form-control form-input-sum bestmb") # Ищем по html
            new_data = str(data).split(sep='inputmode="decimal" type="tel" value="')
            new_data = str(new_data).split(sep='<input class="input_calc form-control form-input-sum bestmb" id="bestmb_')
            # print(new_data[6])
            dollar1 = new_data[1].split("""', '""")[0].split('"')[0]
            dollar2 = new_data[1].split("""usd" ', '""")[1].split('"/>')[0]
            dollar = tuple([dollar2, dollar1])
            # print(type(dollar))
            euro1 = new_data[2].split("""', '""")[0].split('"')[0]
            euro2 = new_data[2].split("""eur" ', '""")[1].split('"/>')[0]
            euro = tuple([euro2, euro1])
            # print(euro)
            sterling1 = new_data[3].split("""', '""")[0].split('"')[0]
            sterling2 = new_data[3].split("""gbp" ', '""")[1].split("/>,")[0].split('"')[0]
            sterling = tuple([sterling2, sterling1])
            # print(sterling2)
            uany1 = new_data[4].split("""', '""")[0].split('"')[0]
            uany2 = new_data[4].split("""cny" ', '""")[1].split('"/>')[0]
            uany = tuple([uany2, uany1])
            # print(uany)
            zloty1 = new_data[5].split("""', '""")[0].split('"')[0]
            zloty2 = new_data[5].split("""pln" ', '""")[1].split('"/>')[0]
            zloty = tuple([zloty2, zloty1])
            # print(zloty)
            rub1 = new_data[6].split("""', '""")[0].split('"')[0]
            rub2 = new_data[6].split("""rub" ', '""")[1].split('"/>')[0]
            rub = tuple([rub2, rub1])
            # print(rub)
            cours = [dollar, euro, sterling, uany, zloty, rub]
            # print(cours)
            value = 1

            for valute in cours:
                # print(valute)
                if valute[-1] == "usd":
                    course_usd = float(valute[0])
                    result = value * float(valute[0])
                    result = round(result, 3) #округляем ответ до 000
                    print(result)
                if valute[-1] == "eur":
                    course_eur = float(valute[0])
                    result = value * float(valute[0])
                    result = round(result, 3) #округляем ответ до 000
                    print(result)
                if valute[-1] == "gbp":
                    course_gbp = float(valute[0])
                    result = value * float(valute[0])
                    result = round(result, 3) #округляем ответ до 000
                    print(result)
                if valute[-1] == "cny":
                    course_cny = float(valute[0])
                    result = value * float(valute[0])
                    result = round(result, 3) #округляем ответ до 000
                    print(result)
                if valute[-1] == "pln":
                    course_pln = float(valute[0])
                    result = value * float(valute[0])
                    result = round(result, 3) #округляем ответ до 000
                    print(result)
                if valute[-1] == "rub":
                    course_rub = float(valute[0])
                    result = value * float(valute[0])
                    result = round(result, 3) #округляем ответ до 000
                    print(result)

                # for i in new_data:
                #     print(i)
                #     print(len(i))
                #     # print('\n')
                # print('\n')
        else:
            print("Oshibka dannyh")
        new_today = int(dt.datetime.now().strftime("%S"))
        print(new_today)
        if new_today % 10 != 0:
            time.sleep(10)
        print("Kurs obnovlen")
Thread(target=get_course).start()


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.label1 = QLabel()
        layout.addWidget(self.label1)

        self.label2 = QLabel()
        layout.addWidget(self.label2)

        self.label3 = QLabel()
        layout.addWidget(self.label3)

        self.label4 = QLabel()
        layout.addWidget(self.label4)

        self.line_edit.textChanged.connect(self.line_edit_text_changed)
        self.line_edit.textChanged.connect(self.line_edit_text_changed1)
        self.line_edit.textChanged.connect(self.line_edit_text_changed2)
        self.line_edit.textChanged.connect(self.line_edit_text_changed3)
        self.line_edit.textChanged.connect(self.line_edit_text_changed4)

        self.show()

    def line_edit_text_changed(self, text):
        text = course_eur * float(text)
        self.label.setText("Ваша сумма: " + str(text) + " EUR")
    def line_edit_text_changed1(self, text1):
        text1 = course_rub * float(text1)
        self.label1.setText("Ваша сумма: " + str(text1) + " RUB")
    def line_edit_text_changed2(self, text2):
        text2 = course_cny * float(text2)
        self.label2.setText("Ваша сумма: " + str(text2) + " CNY")
    def line_edit_text_changed3(self, text3):
        text3 = course_gbp * float(text3)
        self.label3.setText("Ваша сумма: " + str(text3) + " GBP")
    def line_edit_text_changed4(self, text4):
        text4 = course_pln * float(text4)
        self.label4.setText("Ваша сумма: " + str(text4) + " PLN")

app = QApplication(sys.argv)
mw = MainWindow()
app.exec()

