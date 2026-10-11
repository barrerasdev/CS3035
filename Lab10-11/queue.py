class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        return None

    def size(self):
        return len(self.items)


queue = Queue()
print("Enqueueing 6 elements: A, B, C, D, E, F")
for elem in ['A', 'B', 'C', 'D', 'E', 'F']:
    queue.enqueue(elem)

print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Enqueueing 2 more: G, H")
queue.enqueue('G')
queue.enqueue('H')
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Current size:", queue.size())
print("Is empty? :", queue.isEmpty())
print("Peek front element:", queue.peek())
