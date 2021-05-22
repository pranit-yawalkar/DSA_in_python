# The issue with using a list as a stack is that list uses dymanic array internally and when it reaches its capacity it will reallocate a big chunk of memory somewhere else in memory area and copy all the elements.

# Using deuque as stack
from collections import deque
from typing import Mapping
stack = deque()

# dir(stack)
stack.append("https://www.cnn.com/")
print(stack)
stack.append("https://www.cnn.com/world")
stack.append("https://www.cnn.com/india")
stack.append("https://www.cnn.com/china")
print(stack)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
# stack.pop()
print(stack)

# Making a custom Stack data structure


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


s = Stack()
print(s.is_empty())
# s.push(5)
# s.push(56)
# s.push(57)
# print(s.pop())
# print(s.peek())
