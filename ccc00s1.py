c = int(input())
m1, m2, m3 = int(input()), int(input()), int(input())
n = 0
while c > 0:
    c -= 1
    m1 += 1
    n += 1
    if m1 == 35:
        m1 = 0
        c += 30
    if c == 0:
        break
    c -= 1
    m2 += 1
    n += 1
    if m2 == 100:
        m2 = 0
        c += 60
    if c == 0:
        break
    c -= 1
    m3 += 1
    n += 1
    if m3 == 10:
        m3 = 0
        c += 9
print("Martha plays", n, " times before going broke.")