import re

pattern = r"(www\.[A-Za-z0-9\-]+(\.[a-z]+)+)"
sentences = input()

while True:
    if sentences:
        result = re.findall(pattern, sentences)
        if result:
            print(result[0][0])
    else:
        break
    sentences = input()
