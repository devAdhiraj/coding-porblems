a = int(input())
c = []
for i in range(a):
    b = []
    for x in range(4):
        c = input().split()[-1][::-1].lower()
        for n in c:
            if n == "a" or n == "e" or n == "i" or n == "o" or n == "u":
                b.append(c[:c.index(n) + 1])
                break
        if len(b) < x + 1:
            c = c[::-1]
            b.append(c)
    if b[0] == b[1] == b[2] == b[3]:
        print("perfect")
    elif b[0] == b[1] and b[2] == b[3]:
        print("even")
    elif b[0] == b[2] and b[1] == b[3]:
        print("cross")
    elif b[0] == b[3] and b[2] == b[1]:
        print("shell")
    else:
        print("free")