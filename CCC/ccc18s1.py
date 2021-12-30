a = []
t = int(input())
k = []
for i in  range(t):
  a.append(int(input()))
a.sort()
size = len(a) - 1
for n in range(1,size):
  k.append(0.5*(a[n + 1] - a[n]) + 0.5*(a[n] - a[n - 1]))
print(min(k))