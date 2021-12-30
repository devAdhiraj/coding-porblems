a = int(input())

def p(a):
    c = 1
    for i in range(2, int(a**0.5) + 2, c):
        if a % i == 0:
            a = p(a + 1)
            break
        c = 2
    return a
    
if a == 1 or a == 2:
    print(2)
else:
    print(p(a))