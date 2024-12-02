import math
class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = sides
        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        return  False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, sides):
        m = False
        for i in sides:
            if i < 0:
                m = True
                break
        if m and len(sides) != self.__sides:
            return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__radius = self.get_sides()[0][0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3
    def get_square(self):
       a, b, c = self.get_sides()
       s = (a + b + c) / 2
       return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(*([self.get_sides()[0]] * self.sides_count))

    def get_volume(self):
        side_one = self.get_sides()[0]
        return side_one ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)


# Проверка на изменение цветов:

circle1.set_color(55, 66, 77) # Изменится

#print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится

#print(cube1.get_color())



# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5) # Не изменится

print(cube1.get_sides())

circle1.set_sides(15) # Изменится

print(circle1.get_sides())



# Проверка периметра (круга), это и есть длина:

print(len(circle1))



# Проверка объёма (куба):

print(cube1.get_volume())