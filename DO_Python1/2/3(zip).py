l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [11, 12, 13, 14, 15, 16, 17, 18]

l = zip(l1, l2)
res = []
for pair in list(l):
    res.append(pair[0] + pair[1])
print(res)