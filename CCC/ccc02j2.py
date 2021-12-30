c = ["a", "e", "i", "o", "u", "y"]
a = input()
while a != "quit!":
    if len(a) > 3 and a[-2:] == "or" and a[-3] not in c:
        print(a[:-2] + "our")
    else:
        print(a)
    a = input()