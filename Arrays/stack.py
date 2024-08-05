class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1
    def is_Empty(self):
        return self.top == -1
    def if_full(self):
        return self.size == self.top - 1

    def push(self, item):
        if self.if_full():
            print("Stack is full")
        else:
            self.top += 1
            self.stack[self.top] = item

    def pop(self):
        if self.is_Empty():
            print("Stack is empty")
            return None
        else:
            item = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return item

    def peek(self):
        if self.is_Empty():
            print("Stack is empty")
            return None
        else:
            return self.stack[self.top]

stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.pop())
print(stack.peek())