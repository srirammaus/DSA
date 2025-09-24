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


class queue:
    def __init__(self):
        self.queue = []
    def push(self, item):
        self.queue.append(item)
    def pop(self):
        return self.queue.pop(0)
    def isEmpty(self):
        return self.queue == []
    def size(self):
        return len(self.queue)
    def isFull(self):
        print(len(self.queue),self.size())
        return self.size() == len(self.queue)
    def peek(self):
        return self.queue[0]
    def busrtQueue(self):
        self.queue=[]
        return self.queue

myqueue = queue()
myqueue.push('1')
myqueue.push('2')
myqueue.push('3')
myqueue.push('4')
print(myqueue.size())
print(myqueue.isEmpty())
print(myqueue.isFull())
print(myqueue.peek())
myqueue.pop()
print(myqueue.size())
myqueue.busrtQueue()
print(myqueue.size())
