def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        print(str(low ) + " " + str(high) +" " +str(mid) + " "+str(arr[mid]) )
        if arr[mid] == target:
            print("first")
            return mid
        elif arr[mid] < target:
            print("second")
            low = mid + 1
        else:
            print("third")
            high = mid - 1
    return None
print(binary_search([1, 2, 3, 4,5,6,7,8],3 ))
