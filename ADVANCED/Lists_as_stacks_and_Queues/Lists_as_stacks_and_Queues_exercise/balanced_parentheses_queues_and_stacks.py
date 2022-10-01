parentheses_to_check = input()

parentheses_collection = []


for index in range(0, len(parentheses_to_check)):
    current_bracket = parentheses_to_check[index]

    if parentheses_collection:
        if parentheses_collection[- 1] == "(":
            if current_bracket == ")":
                parentheses_collection.pop()
            else:
                parentheses_collection.append(current_bracket)
        elif parentheses_collection[- 1] == "[":
            if current_bracket == "]":
                parentheses_collection.pop()
            else:
                parentheses_collection.append(current_bracket)
        elif parentheses_collection[- 1] == "{":
            if current_bracket == "}":
                parentheses_collection.pop()
            else:
                parentheses_collection.append(current_bracket)

    else:
        parentheses_collection.append(current_bracket)

if parentheses_collection:
    print("NO")
else:
    print("YES")