import sys
input = sys.stdin.readline
j = int(input())
p = int(input())
s = []
m = []
l = []
sReq = []
mReq = []
lReq = []
for i in range(j):
    temp = input()
    if temp == 'L\n':
        l.append(i + 1)
    elif temp == 'M\n':
        m.append(i + 1)
    else:
        s.append(i + 1)

for i in range(p):
    size, num = input().split()
    num = int(num)
    if size == 'L':
        lReq.append(num)
    elif size == 'M':
        mReq.append(num)
    else:
        sReq.append(num)


def myfunc(jerseys, req):
    leftReq = set(req)
    intersect = []
    leftJersey = []

    for v in jerseys:
        if v in leftReq:
            intersect.append(v)
            leftReq.remove(v)
        else:
            leftJersey.append(v)

    return intersect, leftJersey, list(leftReq)

lJerseys, lrgLeft, discard = myfunc(l, lReq)
mJerseys, medLeft, mReqLeft = myfunc(m, mReq)
sJerseys, disc, sReqLeft = myfunc(s, sReq)

t1, t2, t3 = myfunc(medLeft, sReqLeft)
mJerseys += t1
mReqLeft += t3

t1, t2, t3 = myfunc(lrgLeft, mReqLeft)

lJerseys += t1

print(len(lJerseys + mJerseys + sJerseys))