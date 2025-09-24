"""Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


Constraints:

0 <= x <= 231 - 1

what thy are asking to implementing your iwn sqrt, but any how they need decimal
values so we directly jump in second step without finding any prime factors for sqrt. for sqrt like root 2 or 6 root 2
for this prime fatcors finding needed , but anyhow we decimal values only so multiple by all possible guesses

"""
import math

def sqrt(num):
    x=  (num // 2) +1
    for i in range(x+1): #why +1 ? because  if the 1 given as input then range(1) so the loop run only once with i=0 . but he i=1 situation not occurs we need that situation to get answer so we adding +1
        res = i*i
        if num == res:
            return i
        elif num < res:
            return i-1
        else:
            pass

print(sqrt(1))