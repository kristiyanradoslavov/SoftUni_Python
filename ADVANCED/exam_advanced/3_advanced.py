def forecast(*args):
    weather_info = {"Sunny": [], "Cloudy": [], "Rainy": []}

    for i in args:
        current_city = i[0]
        current_weather = i[1]
        weather_info[current_weather].append(current_city)

    final_result = []

    for key, value in weather_info.items():
        for j in sorted(value):
            final_result.append(f"{j} - {key}")

    return "\n".join(final_result)


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))


