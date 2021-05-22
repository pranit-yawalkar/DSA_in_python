# Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial.

from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]


def produce_binary_number(n):
    q = Queue()
    q.enqueue("1")
    for i in range(n):
        front = q.front()
        print(" ", front)
        q.enqueue(front + "0")
        q.enqueue(front + "1")
        q.dequeue()


if __name__ == "__main__":
    produce_binary_number(100)
