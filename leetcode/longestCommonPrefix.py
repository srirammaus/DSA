

def mutualPrefix( strs: list[str])->str:
    longstr = max(strs, key=len)
    idx = strs.index(longstr)
    result_found = False
    mutualWord =""

    for i in range(len(longstr)):
        for j in range(len(strs)):
            # if j == idx:
            #     continue
            if len(strs[j]) > i:
                if longstr[i] == strs[j][i]:
                    print(strs[j] + "  True  "+ str(i) + "   "+ longstr[i]+ "    " + strs[j][i])
                    result_found = True
                else:
                    print(strs[j] + "  Flase  "+ str(i) + "   "+ longstr[i]+ "    " + strs[j][i])
                    result_found = False
                    break
            else:
                result_found = False
                break
        if result_found == True:
            mutualWord += longstr[i]
        else:
            break
    return mutualWord
print(mutualPrefix(["flower","flow","foght"]))

