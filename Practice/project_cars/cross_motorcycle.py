from Practice.project_cars.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
