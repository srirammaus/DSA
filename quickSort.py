

def quickSort (arr):
    # Taking pivot element , which is last element

    if(len(arr) <= 1):
        print("never called")
        return arr
    p = arr[-1]

    left = [x for x in arr[:-1] if x < p]
    right = [y for y in arr[:-1] if y > p]
    print(left)
    print(right)

    left = quickSort(left)
    right = quickSort(right)
    return left + [p] + right

print(quickSort([4,13,3,2,12,5,-1]))