n = [int(x) for x in input().split()]
res = ""

if len(n) == 1:
    print(n[0])
    quit()
for i in range(0, len(n)):
    if i == 0:
        res += str(int(n[i + 1]) + int(n[len(n) - 1])) + ' '
    elif i == len(n) - 1:
        res += str(int(n[i - 1]) + int(n[0])) + ' '
    else:
        res += str(int(n[i - 1]) + int(n[i + 1])) + ' '
print(res)