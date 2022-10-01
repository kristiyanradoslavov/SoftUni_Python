class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
            self.__animals += 1
        elif species == "fish":
            self.fishes.append(name)
            self.__animals += 1
        elif species == "bird":
            self.birds.append(name)
            self.__animals += 1

    def get_info(self, species):
        names = None
        final_species = ""
        if species == "mammal":
            names = ', '.join(self.mammals)
            final_species = "Mammals"
        elif species == "fish":
            names = ', '.join(self.fishes)
            final_species = "Fishes"
        elif species == "bird":
            names = ', '.join(self.birds)
            final_species = "Birds"

        print(f"{final_species} in {self.zoo_name}: {names} ")
        print(f"Total animals: {self.__animals}")


name_of_the_zoo = input()
animal_count = int(input())

zoo = Zoo(name_of_the_zoo)

for all_animals in range(animal_count):
    current_animal = input().split(" ")
    spec = current_animal[0]
    ani = current_animal[1]
    zoo.add_animals(spec, ani)

final_animal = input()
zoo.get_info(final_animal)
