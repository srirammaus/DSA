

# str((n-1)-i)
def lastwordlen(s:str):
    n= len(s)
    # trace = 0
    count = 0
    for i in range(n-1,-1,-1):
        if s[i] == " " and count != 0: #trace == 0
            # print("I will break" + str(count))
            break
        else:
            if s[i] != " ":
                count += 1
                # trace = 1
            # print(s[i])
            pass
    return count


print(lastwordlen("luffy is still joyboy"))
print("----")

# def lastwordlen(s:str):
#     n= len(s)
#     trace = 0
#     count = 0
#     for i in range(n-1,-1,-1):
#         if s[i] == " " and trace == 1:
#             print("I will break" + str(count))
#             break
#         else:
#             if s[i] != " ":
#                 count += 1
#                 trace = 1
#
#             print(s[i])
#             pass