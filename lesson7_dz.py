# 1
# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
# Это одно задание. При выполнении пунктов можно использовать объекты полученные в предыдущих пунктах.

# persons = [{"name": "John", "age": 15},
#            {"name": "Anna", "age": 23},
#            {"name": "Dan", "age": 5},
#            {"name": "Maximusss", "age": 24},
#            {"name": "Olgha", "age": 25},
#            {"name": "Volodymyr", "age": 5},
#            {"name": "Jack", "age": 45}]
#
# ages = []
# names_lens = []
#
# for person_dict in persons:
#     ages.append(person_dict["age"])
#     names_lens.append(len(person_dict["name"]))
#
# min_age = min(ages)
# max_len_name = max(names_lens)
#
# for person_dict in persons:
#     if person_dict["age"] == min_age:
#         print(person_dict["name"])
#
# for person_dict in persons:
#     if len(person_dict["name"]) == max_len_name:
#         print(person_dict["name"])
#
# mean_age = sum(ages) / len(ages)
# print(mean_age)

# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
# Это одно задание. При выполнении пунктов можно использовать объекты полученные в предыдущих пунктах.
#
# my_dict_1 = {1: 1, 2: 2, 3: 3, 11: 100}
# my_dict_2 = {11: 11, 2: 22}
#
# result_1 = list(set(my_dict_1.keys()).intersection(set(my_dict_2.keys())))
# print(result_1)
#
# result_2 = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))
# print(result_2)
#
# result_3 = {key: my_dict_1[key] for key in result_2}
# print(result_3)
#
# result_4 = my_dict_1.copy()
# for key in my_dict_2:
#     if key in result_4:
#         result_4[key] = [result_4[key], my_dict_2[key]]
#     else:
#         result_4[key] = my_dict_2[key]
# print(result_4)

# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

def change_list(my_list):
    for index in range(0, len(my_list), 2):
        my_list[index] = my_list[index][::-1]
    return my_list


my_list = ["qwe", "asd", "zxc", "123"]
my_list = change_list(my_list)
print(my_list)

# 4.Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.случайное_число_от_100_до_999@строка_случайных_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
from random import randint, choice
from string import ascii_lowercase as alphabet


def create_email(domains, names):
    name = choice(names)
    domain = choice(domains)
    number = randint(100, 999)
    my_str = "".join([choice(alphabet) for _ in range(randint(5, 7))])
    e_mail = f"{name}.{number}@{my_str}.{domain}"
    return e_mail


names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print("----------->>>", e_mail)

# >>>miller.249@sgdyyur.com

