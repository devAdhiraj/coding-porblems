a = input()
if bool(a.count("True")) == bool(a.count("not")%2):
    print(False)
else:
    print(True)