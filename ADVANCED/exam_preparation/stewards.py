from collections import deque

available_seats = input().split(", ")
first_queue = deque(map(int, input().split(", ")))
second_queue = deque(map(int, input().split(", ")))

seat_matches = []
rotations_count = 0

while rotations_count < 10:
    first_num = first_queue.popleft()
    second_num = second_queue.pop()
    rotations_count += 1
    symbol = chr(first_num + second_num)
    first_seat_to_check = f"{first_num}{symbol}"
    second_seat_to_check = f"{second_num}{symbol}"

    if (first_seat_to_check not in seat_matches) and (first_seat_to_check in available_seats):
        seat_matches.append(first_seat_to_check)
    elif (second_seat_to_check not in seat_matches) and (second_seat_to_check in available_seats):
        seat_matches.append(second_seat_to_check)
    elif first_seat_to_check in seat_matches or second_seat_to_check in seat_matches:
        continue
    else:
        first_queue.append(first_num)
        second_queue.appendleft(second_num)
    if len(seat_matches) >= 3:
        break

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations_count}")

