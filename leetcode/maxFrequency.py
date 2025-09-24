

"""“Find the maximum frequency of any element in the array, then return the sum of occurrences of all elements that have this maximum frequency.”"""

def maxFrequency(nums):
    n = len(nums)
    stack = {}
    for i in range(n):
        if stack.get(nums[i]):
            stack[nums[i]] += 1
        else:
            stack[nums[i]] = 1
    allFreq = stack.values()
    v = max(allFreq)
    freq = 0
    for i in allFreq:
        if(i == v):
            freq += v

    return freq
maxfreq = maxFrequency([3,2,2,3])
print(maxfreq)