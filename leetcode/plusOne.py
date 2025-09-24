"""
66. Plus One
Easy
Topics
premium lock icon
Companies
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].



"""
#This is simple if we fetch out everthing and then add then spread them in array , but time consuming
# so we use carry method

def plusOne(digits):
    i=0
    n=len(digits)

    carry=0
    newDigits=[]
    while i<n:
        i+=1
        if carry==0 and i == 1:
            current = digits[n - i] + 1 +carry
        else:
            current = digits[n - i] + carry
        if current > 9:
            carry = 1
            current = 10-current
        else:
            carry = 0
        newDigits.insert(0,current)
        if (carry == 1 and (n - i) == 0):
            newDigits.insert(0, carry)
            carry = 0

    return newDigits
print(plusOne([8,9,9,9]))