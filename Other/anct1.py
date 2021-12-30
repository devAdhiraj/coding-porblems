b = input().split()
a = list(map(int, input().split()))
a.sort()
x = -1
while abs(x) < int(b[0]) and int(b[1]) % a[x] != 0:
  x -= 1

if int(b[1]) % a[x]:
  print("This is not the best time for a trip.")
else:
  print(abs(int(b[1]) // a[x]))