def add_songs(*args):
    song_information = {}
    result = []
    new_line = "\n"

    for song, lyrics in args:
        if song not in song_information:
            song_information[song] = lyrics
        else:
            if lyrics:
                song_information[song].append(new_line.join(lyrics))

    for key, value in song_information.items():
        result.append(f"- {key}")
        if value:
            result.append(f"{new_line.join(value)}")

    return "\n".join(result)


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))



