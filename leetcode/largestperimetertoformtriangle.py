"""
Given an integer array nums,
return the largest perimeter of a triangle with a non-zero area,
 formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.



Example 1:

Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
Example 2:

Input: nums = [1,2,1,10]
Output: 0
Explanation:
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.


Key Concept: Triangle Inequality

To form a valid triangle with sides a, b, c:

a + b > c
b + c > a
c + a > b


The sum of any two sides must be strictly greater than the third side.
"""

def perimeter(nums):
    nums.sort()
    nums = nums[::-1]
    n = len(nums)
    for i in range(n):
        if (i+2) < n and  nums[i] < nums[i + 1] +  nums[i + 2]:
            print(i,nums[i], nums[i + 1], nums[i + 2])
            perimeter = nums[i] + nums[i + 1] +  nums[i + 2]
            return perimeter

    return 0
nums = [2, 3, 4, 5, 10]
# Sorted: [10,5,4,3,2]
# Triplets:
# 10,5,4 → 10 < 5+4 ❌
# 5,4,3 → 5 < 4+3 ✅
# Output: 12


print(perimeter(nums))