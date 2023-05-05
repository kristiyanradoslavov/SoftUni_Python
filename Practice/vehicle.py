from abc import abstractmethod, ABC


class Vehicle(ABC):
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


class Car(Vehicle):
    AIR_CONDITIONER = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        total_consumption = (self.fuel_consumption + self.AIR_CONDITIONER) * distance

        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle, ABC):
    AIR_CONDITIONER = 1.6
    FUEL_LEAKAGE = 0.5

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption) 

    def drive(self, distance):
        total_consumption = (self.fuel_consumption + self.AIR_CONDITIONER) * distance

        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        remaining_fuel = fuel * 0.95
        self.fuel_quantity += remaining_fuel
