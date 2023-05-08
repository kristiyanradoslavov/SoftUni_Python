from project.animals.animals import Bird


class Owl(Bird):

    def __init__(self, name, weight, food_eaten, wing_size):
        super().__init__(name, weight, food_eaten, wing_size)

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name, weight, food_eaten, wing_size):
        super().__init__(name, weight, food_eaten, wing_size)

    def make_sound(self):
        return "Cluck"
