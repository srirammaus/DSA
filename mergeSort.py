
def mergerSort(arr,test=0):
    if len(arr) == 1:
        if test == 0: print(arr)
        return arr
    # divding by mid
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    left = mergerSort(leftHalf)
    right = mergerSort(rightHalf,1)
    # print("left: ",left)
    # print("right: ",right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j=  0
    # print("left :" ,left,"right:", right)
    while i < len(left) and j < len(right):
        # print(j)
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    print("---")
    print(left[i:] , right[j:])
    print("---")
    return result
    #
    # result = []
    # i = j = 0
    #
    # while i < len(left) and j < len(right):
    #     if left[i] < right[j]:
    #         result.append(left[i])
    #         i += 1
    #     else:
    #         result.append(right[j])
    #         j += 1
    #
    # result.extend(left[i:])
    # result.extend(right[j:])
    # return result

print(mergerSort([4,3,2,-1, -17,19]))