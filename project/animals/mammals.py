from project.animals.animals import Mammal


class Mouse(Mammal):

    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name, weight, food_eaten, living_region)

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):

    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name, weight, food_eaten, living_region)

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):

    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name, weight, food_eaten, living_region)

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):

    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name, weight, food_eaten, living_region)

    def make_sound(self):
        return "ROAR!!!"
