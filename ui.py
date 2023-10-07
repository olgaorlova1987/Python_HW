from Task_38.logger import*

def interface():
    cmd = ""
    while cmd != "4":
        print("Выберите вариант действия: \n"\
            "1.Записать данные\n"\
            "2.Вывести данные\n"\
            "3.Поиск данных\n"\
            "4.Выход"  )
        cmd = input("Введите номер операции: ")
        while cmd not in ("1", "2", "3", "4"):
            print("Ввод неверный")
            cmd = input("Введите номер операции: ")
        if cmd == "1":
            input_data()
        elif cmd == "2":
            print_data()
        elif cmd == "3":
            search_line()
    print("Всего доброго")