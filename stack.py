class stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def isEmpty(self):
        return self.stack == []
    def size(self):
        return len(self.stack)

# mystack = stack()
# print(mystack.isEmpty())
# mystack.push(10)
# print(mystack.isEmpty())
# print(mystack.size())
# mystack.push(20)
# mystack.push(30)
# mystack.pop()
# print(mystack.size())

