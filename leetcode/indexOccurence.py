
"""28. Find the Index of the First Occurrence in a String
Easy
Topics
premium lock icon
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters."""
def idxOccurence(haystack, needle):
    # needle fully need to be in haystack else -1
    result_index = -1
    k= len(needle)
    M = len(haystack)

    if(k > M):
        return -1
    # print(k)

    for i in range(len(haystack)):
        if(haystack[i] == needle[0]):
            j=0
            while j < k:
                if((i+j) < M):
                    if(haystack[i+j] == needle[j] and j != (k-1)):
                        print("i came inside : " +str(j) + "   K:  " +str(k))
                        j+=1
                    elif(haystack[i+j] == needle[j] and j == (k-1)):
                        print("Atlast here came")
                        result_index = i
                        break
                    else:
                        j = 0
                        break
                else:
                    break
        if(result_index != -1):
            break
    return result_index

print(idxOccurence("mississippi","issippi"))