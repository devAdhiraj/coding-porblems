import sys
input = sys.stdin.readline
n = int(input())
a = sorted(map(int, input().split()))
c = None
if n % 2:
    c = a.pop(0)
n //= 2
for i in range(n, n*2):
    print(a[-i- 1], a[i], end=' ')

if c:
    print(c)