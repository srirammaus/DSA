
# Constraints:
#
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].


# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
def romanToint(num: str )->int:
    integer = 0
    track = None
    for i in range(len(num)):
        # print(num[i])
        # print(integer)
        if(track != None):
            track = None
            continue
        match(num[i]):
            case "I":
                if(i + 1 < len(num)):
                    next = num[i + 1]
                    if(next == "V" or next == "X"):
                        integer +=(romanToint(next)-1)
                        track = 1
                    else:
                        integer += 1
                else:
                    integer+= 1
            case "V":
                integer+= 5
            case "X":
                if(i + 1 < len(num)):
                    next = num[i + 1]
                    if(next == "L" or next == "C"):
                        integer += romanToint(next)-10
                        track = 10
                    else:
                        integer += 10
                else:
                    integer+= 10
            case "L":
                integer+= 50
            case "C":
                if (i + 1 < len(num)):
                    next = num[i + 1]
                    if (next == "D" or next == "M"):
                        integer += romanToint(next) - 100
                        track = 1
                    else:
                        integer += 100
                else:
                    integer += 100
            case "D":
                integer+= 500
            case "M":
                integer+= 1000
            case _: # defalt
                 integer+= 0
    return integer


print(romanToint('MCMXCIV'))

