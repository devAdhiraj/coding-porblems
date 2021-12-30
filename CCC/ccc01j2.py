a = int(input())
b = int(input())
for i in range(2,b):
    if (a*i) % b == 1:
        print(i)
        break
else:
    print("No such integer exists.")