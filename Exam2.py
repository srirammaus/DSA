


def bubble_sort(arr):
    n= len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# comparing reverly
# consider 1 elem is sorted
# min value should be come front
# min avl should be in front then only it is real sorted
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        current_idx = i
        for j in range(i-1,-1,-1):
            if(arr[j] > arr[current_idx]):
                arr[j],arr[current_idx] = arr[current_idx],arr[j]
                current_idx = j
    return arr

# move the lowest elem to front
def selection_sort(arr):
    n = len(arr)
    for i in  range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if(arr[j] < arr[min_idx]):
                min_idx = j
        if(arr[min_idx] != 0):
            arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr


def merge_sort(arr):
    n = len(arr)
    if n <= 1:

        return arr
    # divide the arr
    mid = n//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left,right):
    result = []
    i=j= 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# taking a pivot element
# in merge sort classifying is based on mid elem, here pivot element

def quickSort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    p = arr[-1]
    left = [x for x in arr[:-1] if x <= p ]
    right = [y for y in arr[:-1] if y > p]

    lefthalf = quickSort(left)
    righthalf = quickSort(right)

    return lefthalf + [p] + righthalf

# for general recursion , you have to minimize the respected array for each recursion
def generalRecursion(arr):
    if(len(arr) <= 1):
        print("recursion going back from here 10")
        return arr

    p = arr[-1]

    left = [x for x in arr[:-1] if x > p]
    right = [y for y in arr[:-1] if y > p]
    print(left)
    generalRecursion(left)
    print("recursion going back from here "+ str(p))
    return left



def DualRecursion(arr):
    if(len(arr) <= 1):
        print("recursion going back from here ")
        return arr

    p = arr[-1]

    left = [x for x in arr[:-1] if x < p]
    right = [y for y in arr[:-1] if y > p]
    print(left)
    print(right)
    DualRecursion(left)
    DualRecursion(right)
    print("recursion going back from here "+ str(p))
    return left
# DualRecursionarr = [10,9,8,7,6,1,4,3, 2, 5]
# DualRecursion(DualRecursionarr)
def Recursion(arr):
    n = len(arr)
    if(len(arr) <= 1):
        return arr

    p = n // 2

    left = [x for x in arr[:-1] if x < p]
    print(left)
    Recursion(left)

    return left

Recursion([3,4,1,2])
# using the elements place
# quotient - upper part , dividend - inner value , divsor - side value , remarider  - below value
def radixSort(arr):
    n= len(arr)
    # (elem // 1 (This shoudl be increaded accordign to place you need) ) % 10 -  the formula
    sortedArr= []
    divider= 1
    maxx = max(arr)
    minx = min(arr)
    for i in range(10):
        sortedArr.append([])
    # print(sortedArr)
    i =0
    while i < len(str(maxx)):
        for k in range(n):
            place = (arr[k] // divider) % 10
            sortedArr[place].append(arr[k])
        print(arr)

        arr = []
        for j in range(len(sortedArr)):
            radixArray = sortedArr[j]
            while radixArray != [] :
                arr.append(radixArray[0])
                # print(radixArray)
                radixArray.pop(0)

        divider = divider * 10
        i+=1
    return arr

def countingSort(arr):
    n= len(arr)
    maxx = max(arr)

    countingArr = [0] * (maxx+1)
    for i in range(n):
        c_val = arr[i]
        countingArr[c_val] +=1
    newArr= []
    for j in range(len(countingArr)):
        while countingArr[j] != 0:
            newArr.append(j)
            countingArr[j] -= 1
    return newArr

# print(10 | 14) it seems like OR operation and binary addition same but not , if the additiom done without carry it behaves like actual OR operation , but unfortunaltely addition done done only with carry. but addition and XOR operator are same evn with carry
# arr= [9,8,7,6,5,5]
# print(countingSort(arr))


