from abc import abstractmethod, ABC


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food):
        current_food = food.__class__.__name__


class Bird(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, food_eaten, wing_size):
        super().__init__(name, weight, food_eaten)

        self.wing_size = wing_size


class Mammal(Animal, ABC):

    @abstractmethod
    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name, weight, food_eaten)

        self.living_region = living_region
