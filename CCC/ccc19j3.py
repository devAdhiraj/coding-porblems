a = int(input())
for i in range (a):
  symbols = input()
  count = 1
  count1 = 1
  while(count1 <= len(symbols)):
    count = 1  
    while(count1 <= len(symbols) - 1 and symbols[count1] == symbols[count1 - 1] ):
      count += 1
      count1 += 1
    count1 += 1
    print(str(count), symbols[count1 - 2] + " ", end='')
  print()