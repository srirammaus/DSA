

# Time complexity O(n^2)
# space complextit O(1)
def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        min_value = arr[i]
        current_index = -1
        for j in range(i+1, n):
            # print(arr[j],min_value)
            if(arr[j] < min_value):
                current_index = j
                min_value = arr[j]
        if(current_index != -1):
            print(arr[i],min_value,arr[current_index],current_index,i)
            arr[current_index] = arr[i]
            arr[i] = min_value
            print(arr)
    return  arr

print(selectionSort([4,12,3,2,1,-1,7,-7,-7]))