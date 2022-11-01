class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if self.data:
            ele = self.data.pop()
            return ele

    def top(self):
        if self.data:
            return self.data[-1]

    def is_empty(self):
        if self.data:
            return False

        return True

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"