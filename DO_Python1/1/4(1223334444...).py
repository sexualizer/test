n = int(input())
count = 0
res = []
for i in range(1, n):
    if len(res) >= n:
        break
    for j in range(0, i):
        res.append(i)
print(res[:n])



