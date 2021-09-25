# логический оператор if
# тернарный оператор
# строки, методы строк
# циклы for, while

# приведение типов
value = ""
value_bool = bool(value)  # Всегда True, кроме значения "" --> False
print(value_bool)

value = 0.0
value_bool = bool(value)  # Всегда True, кроме значения 0.0 --> False  0.00000....001 (400+ нулей)
print(value_bool)

value = 0
value_bool = bool(value)  # Всегда True, кроме значения 0 --> False
print(value_bool)
###########################################################################
# if условие_1:
#     блок, если ДА (условие_1)
# elif условие_2:
#     блок, если ДА (условие_2)
# ...
# else:
#     блок, если НЕТ


temp = -0.1

if temp > 0:
    print("Можно шапку не надевать ))")
    print("temp:", temp)
else:
    print("Надень шапку!")
    print("End of else")


case = input("Кинь кубик:")  # всегда str!!!
# case = int(case)
print(case, type(case))
if case == "6":
    print("Победил Вася!")
elif case == "1":
    print("Победил Петя!")
else:
    print("Все проиграли! ))")

from random import randint
case = randint(1, 6)
print("Выпало число:", case)
if case == 6:
    print("Победил Вася!")
elif case == 1:
    print("Победил Петя!")
else:
    print("Все проиграли! ))")

################################################################
# тернарный оператор
if case > 3:
    result = case ** 2
else:
    result = - case

# result = case ** 2 if case > 3 else - case

print("Выпало число:", case, "Результат:", result)

#################################################################
# СТРОКИ и методы строк
# форматирование строк
case = 1
result = "qwe"
print(f"Выпало число:{case} с результатом:{result}")

dir_name = "home"
filename = "test.py"
path = f"{dir_name}/{filename}"
print(path)
# литералы строк
my_str_1 = "I'm Qwerty"
my_str_2 = '"Apple" Inc.'
my_str_3 = '''I'm "Apple" Inc.'''
my_str_4 = """I'm "Apple" Inc."""

index = -5  # индекс -1 это последний с конца строки
symbol = my_str_1[index]
# symbol = my_str_1[100] - ОШИБКА
# print(symbol)
# my_str_1[index] = "K"  - ОШИБКА
my_str_1_len = len(my_str_1)
print(my_str_1_len, my_str_1[my_str_1_len - 1])

# срез строки
my_str_1 = "I'm Qwerty"
new_str = my_str_1[4:7]  # часть строки от левого индекса (включительно) до правого индекса (не включительно)
new_str = my_str_1[40:70]  # ОШИБКИ НЕТ
new_str = my_str_1[1:-1] # 'm Qwert
new_str = my_str_1[-50:-1] # I'm Qwert
new_str = my_str_1[:] # вся строка
new_str = my_str_1[:-3]  # от начала и до...
new_str = my_str_1[2:]  # от .. и до конца строки

index = 5
new_str = my_str_1[: index] + "K" + my_str_1[index + 1:]  # замена символа на конкретном месте в строке


new_str = my_str_1[1:-1:3]  # 3 - шаг среза
new_str = my_str_1[::2]  # символы на четных местах в строке
new_str = my_str_1[1::2]  # символы на нечетных местах в строке
new_str = my_str_1[::-1]  # разворот строки
print(new_str)

my_str_1 = "IIIIaaye'm Qwerty"

if my_str_1[-1] == "a":
    print(f"'a' on last position in {my_str_1}")
else:
    print(f"'a' not on last position in {my_str_1}")

for symbol in my_str_1:  # строка - итерируемый объект
    if (symbol.lower() not in "eyuioa") and symbol.isupper():
        print(symbol)

for symbol in my_str_1:
    print(f"symbol: '{symbol}' --> {ord(symbol)}")

for index in range(ord("a"), ord('z') + 1, 2):
    print(f"index: {index} --> '{chr(index)}'")