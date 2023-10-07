# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. + Программа должна выводить данные
# 2. + Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

import os
import time




def input_name():
    name = input("Введите имя: ")
    return name

def input_surname():
    surname = input("Введите фамилию: ")
    return surname

def input_patronymic():
    patronymic = input("Введите отчество: ")
    return patronymic

def input_phone():
    phone = input("Введите номер телефона: ")
    return phone

def input_address():
    address = input("Введите адрес: ")
    return address

def input_data():
    name = input_name()
    surname = input_surname()
    patronymic =  input_patronymic()
    phone = input_phone()
    address = input_address()
    with open("phone_book.txt", "a",encoding="utf-8") as data:
        data.write(f"{name} {surname} {patronymic}\n{phone}\n{address}\n\n")

def print_data():
    os.system("cls")
    with open("phone_book.txt", "r",encoding="utf-8") as data:
        print(data.read())

def search_line():
    search = input("Введите значение поиска: ")
    with open("phone_book.txt", "r",encoding="utf-8") as data:
        text = data.read().split("\n\n")[:-1]
        
        # data.seek(0)
        # list_data = data.readlines()
        for line in text:
            # print(line)
            # print()
            # time.sleep(1)
            if search in line:
                print(line)
                print()

def delite_line():
    delite = str(input("Введите атрибут удаляемого значения (имя, фамилия и пр): "))
    with open("phone_book.txt", "r",encoding="utf-8") as data:
        text = data.read()
        text_lines = text.strip().split("\n\n")
        for i , line in enumerate (text_lines):
            if delite in line:
                del_phone_book_lines = line
                text_lines.pop(i)
                print(f'Удалена запись: {del_phone_book_lines}\n')
                break
    with open("phone_book.txt", 'w' , newline= '', encording='utf-8') as data:
        data.write('\n\n'.join(text_lines))

def replace_line():
    rep_lace = str(input("Введите любой атрибут изменяемого значения (имя, фамилия и др): "))
    with open("phone_book.txt", "r",encoding="utf-8") as data:
        text = data.read()
    text_lines = text.strip().split("\n\n")
    for i , line in enumerate (text_lines):
        if rep_lace in line:
            rep_phone_book_lines = text_lines[i]
            print(f'Вы хотите изменить: {rep_phone_book_lines}\n')
            text_lines[i]= input_data_to_replace()
    with open("phone_book.txt", 'w' , newline= '', encording='utf-8') as data:
        data.write('\n\n'.join(text_lines))

def interface():
    cmd = ""
    while cmd != "6":
        print("Выберите вариант действия: \n"\
            "1.Записать данные\n"\
            "2.Вывести данные\n"\
            "3.Поиск данных\n"\
            "4.Удалить данные\n"\
            "5.Изменить данные\n"\
            "6.Выход" )
        cmd = input("Введите номер операции: ")
        while cmd not in ("1", "2", "3", "4", "5", "6"):
            print("Ввод неверный")
            cmd = input("Введите номер операции: ")
        if cmd == "1":
            input_data()
        elif cmd == "2":
            print_data()
        elif cmd == "3":
            search_line()
        elif cmd == "4":
            delite_line()
        elif cmd == "5":
            replace_line() 

interface()

    






    