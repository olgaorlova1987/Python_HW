from data_create import*
import os
import re
import csv


def input_data():
    name = input_name()
    surname = input_surname()
    patronymic =  input_patronymic()
    phone = input_phone()
    address = input_address()
    with open("phone_book.txt", "a",encoding="utf-8") as data:
        data.write(f"{name} {surname} {patronymic}\n{phone}\n{address}\n\n")

def input_data_to_replace():
    name = input_name()
    surname = input_surname()
    patronymic =  input_patronymic()
    phone = input_phone()
    address = input_address()
    rep = (f"{name} {surname} {patronymic}\n{phone}\n{address}\n\n")
    return rep

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

def search_line():
    print("Выберите вариант действия: \n"\
            "1.Поиск по имени\n"\
            "2.Поиск по фамилии\n"\
            "3.Поиск по отчеству\n"\
            "4.Поиск по номеру\n"\
            "5.Поиск по адресу" )
    cmd = input("Введите номер операции: ")
    while cmd not in ("1", "2", "3", "4", "5"):
        print("Ввод неверный")
        cmd = input("Введите номер операции: ")
    search = input("Введите значение поиска: ").title()
    with open("phone_book.txt", "r",encoding="utf-8") as data:
        text = data.read().strip().split("\n\n")
        for line in text:
            new_line = line.replace(" ","\n").strip().split("\n")
            if search in new_line[int(cmd)-1]:
                print(line)
                print()
            

            # if search in line:
            #     print(line)
            #     print()

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
    print(data.write)
    print()
            

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
    print(data.write)
    print()
            