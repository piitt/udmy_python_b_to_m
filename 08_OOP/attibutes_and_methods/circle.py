class Circle(object):

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        # атрибут для площади круга
        # self.area = radius ** 2 * self.pi
        self.area = radius ** 2 * Circle.pi

    def get_circumference(self):
        """расчет длины окружности"""
        return self.radius * self.pi * 2


my_circle = Circle(30)
print(my_circle.get_circumference())
print(my_circle.radius)
print(my_circle.pi)
print(my_circle.area)
