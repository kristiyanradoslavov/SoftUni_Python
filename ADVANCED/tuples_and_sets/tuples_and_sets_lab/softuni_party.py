number_of_guests = int(input())

guest_list = set()

for _ in range(number_of_guests):
    current_guest = input()
    guest_list.add(current_guest)

current_command = input()

while current_command != "END":
    guest_who_came = current_command
    guest_list.remove(guest_who_came)
    current_command = input()

print(len(guest_list))
for guest in sorted(guest_list):
    print(guest)
