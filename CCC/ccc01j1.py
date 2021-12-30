n = int(input())
s = " "*n*2
for i in range(1, n+1, 2):
    print("*"*i + s[i:-i] + "*"*i)
for i in range(n-2, 0, -2):
    print("*"*i + s[i:-i] + "*"*i)