

"""
This is basically used to searching ,
main moto is that lesser values of root are in left and bigger values are in right


"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

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
inOrderTraversal(root)

""""
Obivously we have to see in left"""
def findExistingValue(node,target):
    if node is None:
        return "Not Available"
    if target == node.data:
        return "Exist"
    if target < node.data:
        return findExistingValue(node.left,target)
    else:
        return findExistingValue(node.right,target)



# print(findExistingValue(root,8))


def InsertValue(node,value):
    if node is None:
        return TreeNode(value)

    if value < node.data:
        node.left =InsertValue(node.left,value)
    else:
        node.right = InsertValue(node.right,value)

    return node
# InsertValue(root,22)


# inOrderTraversal(root)

def findLowestValue(node):
    current = node

    while current.left is not None:
        current = current.left
    return current


# findLowestValue(root)
"""
possibilities:
equal: 
greater:
lesser:
case1: if there is no child i mean leaf node then , make right or left accroding to it none
"""
def deletenode(node,data):
    if node is None:
        return

    if data < node.data:
        node.left = deletenode(node.left,data)
    elif data > node.data:
        node.right = deletenode(node.right,data)
    else: #actaul del
        if node.left is None and node.right is not None:
            tmp = node.right
            node = None
            return tmp
        elif node.left is not None and node.right is None:
            tmp = node.left
            node = None
            return tmp

        elif node.left is None and node.right is  None:
            node = None
            return node
        node.data = findLowestValue(node.right).data  #getting the succesor from the right subtree
        node.right = deletenode(node.right,node.data)

    return node


deletenode(root,13)
inOrderTraversal(root)








