# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше
# заданного минимума и не больше заданного максимума)



list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list_2 = [ ]
max_num = 10
min_num = 5
for i in range(len(list_1)):
    if min_num <= list_1[i] <= max_num:
        list_2.append(i)
print(list_2)

list_3 = [i for i in range(len(list_1)) if min_num<= list_1[i] <=max_num]
list_4 = [i if min_num <= list_1[i] <= max_num else '*' for i in range (len(list_1))]