a = str(int(input()) + 1)
i = 0
while i < len(a):
    if a.count(a[i]) > 1:
        a = str(int(a) + 1)
        i = -1
    i += 1
print(a)