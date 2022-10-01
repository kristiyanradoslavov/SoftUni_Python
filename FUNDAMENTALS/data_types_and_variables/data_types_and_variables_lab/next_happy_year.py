current_year = int(input())

happy_year = False
final_year = set()

while not happy_year:
    final_year = set()
    current_year += 1
    for i in range(len(str(current_year))):
        final_year.add(str(current_year)[i])
        if len(final_year) == len(str(current_year)):
            happy_year = True
            break

print(current_year)

