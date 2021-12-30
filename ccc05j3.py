a = []
for i in range(10):
    a.append(input())
    if a[-1] == "SCHOOL": 
        break
b = ["LEFT" if i == "R" else "RIGHT" for i in a[::2]][::-1]
x = -3
for i in range(len(b) - 1):
    print("Turn", b[i], "onto", a[x], "street.")
    x -= 2
print("Turn", b[-1], "into your HOME.")