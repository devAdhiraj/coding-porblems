a = []
a.append(int(input()))
a.append(int(input()))
if max(a) > 10:
  x = min(a)
  if min(a) >= 10:
    x = 9
else:
  x = max(a) + min(a) - 9
if(x < 0):
  x = 0
if(x == 1):
  print("There is 1 way to get the sum 10.")
else:
  print("There are " + str(x) + " ways to get the sum 10.")