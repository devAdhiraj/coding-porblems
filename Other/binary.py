n = int(input())
for i in range(n):
  s = ""
  a = bin(int(input()))[2::]
  a = format(int(a), "0" + str(((len(a) // -4)*-1) * 4))
  for i in range(0, len(a)):
    s += a[i]
    if (i + 1) % 4 == 0: s += " "
  print(s)