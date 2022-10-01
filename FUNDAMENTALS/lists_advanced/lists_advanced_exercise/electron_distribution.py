number_of_electrons = int(input())

shell = []
n = 1

while number_of_electrons > 0:
        formula = 2 * n ** 2
        if number_of_electrons >= formula:
            shell.append(formula)
            number_of_electrons -= formula
        else:
            shell.append(number_of_electrons)
            number_of_electrons -= number_of_electrons
        n += 1

print(shell)