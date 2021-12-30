c = int(input())
a = list(map(int, input().split()))
for n in range(10):
  b = []
  for i in range(c):
    if a[i] % 10 == n:
      b.append(a[i])
  b.sort(reverse = True)
  for x in range(len(b)):
    print(b[x], end=' ')