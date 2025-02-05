def primes(n):
    res = list()
    for i in range(2, n):
        dels = list()
        for j in range(1, i + 1):
            if (i % j == 0):
                dels.append(j)
        if len(dels) == 2:
            res.append(i)
    return res

print("Enter a number:")
n = int(input())
print(primes(n))