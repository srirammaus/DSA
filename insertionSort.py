
# Time complexity O(n^2)
#space complexity O(1)
def insertionSort(arr):
        # It should cccur reverse order , it does not mean 1st picking elem is from last ,
        # if you are sorting 2 and 1 elem then 2 and 1 is comparing , so it is called reverse
        n = len(arr)
        for i in range(1,n):
            current_val_idx = i
            print(i,"This is i")
            for j in range(i-1,-1,-1):
                print(arr[j])
                print(arr[current_val_idx])

                if arr[j] > arr[current_val_idx]:
                    arr[j],arr[current_val_idx] = arr[current_val_idx],arr[j]
                    current_val_idx = j
                    print(arr)

            print("-----")
        return  arr

print(insertionSort([4,3,2,1,-1,12,-17]))