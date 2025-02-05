number = input()
number = number[::-1]
s = int(input())
dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 16}
res = 0

if (s == 2):
    for i in range(0, len(number)):
        if number[i] == '1':
            res += 2 ** i
elif (s == 8):
    for i in range(0, len(number)):
        res += 8 ** i * int(number[i])
elif (s == 16):
    print(dict)
    for i in range(0, len(number)):
        if number[i] in dict:
            res += 16 ** i * int(dict.get(number[i]))
        else:
            res += 16 ** i * int(number[i])
print(res)