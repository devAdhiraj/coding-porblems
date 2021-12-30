key = input()
s = input()
n = 0
c = len(key)
for i in range(len(s)):
    if s[i].isalpha():
        temp = ord(key[n%c]) - 65 + ord(s[i]) - 65
        if temp > 25:
            temp -= 26
        print(chr(temp+65), end='')
        n += 1