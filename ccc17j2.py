a = int(input())
final_sum = 0
for i in range(int(input()) + 1):
    final_sum += a*(10**i)
print(final_sum)