target_sequence = list(map(int, input().split(" ")))
command = input()
shot_targets = 0

while command != "End":
    current_command = int(command)
    if len(target_sequence) - 1 >= current_command >= 0:
        target_before_shot = target_sequence[current_command]
        target_sequence[current_command] = -1
        shot_targets += 1
        for index, char in enumerate(target_sequence):
            if char > target_before_shot:
                target_sequence[index] -= target_before_shot
            elif char > -1:
                target_sequence[index] += target_before_shot

    command = input()

shot_targets_info = " ".join(str(x) for x in target_sequence)

print(f"Shot targets: {shot_targets} -> {shot_targets_info}")
