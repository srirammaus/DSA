

def longestpalindromesubstr(s):
    i=0
    n=len(s)
    palindrome_len = 0
    palindrome_str = ""
    for i in range(n):
        for j in range(i+1,n+1):
            # print(i,j)
            p1 = s[i:j]
            p2 = p1[::-1]
            # print(p1,p2)
            if p1 == p2:
                if (palindrome_len < len(p1)):
                    # print(i,j)
                    # print(p1,p2)
                    # print(palindrome_len)
                    palindrome_str = p1
                    palindrome_len = len(p1)

        # print("---")
    return palindrome_str


n="forgeeksskeegfor"
print(longestpalindromesubstr(n))
# if p1 == p2:
#     if (palindrome_len < len(p1)):
#         palindrome_str = p1


# isPalindrome = stack[:idx + 1]
# p1 = "".join(isPalindrome)
# p2 = "".join(isPalindrome[::-1])
# current_pal_len = len(p1)
# if (current_pal_len > palindrome_len):
#     if (p1 == p2):
#         palindrome_str = p1
# palindrome_len = max(palindrome_len, current_pal_len)
#
# n= [1,2,3,4,5,6]
# k = n[:1]
# print(n)
# print(k)

# n = ["a","b","c"]
# n= "".join(reversed(n))
# print(n)
