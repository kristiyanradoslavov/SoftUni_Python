def flights(*args):
    flights_dict = {}

    for current_str in range(0, len(args), 2):
        destination = args[current_str]
        if destination == "Finish":
            break
        passengers = args[current_str + 1]

        if destination not in flights_dict:
            flights_dict[destination] = 0
        flights_dict[destination] += int(passengers)

    return flights_dict


print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))