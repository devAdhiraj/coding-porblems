r = []
for i in range(int(input())):
    r.append(int(input()))

x = 0
while x != 77:
    x = int(input())
    if x == 99:
        index = int(input()) - 1
        percent = int(input()) / 100
        left_river = r[index]*percent
        right_river = r[index] - left_river
        r = r[:index] + [left_river] + [right_river] + r[index + 1:]
    if x == 88:
        index = int(input()) - 1
        r = r[:index] + [r[index] + r[index + 1]] + r[index + 2:]

for i in r:
    print(round(i), end=' ')