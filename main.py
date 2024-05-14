class Stack:
    def __init__(self):
        self.values = []

    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)

    def push(self, item):
        self.values.append(item)

    def peek(self):
        if self.is_empty():
            print("Empty stack")
            return None
        else:
            return self.values[-1]

    def pop(self):
        if self.is_empty():
            print("Empty stack")
        else:
            return self.values.pop()




