import itertools

n = int(input())
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, len(l), n):
    print(list(itertools.islice(l, i, i + n)))


