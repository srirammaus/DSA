# This file contains all sorting algorithms you have pratied , this is your test


#Bubble sort
# Taking array of inputs, solving it in n-1 manner because if four items three pair is going be processed
# For your understanfing generally in algorithms  "Edhu kuda comare panramo adhu pakam arrow small ah irukanum" for if condfition
def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                print(arr,arr[j],arr[j+1])
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# print(bubbleSort([4,3,2,1]))

# Insertion sort
# Works in Reverse Pattern not in reverese order if [4,3,2,1]  4 should be consider as sorted and from 3 and 4 comparision started , then followin g happen
def insertionSort(arr):
    n = len(arr)

    for i in range (1,n):
        current_idx = i
        for j in range(i-1, -1, -1):
            print(arr[j])
            print(arr[current_idx])
            if arr[j] > arr[current_idx]:
                arr[j],arr[current_idx] = arr[current_idx], arr[j]
                current_idx = j

        print("---")
    return arr
# print(insertionSort([4,3,2,1]))

# Quicksort , divding by taking a pivot element small should be left and big should be right
def quickSort(arr):
    n = len(arr)
    if(len(arr) <=1):
        return arr
    pivot_element = arr[-1]

    left = [x for x in arr[:-1] if x < pivot_element]
    right = [y for y in arr[:-1] if y > pivot_element]

    left = quickSort(left)
    right = quickSort(right)

    print(left)
    print(right)

    return left + [pivot_element] + right
# print(quickSort([4,3,2,1]))
def selectionSort(arr):
    return arr

# counting sort algorithm
# get the max or biggest value
def countingSort(arr):
    n = len(arr)
    maxx =  max(arr)
    myarray = [0] * (maxx+1)
    for i in range(n):
        val = arr[i]
        myarray[val] +=1
    arr = []
    for  j in range(len(myarray)):
        while myarray[j] > 0:
            arr.append(j)
            myarray[j] -= 1
    return arr

print(countingSort([7,6,4,4,44,5,9]))
# RadixSort
# Taking the max elem and go from one to 100 th place
# make it in ascending
# Radix sort not for negative
def RadixSort(arr):
    n = len(arr)
    # get the max value
    # print ((maxx // 1000) % 10)

    maxx = max(arr)
    radixArray = []
    for i in range(10):
        radixArray.append([])
    i = 0
    divider = str(1)
    # print(radixArray)
    # print ((maxx // 10) % 10)
    while i < len(str(maxx)):
        if i != 0:
            divider = str(divider) + "0"

        for j in range(n):
            c_idx = (arr[j] // int(divider)) % 10
            print(c_idx,arr[j],divider)
            radixArray[c_idx].append(arr[j])
        print(radixArray)
        arr= []
        for k in range(len(radixArray)):
            if radixArray[k] != []:
                while  range(len(radixArray[k])):
                    val = radixArray[k].pop(0)
                    arr.append(val)
                    # print(val,"This is the elem",l)
                    # print("It reached the firs attempt")
        print(arr)
        # print(arr)
        # print("Our array is now empy")
        # print(arr)

        # for k in range(n):
        #     radixArray

        i+=1

    return arr

# print(RadixSort([3564,44,33,22,45,11,13]))
def TwoSum(arr):
    return arr
def mergerSort(arr):
    return arr
def merge(arr):
    return arr