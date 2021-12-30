a = []
sq = int(input())
r = int(input())
c = int(input())
a.append(input())
rooms = [0]*(r+c)
rn = 0
for x in range(len(a[0])):
    if a[0][x] == ".":
        rooms[rn] += 1
        a[0] = a[0][:x] + chr(rn+97) + a[0][x + 1:]       
    elif a[0][x] == "I" and rooms[rn]:
        rn += 1
            
for i in range(1, r):
    a.append(input())
    for j in range(c):

        if j and a[-1][j-1] != "I" and a[-1][j] != "I":
            a[-1] = a[-1][:j] + a[-1][j-1] + a[-1][j + 1:]
            rooms[ord(a[-1][j - 1]) - 97] += 1
            
        if a[-1][j] != "I":
            if a[-1][j] == ".":
                if "I" != a[-2][j]:
                    rn = ord(a[-2][j]) - 97
                    rooms[rn] += 1
                    a[-1] = a[-1][:j] + chr(rn+97) + a[-1][j + 1:]
                else:
                    rn = rooms.index(0)
                    rooms[rn] += 1
                    a[-1] = a[-1][:j] + chr(rn+97) + a[-1][j + 1:]

            elif a[-2][j] != "I":
                rn_top = a[-2][j]
                rn_left = a[-1][j]
                if ord(rn_top) < ord(rn_left):
                    a[-1] = a[-1][:j+1].replace(rn_left, rn_top) + a[-1][j + 1:]
                    for i in range(len(a)):
                        a[i] = a[i].replace(rn_left, rn_top)
                    rooms[ord(rn_top)-97] += rooms[ord(rn_left)-97]
                    rooms[ord(rn_left)-97] = -1
                elif ord(rn_top) > ord(rn_left):
                    for i in range(len(a)):
                        a[i] = a[i].replace(rn_top, rn_left)
                    rooms[ord(rn_left) - 97] += rooms[ord(rn_top) - 97]
                    rooms[ord(rn_top) - 97] = -1
rm = 0
for i in sorted(rooms, reverse=True):
    if i > 0:
        if sq - i < 0:
            break
        else:
            sq -= i
            rm += 1


if rm == 1:
    print("1 room, {0} square metre(s) left over".format(sq))

else:
    print("{0} rooms, {1} square metre(s) left over".format(rm,sq))