"""
map funcion
"""


def square(num):
    return num ** 2


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


my_nums = [1, 2, 3, 4, 5]
print(list(map(square, my_nums)))

names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer, names)))

"""
filter funcion
"""


def check_even(num):
    return num % 2 == 0


list_nums = [1, 2, 3, 4, 5, 6]

print(list(filter(check_even, list_nums)))

"""
lambda expression
"""


def square_num(num): return num ** 2


print(square_num(3))

# вместо def и названия функции пишем ключевое слово lambda
# lambda num: num ** 2
print(list(map(lambda num: num ** 2, my_nums)))
print(list(filter(lambda num: num % 2 == 0, list_nums)))
