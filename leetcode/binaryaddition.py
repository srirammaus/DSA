
"""Easy
Topics
premium lock icon
Companies
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

rule =  0+0 = 0
        0+1 = 1
        1+0 = 1
        1+1 = 0 with carry 1
 """
def binaryAddition(num1, num2):
    # coloumn by column , right to left

    if(len(num1) < len(num2)):
        num2,num1 = num1,num2

    n_1 = len(num1)
    n_2 = len(num2)

    # print(num1,num2)
    i=0
    j= 0
    result = ""
    carry = "0"
    while i < n_1 or j < n_2 :
        i+=1
        j+=1
        if((n_1-i) == 0 or n_1-i > 0  ):
            add1 = num1[n_1 - i]
            # print(num1[n_1-i],n_1-i)
        else:
            add1 = "0"
        if((n_2-j) == 0 or n_2-j > 0 ):
            add2 = num2[n_2 - j]
            # print(num2[n_2-j]+ " : " + str(n_2-j) + " This")
        else:
            # print("This will add a zero")
            add2 = "0"

        match(add1, add2):
            case "1","1":
                if carry == "1":
                    res = "1"
                else:
                    # print("This happened first")
                    res = "0"
                carry = "1"
                # print("This will carry one")
                result = res +result
            case "0","0":
                if carry == "1":
                    res = "1"
                else:
                    res = "0"
                carry = "0"
                result = res +result
            case "1","0":
                if carry == "1":
                    res = "0"
                    carry = "1"
                    # print("you will end up here with carry 1 ")
                else:
                    res = "1"
                    carry = "0"
                result = res +result
            case "0","1":
                if carry == "1":
                    res = "0"
                    carry = "1"
                else:
                    res = "1"
                    carry = "0"
                result = res +result
        if(carry == "1" and (n_1)-i == 0):
            # print("This will never happening")
            result = carry + result

    return result



print(binaryAddition("1101101", "1011"))

# def binaryAddition(num1, num2):
#     # coloumn by column , right to left
#
#     if(len(num1) < len(num2)):
#         num2,num1 = num1,num2
#
#     n_1 = len(num1)
#     n_2 = len(num2)
#
#     # print(num1,num2)
#     i=0
#     j= 0
#     result = []
#     carry = "0"
#     while i < n_1 or j < n_2 :
#         i+=1
#         j+=1
#         if((n_1-i) == 0 or n_1-i > 0  ):
#             add1 = num1[n_1 - i]
#             print(num1[n_1-i],n_1-i)
#         else:
#             add1 = "0"
#         if((n_2-j) == 0 or n_2-j > 0 ):
#             add2 = num2[n_2 - j]
#             print(num2[n_2-j]+ " : " + str(n_2-j) + " This")
#         else:
#             print("This will add a zero")
#             add2 = "0"
#
#         match(add1, add2):
#             case "1","1":
#                 if carry == "1":
#                     res = "1"
#                 else:
#                     print("This happened first")
#                     res = "0"
#                 carry = "1"
#                 print("This will carry one")
#                 result.insert(0,res)
#             case "0","0":
#                 if carry == "1":
#                     res = "1"
#                 else:
#                     res = "0"
#                 carry = "0"
#                 result.insert(0,res)
#             case "1","0":
#                 if carry == "1":
#                     res = "0"
#                     carry = "1"
#                     print("you will end up here with carry 1 ")
#                 else:
#                     res = "1"
#                     carry = "0"
#                 result.insert(0,res)
#             case "0","1":
#                 if carry == "1":
#                     res = "0"
#                     carry = "1"
#                 else:
#                     res = "1"
#                     carry = "0"
#                 result.insert(0,res)
#         if(carry == "1" and (n_1)-i == 0):
#             print("This will never happening")
#             result.insert(0,carry)
#
#     return result



