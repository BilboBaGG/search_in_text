#Python

import os

#folder_file = str(input())
folder_file = 'C:\\Users\\User\\Desktop\\Program\\Python\\search.txt'

#Считывание информации из файла
def str_from_file(folder_file):
    file = open(folder_file, 'r')
    return file.read()
    file.close()

string_second = str_from_file(folder_file)
string = string_second.lower()

counter = 0
our_txt = None

os.system('cls')#'clear', если мак или линукс
print(string_second)

while True:
    our_txt = str(input('Чтo ищем : ')).lower()

    if our_txt == '':
        break

    os.system('cls')#'clear', если мак или линукс

    index = 0
    len_of_our_txt = len(our_txt)
    count = 0

    # Узнаем кол-во совпадений
    for i in range(len(string) - len_of_our_txt):
        if our_txt == string[i:i + len_of_our_txt]:
            count += 1

    list_of_indexes = []

    #Если нашлось совпадение
    if count > 0:
        #Поиск всех совпадений попорядку
        for _ in range(count):

            index = string.index(our_txt, index)
            for i in range(len_of_our_txt):
                list_of_indexes.append(index + i)
            index += 1

    #Вывод с учетом уже известных данных
    for i in range(len(string)) :
        if i in list_of_indexes:
            print(f'\033[41m{string_second[i]}\033[0m',end = '')
        else:
            print(string_second[i], end = '')

    print(f"\nВсего совпадений : {count} .\n")

    list_of_indexes.clear()

os.system('cls')
