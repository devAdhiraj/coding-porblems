c = []
s = int(input())
a = input()
n = 999999
for i in a:
    if i == "1":
        n = 0
    else:
        n += 1
    c.append(n)

for i in range(s - 1, -1, -1):
    if a[i] == "1":
        n = 0
    
    else:
        n += 1
        if c[i] > n:
            c[i] = n

print(sum(c))