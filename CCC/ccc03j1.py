t = int(input())
s = int(input())
h = int(input())

for i in range(t):
    sp = " "*s
    print("*" + sp + "*" + sp + "*")

print("*"*(2*s + 3))

for i in range(h):
    print(" "*s, "*")