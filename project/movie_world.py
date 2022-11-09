from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        current_customer = [c for c in self.customers if c.id == customer_id][0]
        current_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"

        elif current_dvd.is_rented:
            return "DVD is already rented"

        elif current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        else:
            current_dvd.is_rented = True
            current_customer.rented_dvds.append(current_dvd)
            # self.dvds.remove(current_dvd)       # should I remove it from here ?
            return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer = [c for c in self.customers if c.id == customer_id][0]
        current_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if current_dvd in current_customer.rented_dvds:
            current_customer.rented_dvds.remove(current_dvd)
            # self.dvds.append(current_dvd)
            return f"{current_customer.name} has successfully rented {current_dvd.name}"

        else:
            return f"{current_customer.name} does not have that DVD"

    def __repr__(self):
        result = []
        for current_customer in self.customers:
            result.append(str(current_customer))

        for current_dvd in self.dvds:
            result.append(str(current_dvd))

        return "\n".join(result)


c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)

