from binarysearchtree import findExistingValue, findLowestValue


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

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print("\n BFS - breadth first search")
def bfs(root):
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


print(bfs(root))
print("\n")
print("\nDepth first search  , pre,in,post")
print("\nPre order")
def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

preOrderTraversal(root)

print("")

print("Pre order while")
def pre_order(node):
    stack = [node]

    while stack:
        node = stack.pop()
        print(node.data, end=", ")
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)




pre_order(root)
print("\n")
print("\nIn order")


def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

inOrderTraversal(root)
print("")
print("In order while")
def in_order(node):
    stack = []
    current = node
    result = []
    while stack or current:

        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            # result.append(current.data)

            print(current.data, end=",")
            current = current.right


in_order(root)
print("\n")
print("\nPost orer Traversal")
def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=",")

postOrderTraversal(root)

print("")
print("Post order while")
def post_order(node):
    stack1 = [node]
    stack2 = []

    while stack1:
        # r= [node_.data for node_ in stack1]
        # print(r)
        node = stack1.pop()
        # stack2.insert(0,node)
        stack2.append(node)
        if node.left is not None:
            stack1.append(node.left)
        if node.right is not None:
            stack1.append(node.right)


    result = [n.data for n in stack2]
    print(result[::-1])  #just you can return result if using stack2.insert(0,node) means everything inserted in statrting




post_order(root)

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# Traverse
print("\nBinary Search Tree , DFS in -order")
inOrderTraversal(root)


print("\nFind Existing Value")
def findExistingValue(node,target):
    if node is None:
        return "not available"
    if node.data == target:
        return "Exists"
    elif target < node.data:
        return findExistingValue(node.left,target)
    else:
        return findExistingValue(node.right,target)


print(findExistingValue(root,3))


print("Find Lowest Value")

def findLowestValue(node):
    current = node
    while current.left:
        current = current.left
    return current

print(findLowestValue(root).data)

print("before InsertNode\n")
inOrderTraversal(root)
def Insertnode(node,data):
    if node is None:
        return TreeNode(data)
    if data < node.data:
        node.left = Insertnode(node.left,data)
    elif data > node.data:
        node.right = Insertnode(node.right,data)

    return node

print("\nafter InsertNode")
Insertnode(root,2)
inOrderTraversal(root)

print("\nDelete node")
def deletenode(node,data):
    if node is None:
        return

    if data < node.data:
        node.left = deletenode(node.left,data)
    elif data > node.data:
        node.right = deletenode(node.right,data)
    else:
        if not node.left:
            temp = node.right
            node =None
            return temp
        elif not node.right:
            temp = node.left
            node =None
            return temp

        node.data = findLowestValue(node.right).data  #replacing the deleted place with in-order sucesor or immmediate right value
        node.right = deletenode(node.right,node.data) # after the replacement of the inorderssucressor or immediate right value their place has be filled with none that works carried by our if not anything becuase there is no right or left value it becomes none

    return node

deletenode(root,15)
inOrderTraversal(root)







binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']


n = len(binary_tree_array)
def left_child_index(index):
    return (2 * index ) + 1
def right_child_index(index):
    return (2 * index) + 2

def pre_order_arr(index):
    # print(index)
    if index >= n or binary_tree_array[index] is None:
        return []
    return [binary_tree_array[index]] + pre_order_arr(left_child_index(index)) + pre_order_arr(right_child_index(index))
def in_order_arr(index):
    # print(index)
    if index >= n or binary_tree_array[index] is None:
        return []
    return  pre_order_arr(left_child_index(index))+[binary_tree_array[index]] + pre_order_arr(right_child_index(index))

def post_order_arr(index):
#     print(index)
    if index >= n or binary_tree_array[index] is None:
        return []
    return  pre_order_arr(left_child_index(index)) + pre_order_arr(right_child_index(index)) +[binary_tree_array[index]]



print("\nIn order Arr ")
print(in_order_arr(0))

print("\nPost order Arr ")
print(post_order_arr(0))

print("\npre order Arr ")
print(pre_order_arr(0))

def pre_order_arr_while(index):
    stack =  [binary_tree_array[index]]
    n = len(binary_tree_array)
    result = []
    i = 0
    while stack:
        current = stack.pop()
        # print(current)
        result.append(current)


        left_child_idx= left_child_index(index)
        right_child_idx = right_child_index(index)

        if left_child_idx < n:
            if binary_tree_array[left_child_idx] is not None:
                stack.append(binary_tree_array[left_child_idx])
                # print(left_child_idx,"The left")
                # print(stack)
                # print(result)
        if right_child_idx < n:

            if binary_tree_array[right_child_idx] is not None:
                stack.append(binary_tree_array[right_child_idx])
                # print(right_child_idx, "The right")
                # print(stack)
                # print(result)


        index+=1



    print("\npre order Arr while ")
    print(result)

pre_order_arr_while(0)
