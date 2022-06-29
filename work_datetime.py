import datetime as dt
from datetime import date
from datetime import time
from datetime import datetime

today = dt.datetime.now()
# print("Date :", today)
# print(str(today).split(" ")[1][0:8:1]) #получение времени из .now() последуюцая обрезка
today_date = date.today()
print(today_date)
# today_second = datetime.time()
# print(today_second)
new_today = today.strftime("%d-%m-%Y %H:%M:%S")
print(new_today)

# Timestamp = 0
# date_From_Timestamp = datetime.fromtimestamp(Timestamp)  #превращение числа в тип данных даты
# print(date_From_Timestamp)
