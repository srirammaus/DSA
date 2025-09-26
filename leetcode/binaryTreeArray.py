
binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']


def left_child_index(index):
    return 2 * index + 1

def right_child_index(index):
    return 2 * index + 2

def preOrderTraversal(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None :
        return []
    return [binary_tree_array[index]] + preOrderTraversal(left_child_index(index)) + preOrderTraversal(right_child_index(index))
def inOrderTraversal(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None :
        return []
    return inOrderTraversal(left_child_index(index)) + [binary_tree_array[index]]+inOrderTraversal(right_child_index(index))

def postOrderTraversal(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None :
        return []
    return postOrderTraversal(left_child_index(index)) + postOrderTraversal(right_child_index(index)) + [binary_tree_array[index]]

# pre order in loop
binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']


def pre_order_iterative():
    n = len(binary_tree_array)
    result = []

    # use stack to simulate recursion
    stack = [0]  # start with root index (0)

    while stack:
        index = stack.pop()

        if index >= n or binary_tree_array[index] is None:
            continue  # skip invalid nodes

        # 1️⃣ Visit the node
        result.append(binary_tree_array[index])

        # 2️⃣ Push right child first
        if 2 * index + 2 < n:
            stack.append(2 * index + 2)

        # 3️⃣ Push left child
        if 2 * index + 1 < n:
            stack.append(2 * index + 1)

    return result


# print("Pre-order traversal:", pre_order_iterative())
def post_order_iterative():
    n = len(binary_tree_array)
    result = []

    stack = [0]
    while stack:
        index = stack.pop()
        if index >= n or binary_tree_array[index] is None:
            continue
            # 1️⃣ Visit the node

        # 2️⃣ Push right child first
        if 2 * index + 2 < n:
            stack.append(2 * index + 2)
        # 3️⃣ Push left child
        if 2 * index + 1 < n:
            stack.append(2 * index + 1)


    return result

print(post_order_iterative())

# print(preOrderTraversal(0))
# print(inOrderTraversal(0))
print(postOrderTraversal(0))
