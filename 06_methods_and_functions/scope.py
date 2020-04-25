x = 25


def printer():
    x = 50
    return x


print(x)  # 25
print(printer())  # 50

name = 'это глобальная строка'


def greet():
    name = 'Влад'

    def hello():
        # name = 'Вася'
        print('Привет, ' + name)

    hello()


greet()

y = 30


def func(y):
    print(f'y равно {y}')
    y = 200
    print(f'я поменял значение y на {y}')


func(y)
print(y)

z = 100


def func_z():
    global z
    print(f'z равно {z}')
    z = 'новое значение'
    print(f'я поменял глобальное значение z на {z}')


func_z()
print(z)
