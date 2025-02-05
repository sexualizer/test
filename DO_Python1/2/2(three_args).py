def three_args(var1 = None, var2 = None, var3 = None):
    args = []

    if var1 is not None:
        args.append(f"var1 = {var1}")
    if var2 is not None:
        args.append(f"var2 = {var2}")
    if var3 is not None:
        args.append(f"var3 = {var3}")

    if args:
        print("Переданы аргументы: " + ", ".join(args))
    else:
        print("Не переданы аргументы.")

# Примеры вызова функции
three_args(var1 = 2, var3 = 10)
three_args(var2 = 5)
three_args(var1 = None, var2 = None, var3 = None)