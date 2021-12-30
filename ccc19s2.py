def is_prime(num):
    for x in range(3, int(num**0.5) + 1, 2):
        if num % x == 0:
            return False
    return True

for i in range(int(input())):
    a = int(input())
    for j in range(2*a - 3, 1, -2):
        if j%2:
            if is_prime(j) and is_prime(2*a - j):
                print(j, 2*a - j)
                break