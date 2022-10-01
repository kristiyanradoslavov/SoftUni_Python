count_of_numbers = int(input())

list_of_positives = []
list_of_negatives = []

for i in range(count_of_numbers):
    current_num = int(input())
    if current_num >= 0:
        list_of_positives.append(current_num)
    else:
        list_of_negatives.append(current_num)

print(list_of_positives)
print(list_of_negatives)
print(f"Count of positives: {len(list_of_positives)}")
print(f"Sum of negatives: {sum(list_of_negatives)}")
