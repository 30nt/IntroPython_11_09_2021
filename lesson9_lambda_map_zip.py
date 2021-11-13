# lambda
# zip
# map

import json

def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data


# def sort_by_len_text(person_dict):
#     text = person_dict["text"]
#     words_count = len(text.split())
#     return words_count

def sort_by_len_text(person_dict):
    return len(person_dict["text"].split())


data_math = read_json("HW/data.json")
data_math_sort_by_len_text = sorted(data_math, key=lambda person_dict: len(person_dict["text"].split()))
print(data_math_sort_by_len_text)

# lambda
my_list = [1, -4, 0.5, 100]

sort_list = sorted(my_list, key=lambda x: abs(50 - x))
print(sort_list)

persons = [{"name": "John", "age": 15},
           {"name": "Anna", "age": 24},
           {"name": "Maximusss", "age": 24},
           {"name": "Olgha", "age": 24},
           {"name": "Volodymyr", "age": 5},
           {"name": "Dan", "age": 5},
           {"name": "Jack", "age": 45}]

sort_by_age = sorted(persons, key=lambda x: (x["age"], len(x["name"])))
print(sort_by_age)

first = [1, 2, 3, 4, 5]
second = [9, 8, 7, 6, 5]
test = list("qwerty")

result = list(zip(first, second, test))
print(result)

result = [numb ** 2 for numb in first]
print(result)

result_map = list(map(lambda x: x ** 2, first))
print(result_map)