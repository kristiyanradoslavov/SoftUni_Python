class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return f"{self.name} {other.surname}"


class Group:

    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return self.people

    def __add__(self, other):
        name = f"{self.name} {other.name}"
        first_people = self.people
        second_people = other.people
        first_people.extend(second_people)
        return first_people


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3
first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group
print(third_group)