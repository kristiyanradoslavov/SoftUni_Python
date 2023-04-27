class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if price > self.__budget:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            current_worker = next(filter(lambda w: w.name == worker_name, self.workers))
            self.workers.remove(current_worker)
            return f"{worker_name} fired successfully"

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum([s.salary for s in self.workers])

        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animal_expenses = sum([e.money_for_care for e in self.animals])

        if self.__budget >= animal_expenses:
            self.__budget -= animal_expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animal_count = len(self.animals)
        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]
        result = [f"You have {animal_count} animals", f"----- {len(lions)} Lions:"]

        for lion in lions:
            result.append(repr(lion))

        result.append(f"----- {len(tigers)} Tigers:")
        for tiger in tigers:
            result.append(repr(tiger))

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        for cheetah in cheetahs:
            result.append(repr(cheetah))

        return '\n'.join(result)

    def workers_status(self):
        workers_count = len(self.workers)
        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]
        result = [f"You have {workers_count} workers", f"----- {len(keepers)} Keepers:"]

        for keeper in keepers:
            result.append(repr(keeper))

        result.append(f"----- {len(caretakers)} Caretakers:")
        for caretaker in caretakers:
            result.append(repr(caretaker))

        result.append(f"----- {len(vets)} Vets:")
        for vet in vets:
            result.append(repr(vet))

        return "\n".join(result)
