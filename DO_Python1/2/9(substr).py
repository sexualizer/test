def get_substr(text):
    while True:
        s = input()
        if (s == "exit"):
            break
        index = text.find(s)
        print(index)

print(get_substr("london is the capital of great britain"))