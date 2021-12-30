for i in range(int(input())):
    a, b = input().split()
    a, b = int(a), int(b)
    x = []
    def n(a):
        def p(a):
            c = 1
            for i in range(2, int(a**0.5) + 2, c):
                if a % i == 0:
                    a = p(a + 1)
                    break
                c = 2
            return a

        if a == 1 or a == 2:
            return 2
        else:
            return p(a)
    c = 0
    while a < b:
        c = n(a)
        if c < b:
            x.append(c)
        else:
            break
        a = c + 1

    print(len(x))