for i in range (5):
  a = int(input())
  c = a
  x = 0
  while a // 2 != 0:
    a //= 2
    x += 1
  if c - 2**x < abs(c - 2**(x + 1)):
    print(2**x)
  else:
    print(2**(x + 1))