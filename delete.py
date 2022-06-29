import os
import shutil


first = os.path.abspath(os.path.dirname(__file__)) #содержит обсолютный путь к текущему скрипту
# first = os.path.abspath(os.path.dirname(__file__)) #содержит относительный путь к текущему скрипту
print(first)
second = "temp/junk1.txt"
print(second)
path = os.path.join(first, second)
print(path)
try:
     os.remove(path)  #удаляет фаил
     # pass
except Exception as error:
    print(error)
finally:
    os.rmdir("temp")  # удаления папки
    print("finally")
    pass
print("something")

#
# path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'TestDir')
shutil.rmtree(path) #удаляет если даже папка полная