from collections import deque

seats = input().split(", ")
first_row = deque(map(int, input().split(", ")))
second_row = deque(map(int, input().split(", ")))

rotations = 0
taken_seats = []

while rotations < 10 and len(taken_seats) < 3:
    rotations += 1
    first_num = first_row.popleft()
    last_num = second_row.pop()
    num_sum = first_num + last_num
    symbol = chr(num_sum)
    seat_found = False

    first_seat_to_check = f"{first_num}{symbol}"
    second_seat_to_check = f"{last_num}{symbol}"

    if first_seat_to_check in seats and first_seat_to_check not in taken_seats:
        seat_found = True
        taken_seats.append(first_seat_to_check)

    if second_seat_to_check in seats and second_seat_to_check not in taken_seats:
        seat_found = True
        taken_seats.append(second_seat_to_check)

    if not seat_found:
        first_row.append(first_num)
        second_row.appendleft(last_num)

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")

