from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    # Excersice 1: Reverse the string using stack
    def reverse_string(self, val):
        for char in val:
            self.container.append(char)
        rstr = ""
        for char in range(len(self.container)):
            rstr += self.container.pop()
        return rstr


        # while(len(self.container!=0)):
        # rstr+=self.container.pop()
        # return rstr
s = Stack()
print(s.is_empty())
print(s.reverse_string("We will conquere COVID-19"))
