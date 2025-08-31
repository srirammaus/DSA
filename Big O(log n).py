def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        print(str(low ) + " " + str(high) +" " +str(mid))
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


print(binary_search([1, 2, 3, 4,5,6,7,8],1 ))
