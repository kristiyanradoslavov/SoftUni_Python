from project.animals.animal import Mammal


class Mouse(Mammal):
    INCREASE_WEIGHT = 0.10

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def food_info(self):
        return ["Vegetable", "Fruit"]


class Dog(Mammal):
    INCREASE_WEIGHT = 0.40

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def food_info(self):
        return ["Meat"]


class Cat(Mammal):
    INCREASE_WEIGHT = 0.30

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def food_info(self):
        return ["Meat", "Vegetable"]


class Tiger(Mammal):
    INCREASE_WEIGHT = 1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def food_info(self):
        return ["Meat"]


