# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
from typing import List




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                ans = nums[i] + nums[j]
                if ans == target and i != j:
                    return [i, j]
                else:
                    continue

print(Solution().twoSum(nums=[2,3,4,5], target=9))