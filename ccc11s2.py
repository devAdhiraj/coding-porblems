import sys
input = sys.stdin.readline
s = 0
n = int(input())
ans = [input() for i in range(n)]
for i in ans:
    if i == input():
        s += 1
print(s)