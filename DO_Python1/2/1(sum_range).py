def sum_range(a, b):
    start = min(a, b)
    end = max(a, b)
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum

a = int(input())
b = int(input())
print(sum_range(a, b))