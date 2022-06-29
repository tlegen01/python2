import time
from threading import Thread
import sys
import requests
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLineEdit, QLabel
from bs4 import BeautifulSoup

course_dollar = 0.0
# url = "https://www.google.kz/search?q=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D1%83&source=" \
#       "hp&ei=s5yoYsPlCNKJxc8P7umL-AM&iflsig=AJiK0e8AAAAAYqiqw6EejbrNRRjtPcu562hwQ_7G8qGN&ved=0ahUKEwiDi7KIla34AhXSRPEDHe" \
#       "70Aj8Q4dUDCAY&uact=5&oq=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D1%83&gs_lcp=Cgdnd3" \
#       "Mtd2l6EAMyDAgAELEDEAoQRhCCAjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjoLCAAQgAQQs" \
#       "QMQgwE6CAgAEIAEELEDOg4ILhCABBCxAxDHARCjAjoOCC4QgAQQsQMQxwEQ0QM6BQguEIAEOgsILhCABBDHARDRAzoFCAAQgAQ6CwgAEIAEELED" \
#       "EMkDOg0IABCABBCxAxBGEIICOgkIABANEEYQggI6BAgAEA1QAFjFMWDoNmgBcAB4AIABnAGIAcwOkgEEMC4xNZgBAKABAQ&sclient=gws-wiz"
url = "https://finance.rambler.ru/calculators/converter/1-KZT-USD/"
params = {}
response = requests.get(url=url, params=params)


def get_course():
    global course_dollar
    while True:
        if response.status_code == 200:
            value = 400000.60
            soup = BeautifulSoup(response.text, "lxml")
            # print(response)
            # print(response.status_code)
            # print(soup)
            # print(type(soup))
            # data = soup.find_all("input", class_="text") #ищем по классу span и классу текст
            data = soup.find_all("div", class_="converter-display__cross-block")[0]  # ищем по классу span и классу текст
            new_data = str(data).split(sep='__value">')[1:]
            # print(new_data)
            # print(len(new_data))
            tenge = tuple(
                [
                    new_data[0].split('</div>\n<div class="converter-display__currency">')[0],
                    new_data[0].split('</div>\n<div class="converter-display__currency">')[1].split("</div>")[0]
                ]
            )
            dollar = tuple(
                [
                    new_data[1].split("</div>")[0],
                    new_data[1].split("</div>")[-3].split('>')[-1]
                ]
            )
            # print(dollar)

            course = [tenge, dollar]
            print(course)
            index = 0
            for valute in course:
                index += 1
                print(f'Obekt №{index}: {valute}')

                if valute[-1] == "USD":
                    course_dollar = float(valute[0])
                    result = round(value * float(valute[0]), 3)
                    # result = round(result, 3) # округления
                    print(str(result) + " S")
                    # print(valute[-1])
            # for i in data:
            #     print(i)
            #     print("\n")

            # content = response.content #возврощают в байтах
            # with open(file="temp/new.html", mode="wb") as file:
            #     file.write(content)
            # print(type(content))
            # data = content.decode(encoding="ISO-8859-1")  #возврощает строку
            # print(type(data))
            # print(data)
            # new_data = data.split("""value=""")
            # print(len(new_data))
            # for i in new_data:
            #     print(i + "\n")
        else:
            print("Oshibka polucheniya")
        # print(response)
        # print(response.status_code)
        # print(response.content)
        time.sleep(5.0)
        print("Kurs obnovlen")


Thread(target=get_course).start()



from PySide6.QtCore import *
from PySide6.QtGui import *


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.line_edit.textChanged.connect(self.line_edit_text_changed)

        self.show()

    def line_edit_text_changed(self, text):
        try:
            text = round(course_dollar * float(text), 3)
            self.label.setText("Ваша сумма: " + str(text) + " $")
        except Exception as error:
            self.label.setText('ошибка ввода данных')


app = QApplication(sys.argv)
mw = MainWindow()
app.exec()
