a = int(input())
b = int(input())
op = input()
res = 0

if op == '+':
    res = a + b
elif op == '-':
    res = a - b
elif op == '/':
    if b == 0:
        print("You cannot divide by zero")
    else:
        res = a / b
elif op == '*':
    res = a * b
elif op == "mod":
    res = a % b
elif op == "pow":
    res = a ** b
elif op == "div":
    res = a // b
else:
    print("No such operation")
    quit()
print(res)
