a = [[]]
start = int(input())
end = int(input())
n = 1
a[0].append(start)
count = start
i = 0
while True:
    a.append([])
    # adds to down
    if count == end and i == n:
        print("w")
        for i in range(1, n + 1):
            a[i].insert(0, " ")
        break

    if count == end:
        break

    for i in range(1, n + 1):
        if count != end:
            count += 1
            a[i].insert(0, count)
    
        else:
            a[i].insert(0, " ")
        
    if count == end:
        break 

    # adds to right
    for i in range(1, n):
        count += 1
        a[-1].append(count)
        if count == end:
            break
    
    if count == end:
        break
    
    n += 1
    a.insert(0, [])
    # adds to top
    for i in range(n, -1, -1):
        count += 1
        a[i].append(count)
        if count == end:
            break

    if count == end:
        break

    # adds to left
    for i in range(n):
        if count != end:    
            count += 1
            a[0].insert(0, count)
        elif i == n - 1:
            break
        else:
            a[0].insert(0, " ")
    n += 1
    


for x in a:
    for j in x:
        print("{:4s}".format(str(j)), end='')
    print()