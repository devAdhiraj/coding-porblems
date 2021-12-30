for j in range(int(input())):
    n = 0
    a = input()
    for i in range(len(a)):
        if a[i].isalpha():
            o = ord(a[i]) - 64
            if o < 19:
                print(((o - 1) // 3) + 2, end='')
            elif o < 23:
                print(o // 4 + 3, end='')
            else:
                print(9, end='')
            n += 1
        
        elif a[i].isdigit():
            print(a[i], end='')
            n += 1
        if n in [3, 7]:
            print("-", end='')
            n += 1
        
        if n == 12:
            break
    print()