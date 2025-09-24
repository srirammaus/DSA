# negative number cannot be palidrome
#  if you want get the asnwer even if it is negeative then the divison //(This place also be negative)

def isPalindrome(x: int)->bool:
    y = x
    i = 1

    # the appender
    appender = 0
    while x > 0:
        x = x // 10
        z = (y // i ) % 10
        i = i * 10

        appender = appender * 10 + z
    if(appender == y):
        return True
    return False

print(isPalindrome(-12321))

# another method
# by doing only any half reversed and mathhc it
def palindrome(num: int)->bool:
    return True

