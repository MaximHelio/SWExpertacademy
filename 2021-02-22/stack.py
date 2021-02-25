# Last In First Out

class stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        if len(self.stack) == 0: return
        return self.stack.pop(-1)

    def top(self):
        n = self.stack[-1]
        return n

stack_a = stack()
stack_a.push(1)
stack_a.push(2)
stack_a.push(3)
print(stack_a.pop())
print(stack_a.pop())
print(stack_a.pop())
print(stack_a.pop())
