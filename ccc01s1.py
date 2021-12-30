total = [0, 0, 0, 0]
a = ["D", "H", "S", input()[1:]]
for i in range(3):
    a += a.pop(-1).split(a[0])
    a.pop(0)

for i in range(4):
    if a[i]:
        total[i] += a[i].count("A")*4 + a[i].count("K")*3 \
        + a[i].count("Q")*2 + a[i].count("J")
    total[i] += (3 - len(a[i])) * (int(len(a[i]) < 4))


print("Cards Dealt" + " "*34 + " Points")

print("Clubs", end='')
for x in a[0]:
    print(" " + x, end="")
print(" "*(47 - len(a[0])*2 - len(str(total[0]))) \
 + str(total[0]))

print("Diamonds", end='')
for x in a[1]:
    print(" " + x, end="")
print(" "*(44 - len(a[1])*2 - len(str(total[1]))) \
 + str(total[1]))

print("Hearts", end='')
for x in a[2]:
    print(" " + x, end="")
print(" "*(46 - len(a[2])*2 - len(str(total[2]))) \
 + str(total[2]))

print("Spades", end='')
for x in a[3]:
    print(" " + x, end="")
print(" "*(46 - len(a[3])*2 - len(str(total[3]))) \
 + str(total[3]))

temp = sum(total)

print(" "*(45 - len(str(temp))) + " Total " + str(temp))