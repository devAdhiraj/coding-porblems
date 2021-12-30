import sys

input = sys.stdin.readline
r, c = [int(s) for s in input().split()] 
a = [[0]*c for i in range(r)]

for i in range(int(input())):
    x, y = input().split()
    a[int(x) - 1][int(y) - 1] = -1

for i in range(c):
    if a[0][i] != -1:
        a[0][i] = 1
    else:
        break
    
for i in range(r):
    if a[i][0] != -1:
        a[i][0] = 1
    else:
        break

for i in range(1, r):
    for j in range(1, c):
        if a[i][j] != -1:
            if a[i][j - 1] != -1:
                a[i][j] += a[i][j - 1]
            if a[i - 1][j] != -1:
                a[i][j] += a[i - 1][j]

print(a[r - 1][c - 1])