from project.animals.animal import Bird


class Owl(Bird):
    INCREASE_WEIGHT = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def food_info(self):
        return ["Meat"]


class Hen(Bird):
    INCREASE_WEIGHT = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def food_info(self):
        return ["Meat", "Vegetable", "Fruit", "Seed"]
