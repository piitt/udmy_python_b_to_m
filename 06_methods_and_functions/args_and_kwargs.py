def myfunc(*args):
    """return 5% of the sum numbers"""
    return sum(args) * 0.05


print(myfunc(40, 60, 100, 1, 34))


def my_func(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choise is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


my_func(fruit='apple', veggie='lettuce')


def m_func(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


m_func(10, 20, 30, fruit='orange', food='eggs', animal='dog')
