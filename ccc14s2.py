def fn():
    x = []
    if a % 2 == 1:
        return "bad"
    for i in range(len(b)):
        if b[i] == c[i]:
            return "bad"
        if b[i] < c[i]:
            x.append(b[i] + c[i])
        else:
            x.append(c[i] + b[i])
    for i in x:
        if x.count(i) != 2:
            return "bad"
    return "good"
a = int(input())
b = input().split()
c = input().split()
print(fn())