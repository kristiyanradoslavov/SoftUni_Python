from abc import abstractmethod, ABC


class Animal(ABC):
    INCREASE_WEIGHT = 0

    @abstractmethod
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def food_info(self):
        pass

    def feed(self, food):
        current_food = food.__class__.__name__

        if current_food not in self.food_info():
            return f"{self.__class__.__name__} does not eat {current_food}!"
        else:
            food_quantity = food.quantity * self.INCREASE_WEIGHT
            self.weight += food_quantity
            self.food_eaten += food.quantity


class Bird(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)

        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):

    @abstractmethod
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)

        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
