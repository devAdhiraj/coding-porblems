import sys
input = sys.stdin.readline

q = int(input())
size = int(input())
arr1 = list(map(int, input().split()))

arr2 = list(map(int, input().split()))

if q == 1:
    v = 0
    arr1.sort()
    arr2.sort()
    for i in range(size):
        v += max(arr1[i], arr2[i])
    print(v)
else:
    print(sum(sorted(arr1 + arr2, reverse=True)[0:size]))