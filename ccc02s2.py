a, b = int(input()), int(input())
if a / b == a//b:
    print(a//b)
else:
    c = a//b
    a -= c*b
    for i in range(a, 1, -1):
        if a%i == 0 == b%i:
            a //= i
            b //= i
            break
    if c:
        print(c, str(a) + "/" + str(b))
    else:
        print(str(a) + "/" + str(b))