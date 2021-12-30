pos = 1
while True:
    n = int(input())
    if n == 0:
        print("You Quit!")
        break

    elif pos + n <= 100:
        pos += n

    if pos == 99:
        pos = 77
    elif pos == 90:
        pos = 48
    elif pos == 54:
        pos = 19
    elif pos == 9:
        pos = 34
    elif pos == 40:
        pos = 64
    elif pos == 67:
        pos = 86
    print("You are now on square", pos)
    if pos == 100:
        print("You Win!")
        break