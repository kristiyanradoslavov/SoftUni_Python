from OOP.inheritence.inheritence_exercise.project_zoo.reptile import Reptile


class Lizard(Reptile):
    def __init__(self, name):
        super().__init__(name)