import datetime

list1 = [1, 2, 3, 6, 7, "123"]
print(list1)
print(type(list1))

set1 = set(list1) # несартированное множество
set2 = {1, 2, 3, 6, 7}
print(set2)
print(type(set2))

set1.add(111111) # добавить переменую в можество
print(set1)
print(type(set1))

set3 = set(list1)
print(set3)
set4 = {1, 2, 3, 6, 7}
set4.add("333333333")
set4.add("2")
print(set4)

set5 = set3.difference(set4)  #вывести разницу между двумя множествами
print(set5)

set6 = set3.intersection(set4)  #вывести пересечение между двумя множествами
print(set6)

set7 = set3.union(set4)  #вывести все переменные с двух множеств
print(set7)

set8 = set(list1)
print(set8)
set8.remove(2) # удаление переменной из множества
print(set8)

val1 = [x for x in set8 if isinstance(x, str)] # оставить только str
print(val1)

set8.add(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) # текущее время в строке
val2 = []
for x in set8:
    if isinstance(x, str): # спрашивает x есть str 
        val2.append(x)
print(set8)