import sys
input = sys.stdin.readline

xmax, ymax = list(map(int, input().split()))


x, y = list(map(int, input().split()))

posx, posy = 0, 0

while(x != 0 or y != 0):
    posx += x
    posy += y
    if posx < 0:
        posx = 0
    if posx > xmax:
        posx = xmax
    if posy < 0:
        posy = 0
    if posy > ymax:
        posy = ymax
    
    print(posx, posy)
    x, y = list(map(int, input().split()))