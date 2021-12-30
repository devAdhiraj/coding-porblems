import sys
input = sys.stdin.readline

ans = 0
n = int(input())
s1 = [0] + input().split()
s2 = [0] + input().split()

for i in range(1, n + 1):
    s1[i] = int(s1[i - 1]) + int(s1[i])
    s2[i] = int(s2[i - 1]) + int(s2[i])
    if s1[i] == s2[i]:
        ans = i
print(ans)