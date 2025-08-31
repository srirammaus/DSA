



# combining merge sort and insertion sort
# run limit is 32
# Python3 program to perform basic timSort
MIN_MERGE = 32


def calcMinRun(n):
    """Returns the minimum length of a
    run from 23 - 64 so that
    the len(array)/minrun is less than or
    equal to a power of 2.

    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 127=>64, 128=>32, ...
    """
    r = 0
    print(n)
    while n >= MIN_MERGE:
        r |= n & 1
        print("This n , r size", n , r)
        n >>= 1
    return n + r


# This function sorts array from left index to
# to right index which is of size atmost RUN
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# Merge function merges the sorted runs
def merge(arr, l, m, r):

    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # Copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    # Copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


# Iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
    print(minRun)
    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)

    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = minRun
    while size < n:

        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):

            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size


# Driver program to test above function
if __name__ == "__main__":

    arr = [ 6, 70,74, 29, 6, 70, 116, 12, 65, 111, 80, 40, 117, 14, 73, 122, 61, 2, 118, 110, 120, 4, 92, 45, 8, 51, 79, 86, 96, 1, 97, 81, 43, 32, 33, 22, 77, 49, 75, 0, 102, 20, 62, 36, 59, 25, 67, 93, 30, 21, 10, 38, 18, 17, 91, 48, 39, 100, 106, 95, 119, 34, 44, 28, 11, 105, 26, 7, 47, 104, 72, 13, 98, 88, 63, 31, 85, 42, 87, 54, 16, 58, 109, 108, 3, 94, 41, 84, 55, 76, 35, 56, 83, 101, 24, 107, 9, 68, 66, 27, 60, 78, 37, 5, 19, 52, 23, 57, 103, 69, 71, 99, 53, 64, 15, 50, 89, 90, 46, 112, 113, 114, 115, 121, 82]



    #print("Given Array is")
    #print(arr)

    # Function Call
    timSort(arr)

    #print("After Sorting Array is")
    print(arr)