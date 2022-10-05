try:
    result = open("my_first_file.txt", "x")
    result.close()
except:
    print("File already created")

with open("my_first_file.txt", "w") as file:
    file.write("I just created my first file!")

