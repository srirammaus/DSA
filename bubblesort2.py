

# The bubble sort is O(n^2) time complexity and space complexity is O(1) because only one one array

def bubbleSort(arr):

    n = len(arr)
    for i in range(n-1):
        for j in range(n-1):
            # print((str(j-1)) + " " + str(arr[j-1]))
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
print(bubbleSort([4,3,12,-1,2,1]))