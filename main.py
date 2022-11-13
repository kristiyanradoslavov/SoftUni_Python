from OOP.polymorphism_and_abstraction.polymorphism_and_abstraction_exercise.project_animals.cat import Cat
from OOP.polymorphism_and_abstraction.polymorphism_and_abstraction_exercise.project_animals.kitten import Kitten

kitten = Kitten("Kiki", 1)
print(kitten.make_sound())
print(kitten)
cat = Cat("Johnny", 7, "Male")
print(cat.make_sound())
print(cat)
