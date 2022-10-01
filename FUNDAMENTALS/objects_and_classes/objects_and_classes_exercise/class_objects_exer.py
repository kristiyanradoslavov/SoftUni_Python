class Class:

    def __init__(self, name, attribute__students_count=22):
        self.name = name
        self.students = []
        self.grades = []
        self.attribute__students_count = attribute__students_count

    def add_student(self,name: str, grade: float):
        if len(self.students) < self.attribute__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        result = 0
        if self.students:
            grades_sum = sum(self.grades)
            result = float(grades_sum / len(self.grades))
        return result

    def __repr__(self):
        result = f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade():.2f}"
        return result


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
