def infinite(lst, tries):
    res = ""
    if len(lst) > tries:
        for i in range(0, tries):
           res += str(lst[i]) + " "
    else:
        while(tries > len(lst)):
            for j in range(0, len(lst)):
                res += str(lst[j]) + " "
            tries = tries - len(lst)
        for i in range(0, tries):
           res += str(lst[i]) + " "
    return res.lstrip()


print(infinite([1, 2, 3, 4, 5], 8))