
class queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
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

class Listnode():
    def __init__(self, data=0,next=None):
        self.data = data
        self.next = next

    def add(self,data=0,head=None):
        if head == None:
            head = self
        node = Listnode(data)
        head.next = node
        return node

def printr(node):
    current_node = node
    while current_node:
        print(current_node.data)
        current_node = current_node.next

# node1 = Listnode("admin")
# node2 =node1.add("user",node1)
# node3 =node1.add("guest",node2)
# node4 =node1.add("moderator",node3)
# node5 =node1.add("superuser",node4)
# node6 =node1.add("member",node5)
#
# printr(node1)

class queue2:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    def enqueue(self,data):
        if self.front is None:
            self.front = Listnode(data)
            self.rear = self.front
            self.size += 1
            return
        new_node = Listnode(data)
        self.rear.next = new_node
        self.rear = new_node
        self.size += 1
        return self.rear

    def dequeue(self):
        if self.front is None:
            self.rear = None
            return
        temp = self.front
        self.front = self.front.next
        self.size -= 1
        return temp.data
    def size(self):
        return self.size
    def isEmpty(self):
        return self.size == 0
    def peek(self):
        if self.front is not None:
            return self.front.data
        else:
            return "Queue is empty"
    def printr(self):
        current_node = self.front
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        print("------")
myqueue2 = queue2()
myqueue2.enqueue("admin")
myqueue2.enqueue("user")
myqueue2.enqueue("guest")
myqueue2.enqueue("moderator")
myqueue2.enqueue("superuser")

myqueue2.printr()
myqueue2.dequeue()
myqueue2.dequeue()
myqueue2.dequeue()
myqueue2.dequeue()
print(myqueue2.dequeue())

myqueue2.printr()

# myqueue = queue()
# myqueue.enqueue('1')
# myqueue.enqueue('2')
# myqueue.enqueue('3')
# myqueue.enqueue('4')
# print(myqueue.size())
# print(myqueue.isEmpty())
# print(myqueue.isFull())
# print(myqueue.peek())
# myqueue.dequeue()
# print(myqueue.size())
# myqueue.busrtQueue()
# print(myqueue.size())
