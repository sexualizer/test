n = int(input())
spaces = n * 2 - 1

for i in range(1, n + 1):
    line = " " * int(((spaces - 1) // 2)) + (str(i) * (2 * i - 1)) + " " * int(((spaces - 1) // 2))
    print(line)
    spaces -= 2

"""
    1
   222
  33333
 4444444
555555555
"""