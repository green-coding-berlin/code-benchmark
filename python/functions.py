import random
MIN = -100
MAX = 100

def generate_random_list(length):
    random_list = []
    for _ in range(length):
        number = random.randint(MIN, MAX)
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

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def count_evens(numbers):
    return len([num for num in numbers if num % 2 == 0])

def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp
    return my_list

def swap_elements(length):
    my_list = generate_random_list(length)
    for i in range(length - 2):
        swap(my_list,i ,i + 1)
    return my_list

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def run_matrices(length):
    a = generate_random_list(length)
    b = generate_random_list(length)
    c = generate_random_list(length)
    d = generate_random_list(length)
    return add_matrices([a,b], [b,c])

def list_for_find(length):
    randome_elements = random.sample(range(MIN, MAX), 100)
    list_seq = list(generate_random_list(length))

    counter = 0
    for ele in randome_elements:
        if ele in list_seq:
            counter += 1

    return counter