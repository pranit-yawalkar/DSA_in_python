from collections import deque

# Using list as a queue
'''
wmt_score_price_queue = []

wmt_score_price_queue.insert(0, 131.10)
wmt_score_price_queue.insert(0, 131.12)
wmt_score_price_queue.insert(0, 135)

print(wmt_score_price_queue)
print(wmt_score_price_queue.pop())
print(wmt_score_price_queue.pop())
print(wmt_score_price_queue.pop())
print(wmt_score_price_queue.pop()) # But list has issues with dynamic memory allocation

'''

# Using collections.deque as queue
'''

from collections import deque
q = deque()
q.appendleft(5)
q.appendleft(8)
q.appendleft(10)
print(q)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

'''
# Implementing queue class using collections.deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


pq = Queue()
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(pq.size())
print(pq.dequeue())
print(pq.dequeue())
