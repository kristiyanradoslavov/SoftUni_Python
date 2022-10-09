def add_songs(*args):
    final_string = {}
    for i in range(len(args)):
        if args[i][0] not in final_string:
            final_string[args[i][0]] = []
        if args[i][1]:
            final_string[args[i][0]].append(args[i][1])

    final_result = ""
    for key, value in final_string.items():
        final_result += f'- {key}\n'
        for i in range(len(value)):
            for j in range(len(value[i])):
                final_result += f"{value[i][j]}\n"

    return final_result[:-1]


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))


