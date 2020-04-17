class Anymal(object):
    """
    Абстрактный класс создается с целью, что он будет в качестве
    суперкласса для других классов (объязательно наследован)
    От этого класса никогда не будет создан экзепляр класса
    """

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')


class Dog(Anymal):

    def speak(self):
        return self.name + ' says woof!'


class Cat(Anymal):

    def speak(self):
        return self.name + ' says meow!'


fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())
