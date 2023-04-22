import re

dimensions = 6
pattern = r'\(\)'

matrix = [input().split() for r in range(dimensions)]

string = input()

position_information = re.split(pattern, string)

print(position_information)