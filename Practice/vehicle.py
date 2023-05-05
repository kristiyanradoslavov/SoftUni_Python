from abc import abstractmethod, ABC


class Vehicle:
    AIR_CONDITIONER = 0

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle, ABC):
    AIR_CONDITIONER = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        total_consumption = (self.fuel_consumption + self.AIR_CONDITIONER) * distance

        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        pass


class Truck(Vehicle, ABC):
    AIR_CONDITIONER = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption) 

    def drive(self, distance):
        total_consumption = (self.fuel_consumption + self.AIR_CONDITIONER) * distance

        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        pass
