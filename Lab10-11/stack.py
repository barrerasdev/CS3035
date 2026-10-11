class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)


stack = Stack()
print("Pushing 5 elements: 10, 20, 30, 40, 50")
for elem in [10, 20, 30, 40, 50]:
    stack.push(elem)

print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Current size:", stack.size())
print("Is empty?", stack.isEmpty())
print("Peek top element:", stack.peek())
