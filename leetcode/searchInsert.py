"""
35. Search Insert Position
Easy
Topics
premium lock icon
Companies
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

"""
This is O(n power 2)  but here asked O(log n)"""
def searchInsert(nums, target):
    n= len(nums)
    maxx = max(nums)
    idx = -1
    for i in range(n):
        if nums[i] == target : #and i != (n-1)
            idx = i
        elif target < maxx and i == (n-1):
            for p in range(n):
                if nums[p] < target:
                    pass
                else:
                    nearby = nums[p]
                    break
            j = nums.index(nearby)
            idx = j  #j-1
        elif target > maxx and i == (n-1):
            idx = n
        else:
            pass
    return idx

# print(searchInsert(nums, target))

# Ologn
def searchInsert2 (nums, target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid  = (left+right)//2
        print("This mid : "+ str(mid) + "   left : " + str(left)  + " right : " + str(right))
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid +1
        elif nums[mid] > target:
            right = mid-1
        else:
            pass
    return left
nums = [100,200,300]
target = 2332

print(searchInsert2(nums, target))