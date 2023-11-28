import random

LIST_LENGTH = 100000

def generate_random_list(length):
    random_list = []
    for _ in range(length):
        number = random.randint(-100, 100)
        random_list.append(number)
    return random_list

def multiply(length):
    some_list = generate_random_list(length)
    result = []
    for i in range(len(some_list)):
        if some_list[i] > 0:
            result.append(some_list[i] * 2)
    return result

def even_odd(length):
    def is_even(num):
        return num % 2 == 0

    numbers = generate_random_list(length)
    counter_odd = 0
    counter_even = 0
    for number in numbers:
        if is_even(number):
            counter_even += 1
        else:
            counter_odd += 1

    return counter_odd, counter_even


def string_concat(length):
    s = ""
    for i in range(length):
        s += str(i)
    return s

def element_in_list(length):
    
    if length <= 2:
        return False
    
    my_list = generate_random_list(length)
    my_list[length-2] = 101
    if 101 in my_list:
        return True
    return False

##
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

##
def count_evens(numbers):
    return len([num for num in numbers if num % 2 == 0])

##
data = {"a": 1, "b": 2, "c": 3}
for key in data:
    data[key] = data[key] * 2
