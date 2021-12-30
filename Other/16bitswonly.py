a = int(input())
s = ""
for i in range(a):
  b = []
  b = input().split()
  if int(b[0]) * int(b[1]) - int(b[2]):
    s += "16 BIT S/W ONLY\n"
  else:
    s += "POSSIBLE DOUBLE SIGMA\n"
print(s)