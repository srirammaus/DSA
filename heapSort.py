

# This works by binary tree struture
# first make the binary tree as max heap
# means the max number should be at the top same followed for below
def heapify(arr):
    """
    each node gonna have two leaf nodes
    :param arr:
    :return:
 """
    n= len(arr)



    return

def heapSort(arr):

    return
def binary_tree(arr):
    n = len(arr)
    track = 0
    i = 0
    while i < n:
        count = 2 ** track
        print(count)
        print(arr[i:min(i + count, n)])
        i += count
        track += 1

heapify([1,2,3,4,5,6,7,8])