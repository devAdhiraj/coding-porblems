import sys
input = sys.stdin.readline
t = int(input())
c = 0
a = [int(input()) for i in range(int(input()))]
for i in sorted(a):
    if t - i >= 0:
        t -= i
        c += 1
    else:
        break
print(c)