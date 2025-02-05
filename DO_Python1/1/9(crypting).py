to = {"0": "@", "1": "!", "2": "#", "3": "$", "4": "%",
    "5": "^", "6": "&", "7": "*", "8": "(", "9": ")"
}

out = {"@": "0", "!": "1", "#": "2", "$": "3", "%": "4",
    "^": "5", "&": "6", "*": "7", "(": "8", ")": "9"}

def encrypting(line):
    res = ""
    code = ""
    for char in line:
        code += out[char]
        if (len(code) < 2) or (int(code) < 32):
            continue
        else:
            res += chr(int(code))
            code = ""
    return res


def crypting(line):
    res = ""
    num = 0
    for char in line:
        num = ord(char)
        for n in str(num):
            res += to[n]
    return res


print("Do you want to crypt - 1, or encrypt - 2?")
choice = int(input())
if (choice == 1):
    print("Enter a line to crypt:")
    line = input()
    print(crypting(line))
elif (choice == 2):
    print("Enter a line to encrypt:")
    line = input()
    print(encrypting(line))
