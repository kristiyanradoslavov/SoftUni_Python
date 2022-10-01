count_of_rooms = int(input())

free_chairs = 0
room_number = 0
room_without_chars = False

for rooms in range(0, count_of_rooms):
    current_room = input().split(' ')
    room_number += 1
    available_charis = len(current_room[0])
    count_of_people = int(current_room[1])
    if available_charis >= count_of_people:
        free_chairs += available_charis - count_of_people
        continue
    else:
        room_without_chars = True
        chairs_needed = abs(available_charis - count_of_people)
        print(f"{chairs_needed} more chairs needed in room {room_number}")

if room_without_chars is False:
    print(f"Game On, {free_chairs} free chairs left")
