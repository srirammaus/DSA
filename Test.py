

# def test (arr):
#
#     if(len(arr) == 1):
#         return arr
#
#
#     mid = int(len(arr)/2)
#     left = arr[:mid]
#     right = arr[mid:]
#
#     left_  = test(left)
#     right_ = test(right)
#
#     print("left:" ,left_)
#     print("right : ",right_)
# test([3, 7, 6, -10, 15, 23.5, 55, -13])
# i =0
# j=0
# while i < 3 and j < 2:
#     print("hello world")
#     i+=1

# my_list = [1, 2, 3]
# another_list = [4, 5, 6]
#
# my_list.extend(another_list)
#
# print(my_list)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# def traverseAndPrint(head):
#     currentNode = head
#     while currentNode:
#         print(currentNode.data, end=" -> ")
#         currentNode = currentNode.next
#     print("null")
#
# def deleteSpecificNode(head, nodeToDelete):
#
#     if head == nodeToDelete:
#         print("function has to return here")
#         return head.next
#     print("function wont come  here")
#     currentNode = head
#     i = 1
#     while currentNode.next and currentNode.next != nodeToDelete:
#         print("node ",i)
#         i+=1
#         currentNode = currentNode.next
#
#     if currentNode.next is None:
#         return head
#     print("function wont come  here")
#     currentNode.next = currentNode.next.next
#
#     return head
#
# node1 = Node(7)
# node2 = Node(11)
# node3 = Node(3)
# node4 = Node(2)
# node5 = Node(9)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
#
# print("Before deletion:")
# traverseAndPrint(node1)
#
# # Delete node4
# nodes = deleteSpecificNode(node1, node4)
#
# print("\nAfter deletion:")
# traverseAndPrint(nodes)
#
#Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")


def insertNodeAtPosition(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode

    currentNode = head
    for _ in range(position - 2):
        print("current node data",currentNode.data)
        if currentNode is None:
            print('This never prints')
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4


node5 = Node(11)

print("Original list:")
traverseAndPrint(node1)

# Insert a new node with value 97 at position 2
newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 5)

print("\nAfter insertion:")
traverseAndPrint(node1)

# Python