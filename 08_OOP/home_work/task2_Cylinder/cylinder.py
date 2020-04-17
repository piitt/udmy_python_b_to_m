class Cylinder(object):
    """
    Класс Cylinder с атрибутами высота и радиус основания.
    Класс содержит 2 метода volume (вычисление объема цилиндра) и
    surface_area (нахождение полной поверхности цилиндра)
    """

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        """Вычисление объема цилиндра"""
        return Cylinder.pi * self.radius ** 2 * self.height

    def surface_area(self):
        """Вычисление площади поверхности цилиндра"""
        return 2 * Cylinder.pi * self.radius * (self.height + self.radius)


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())
