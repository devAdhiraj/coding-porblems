import sys
input = sys.stdin.readline
a = input().split()
b = input().split()
c = int(input())
dist = abs(int(b[0]) - int(a[0]))
dist += abs(int(b[1]) - int(a[1]))

if dist > c or c % 2 != dist % 2:
    print("N")

else:
    print("Y")