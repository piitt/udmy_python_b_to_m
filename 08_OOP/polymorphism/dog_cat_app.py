from dog import Dog
from cat import Cat

niko = Dog('niko')
print(niko.speak())

felix = Cat('felix')
print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

print('=================')
pet_speak(niko)
pet_speak(felix)
