def rectangle(length, width):
    def area():
        result = length * width
        return f"Rectangle area: {result}"

    def perimeter():
        result = length * 2 + width * 2
        return f"Rectangle perimeter: {result}"

    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    return area() + "\n" + perimeter()


print(rectangle(2, 10))