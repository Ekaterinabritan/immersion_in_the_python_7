#Напишите функцию группового переименования файлов.
# Она должна принимать параметры:
#                   желаемое конечное имя файлов .
#                   количество цифр в порядковом номере .
#                   расширение исходного файла - extension
#        (т.к. При переименовании в конце имени добавляется порядковый номер)
#                   расширение конечного файла .
#                   диапазон сохраняемого оригинального имени.

#      (т.к. Переименование должно работать только для этих файлов внутри каталога.)
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
import random
import os
from pathlib import Path

LETTERS = 'abcde'
PATHFILE = os.chdir('./file_homework7')

def original_name_random(extension: list[str] = ['.txt'],
                         count_namefile: int = 3,
                         count_file_rename: int = 0,
                         extension_new: str = '.md'):
    for item in extension:
        # создать 3 случайных файлов для каждого расширения имени
        for num in range(count_namefile):
            # пусть имя файла начинается со случайной буквы
            file_name = ''.join(random.choices(LETTERS, k=1))
            file_to_create = str(file_name) + item
            Path(file_to_create).touch()

        for i in os.listdir(PATHFILE):
            oldname = os.listdir(PATHFILE)[count_file_rename]
            newname = str(file_name) + '_rename' + str(count_file_rename + 1) + extension_new
        os.rename(oldname, newname)
        print(oldname + '>>>' + newname)
        count_file_rename = count_file_rename + 1

original_name_random()


