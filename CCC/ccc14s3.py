import sys
input = sys.stdin.readline
for i in range(int(input())):
    m = []
    b = []
    n = 1
    for i in range(int(input())):
        m.append(int(input()))

    while m or (b and b[-1] == n):
        if b and b[-1] == n:
            b.pop()
            n += 1
        elif m:
                
            elem = m.pop()
            if elem != n:
                b.append(elem)
            else:
                n += 1
        
    if b:
        print("N")
    else:
        print("Y")