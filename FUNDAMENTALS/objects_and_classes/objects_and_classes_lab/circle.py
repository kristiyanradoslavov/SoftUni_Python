class Circle:
    __pi_num = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        result = 2 * self.__pi_num * self.radius
        return result

    def calculate_area(self):
        result = self.__pi_num * self.radius ** 2
        return result

    def calculate_area_of_sector(self, angle):
        result = (angle / 360) * self.__pi_num * self.radius ** 2
        return result


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
