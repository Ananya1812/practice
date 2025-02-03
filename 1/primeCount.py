# https://leetcode.com/problems/count-primes/description/
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(arr):
    count = 0
    for i in arr:
        if is_prime(i):
            count += 1
    return count

arr = list(map(int, input().split()))
print(count_primes(arr))

