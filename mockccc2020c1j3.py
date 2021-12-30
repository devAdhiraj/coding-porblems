a = int(input())
b = int(input())
m = a*b
d = m % 4

if d == 0:
    print(str(m//4) + ".00")
elif d == 1:
    print(str(m//4) + ".25")
elif d == 2:
    print(str(m//4) + ".50")
else:
    print(str(m//4) + ".75")