def concatenate(*args, **kwargs):
    concatenated_str = ""
    for i in args:
        concatenated_str += i

    for key, value in kwargs.items():
        if key in concatenated_str:
            concatenated_str = concatenated_str.replace(key, value)

    return concatenated_str


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))