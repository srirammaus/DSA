#
# Input: s = "()"
#
# Output: true
#
# Example 2:
#
# Input: s = "()[]{}"
#
# Output: true
#
# Example 3:
#
# Input: s = "(]"
#
# Output: false
#
# Example 4:
#
# Input: s = "([])"
#
# Output: true
#
# Example 5:
#
# Input: s = "([)]"
#
# Output: false
def isValidParentheses(arg: str ) -> bool:

    stack = []
    pairs = []
    #()() (())
    for idx,char in enumerate(arg):
        match(arg[idx]):
            case "(":
                stack.append(idx)
            case ")":
                if(len(stack))  > 0:
                    opener = stack.pop()
                    pairs.append((opener, idx))
                else:
                    return False
            case "[":
                stack.append(idx)
            case "]":
                if(len(stack))  > 0:
                    opener = stack.pop()
                    pairs.append((opener, idx))
                else:
                    return False
            case "{":
                stack.append(idx)
            case "}":
                if(len(stack))  > 0:
                    opener = stack.pop()
                    pairs.append((opener, idx))
                else:
                    return False

    pair_len = len(pairs)
    argslen = len(arg) / 2
    if argslen !=  pair_len:  #there is no chance , this would be even thatas why im dividing by 2 ,dont put // it will round down
        return False

    return digger(pairs,arg)

def digger(pairs,arg):


    for i in range(len(pairs)):
        # is_empty = (pairs[i][0] + 1) - pairs[i][1]
        # if is_empty != 0:
        parantheses = arg[int(pairs[i][0])] + arg[int(pairs[i][1])]
        match(parantheses):
            case "()" |"[]" | "{}":
                track = True
            case _:

                return False
        # else:
        #     return True
    return track

print(isValidParentheses("({{{{}}}))"))




