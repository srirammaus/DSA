

# This works by binary tree struture
# first make the binary tree as max heap
# means the max number should be at the top same followed for below
# Python program for implementation of heap Sort

# To heapify a subtree rooted with node i
# which is an index in arr[].
# def heapify(arr, n, i):
#     # Initialize largest as root
#     largest = i
#
#     #  left index = 2*i + 1
#     l = 2 * i + 1
#
#     # right index = 2*i + 2
#     r = 2 * i + 2
#     # print(l,r,largest,arr[largest])
#     # If left child is larger than root
#     if l < n and arr[l] > arr[largest]:
#         largest = l
#
#     # If right child is larger than largest so far
#     if r < n and arr[r] > arr[largest]:
#         largest = r
#
#     # If largest is not root
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]  # Swap
#
#         # Recursively heapify the affected sub-tree
#         heapify(arr, n, largest)
#
#
# # Main function to do heap sort
# def heapSort(arr):
#     n = len(arr)
#
#     # Build heap (rearrange array)
#     for i in range(n // 2 - 1, -1, -1):
#         # print(i, "hello")
#         heapify(arr, n, i)
#
#     # One by one extract an element from heap
#     print("----")
#     for i in range(n - 1, 0, -1):
#
#         # Move root to end
#         arr[0], arr[i] = arr[i], arr[0]
#
#         # Call max heapify on the reduced heap
#         heapify(arr, i, 0)
#         print(arr)
#

def printArray(arr):
    for i in arr:
        print(i, end=" ")
    print()



# arr = [9, 4, 3, 8, 10, 2, 5]
# heapSort(arr)
# print("Sorted array is ")
# printArray(arr)

# always consider the first elem as largest (note:consider)
def heapify_(arr,n,i):
    largest = i
    leftnode = 2 * i + 1
    rightnode = 2 * i + 2

    if leftnode < n and arr[leftnode] > arr[largest]:
        largest = leftnode
    if rightnode < n and arr[rightnode] > arr[largest]:
        largest = rightnode

    if largest != i: #it means our condition has be validated
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_(arr, n, largest)



nums =  [9, 4, 3, 8, 10, 2, 5]
n = len(nums)
for i in range(n // 2 - 1, -1, -1):
    heapify_(nums, n, i)

for i in range(n - 1, 0, -1):
    nums[0], nums[i] = nums[i], nums[0]

    heapify_(nums, i, 0)
printArray(nums)