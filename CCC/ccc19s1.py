a,b,c,d = 1,2,3,4
f= input()
if(f.count("V")%2 != 0):
  a, b, c, d = b, a, d, c

if(f.count("H")%2 != 0):
  a, b, c, d = c, d, a, b

print(a,b)
print(c,d)