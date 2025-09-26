

class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None



root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')


root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

# nodeB.left = nodeE
# nodeB.right = nodeF

# nodeF.left = nodeG


def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=' ')
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

# preOrderTraversal(root)

"""
This belows follow LIFO order read this , this will clearly understand """
def pre_order(node):

    stack = [node]
    result = []
    while stack:

        current = stack.pop()
        result.append(current.data)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    print(result)


# pre_order(root)

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data,end=",")
    inOrderTraversal(node.right)

# inOrderTraversal(root)


def in_order(node):
    stack = []
    result = []
    current = node
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            result.append(current.data)

            current = current.right


    print(result)

# in_order(root)



def postOrderTraversal(node): #last left #right #parent
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data,end=",")


postOrderTraversal(root)
"""
left right parent

right or parent . right priotty
right or left decsenad . left descendant is pripry
"""
def post_order(node):
    stack1 = [node]
    stack2 = []
    result = []
    current = node

    while stack1:
        current = stack1.pop()
        stack2.append(current)
        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)

    while stack2:
        result.append(stack2.pop().data)

    print(result)

print(post_order(root))


# def in_order(node):
#
#     stack = []  #instead of recursion
#     result = []
#     current = node
#     while stack or current:
#         # 1. Go all the way to the left
#         if current:
#             stack.append(current)
#             current = current.left
#         else:
#             # 2. Pop from stack (visit node)
#             current = stack.pop()
#             result.append(current.data)
#
#             # 3. Then go to right subtree
#             current = current.right
#
#     return result


# if not node:
#     return []
#
# stack1 = [node]
# stack2 = []
# result = []
#
# while stack1:
#     current = stack1.pop()
#     stack2.append(current)
#
#     if current.left:
#         stack1.append(current.left)
#     if current.right:
#         stack1.append(current.right)
#
# while stack2:
#     result.append(stack2.pop().data)
#
# return result