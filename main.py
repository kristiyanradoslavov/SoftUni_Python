from OOP.inheritence.inheritence_exercise.project_shop import Drink
from OOP.inheritence.inheritence_exercise.project_shop.food import Food
from OOP.inheritence.inheritence_exercise.project_shop import ProductRepository

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
