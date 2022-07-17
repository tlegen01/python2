list1 = [1, 2, 5, [3, 2, 6], 5, {"key_1": 1}, {1, 2, 3, 5, 7, "123"}]
str1 = "Banan"

search1 = list1.index(5) # поиск индекса в массиве по элементу
print(search1, list1[search1])
search2 = str1.index("a")
print(search2, str1[search2])

serach3 = list1.index(5, 3, 7) # поиск индекса в массиве по элементу от куда до куда
print(serach3, " : ", list1[serach3])

list2 = [1, 2, 5, 10, 4, 2]
list2.sort()
print(list2)
str2 = "ABCDffff124124wecerwfgyhtyjsafs"



letter1 = "1"
sumvol1 = ord(letter1) # присваиваем числовой номер буква "а"
print(sumvol1)

number1 = chr(200) # присваиваем символ числа 200
print(number1)

###########################################################

list5 = [1, 2, 5, 10, 4, 2]
print(list5)
list5.sort(reverse=True) # сортировка в обратном порядке
print(list5)

str3 = "ABCDffff124124wecerwfgyhtyjsafs"
print(str3)
# arr1 = []
# for x in str3:
#     arr1.append(x)
arr1 = [x for x in str3]
print(arr1)
arr1.sort(reverse=True)
print(arr1)

str4 = ""
for x in arr1:
    str4 += x
print(str4)
#################################################
myTuple = ("john", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
print(type(x))
##################################################
str5 = "".join(arr1) #собрать из масива в строку через join
print(str5)
##################################################

text1 = "Идейные соображения высшего порядкаб ф также сложившаяся структура организации представляет собой интересный" \
        "экспериментструктура проверки форм развития"

substring = "структура"
find1 = text1.find(substring, 60)
print(find1)
# print(text1[find1:find1+len(substring):1])

text2 = text1.lower() # превращает в нижний регистр
print(text2)



