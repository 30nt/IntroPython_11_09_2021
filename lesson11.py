# декоратор
# полиморфизм
# магические методы
from time import time


def time_decorator(some_function):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = some_function(*args, **kwargs)
        func_time = time() - start_time
        print("Time:", func_time)
        return result

    return wrapper


@time_decorator
def multiply_number(number):
    result = 1
    for numb in range(1, number + 1):
        result *= numb
    return result


number = 100000

# start_time = time()
# result = multiply_number(number)
# func_time = time() - start_time
# print(func_time)

result = multiply_number(number)
