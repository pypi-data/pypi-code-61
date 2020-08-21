def logo(a):
    for x in range(len(a)):
        if a[x] == "0":
            print("\033[40m ", end="")
        elif a[x] == "1":
            print("\033[41m ", end="")
        elif a[x] == "2":
            print("\033[42m ", end="")
        elif a[x] == "3":
            print("\033[43m ", end="")
        elif a[x] == "4":
            print("\033[44m ", end="")
        elif a[x] == "5":
            print("\033[45m ", end="")
        elif a[x] == "6":
            print("\033[46m ", end="")
        elif a[x] == "7":
            print("\033[47m ", end="")
        elif a[x] == "8":
            print("\033[48m ", end="")
        elif a[x] == "9":
            print("\033[49m ", end="")
        elif a[x] == "q":
            print("\033[31m ", end="")
        elif a[x] == "w":
            print("\033[32m ", end="")
        elif a[x] == "e":
            print("\033[33m ", end="")
        elif a[x] == "r":
            print("\033[34m ", end="")
        elif a[x] == "t":
            print("\033[35m ", end="")
        elif a[x] == "y":
            print("\033[36m ", end="")
        elif a[x] == "u":
            print("\033[37m ", end="")
        else:
            print(a[x], end="")
    print("\033[0m")
