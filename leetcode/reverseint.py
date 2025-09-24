

def reverseint(x):
    negative_int= None
    if(x < 0):
        negative_int = True
        x = x * -1
    plus_limit = 2 ** 31 -1
    minus_limit = -2 ** 31
    n=0
    should_reverse=x
    while x >0:
        n+=1
        # print(x)
        x = x // 10

    k=1
    reversed = 0
    for i in range(n):
        reverse = (should_reverse // k ) % 10
        # print(reversed)
        reversed +=  reverse * 10 ** (n-(i+1)) #actauly n-1 that is also only for highest , for finding multiplier for all value im putting (n-(i+1))
        k*=10
    if(negative_int == True):
        reversed = -1 * reversed
    if(reversed > plus_limit or reversed < minus_limit):
        return 0
    return  reversed


x= -1000
print(reverseint(x))