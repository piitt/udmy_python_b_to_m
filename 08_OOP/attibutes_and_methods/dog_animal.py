from animal import Animal

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        # super().__init__()
        print('Dog Created')

    # def who_am_i(self):
    #     print('I am a dog!')

    def bark(self):
        print('WOOF!')

    def eat(self) -> None:
        print('I am a dog and eating')


my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()
my_dog.bark()
