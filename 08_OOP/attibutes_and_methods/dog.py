class Dog(object):

    # атрибут класса
    species = 'mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        # Expects boolean True/False
        self.spots = spots

    def bark(self, number):
        print('WOOF! My name is {} and the number {}'.format(self.name, number))


my_dog = Dog(breed='lab', name='Frankie', spots=False)
me_dog = Dog('Lab', 'Rankie', False)

print(type(my_dog))
print(my_dog.name)
print(my_dog.species)
my_dog.bark(10)

print(me_dog.name)
