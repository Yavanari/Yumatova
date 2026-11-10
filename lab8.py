import math
def is_prime(n):
    if n == 0 or n == 1 or n < 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(1))
print(is_prime(12))
print(is_prime(20))