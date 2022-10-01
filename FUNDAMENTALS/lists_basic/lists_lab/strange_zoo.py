tail = input()
body = input()
head = input()

parts_list = [tail, body, head]

# final_list = [head, body, tail]

parts_list[0], parts_list[2] = parts_list[2], parts_list[0]

print(parts_list)