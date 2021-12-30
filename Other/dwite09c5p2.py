for x in range(5):
  a = int(input())
  def prime(a, d):
    n = d
    i = 2
    while i < 12:
      if (a + n) % i == 0:
        n += d
        i = 1
      if i > abs((a + n - 1) / 2):
        break
      i += 1
    if a + n == 1:
      n += 1
    return a + n

  s = prime(prime(a, 1), 1)
  c = prime(prime(a, -1), -1)
  if abs(a - s) <= abs(a - c):
    print(s)
  else:
    print(c)