# https://leetcode.com/problems/closest-prime-numbers-in-range/solutions/
def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return is_prime

def closest_primes(left, right):
    is_prime_list = sieve(right)  
    primes = [num for num in range(left, right + 1) if is_prime_list[num]]

    if len(primes) < 2:
        print("-1 -1")
        return

    min_gap = float('inf')
    num1, num2 = -1, -1

    for i in range(len(primes) - 1):
        gap = primes[i + 1] - primes[i]
        if gap < min_gap:
            min_gap = gap
            num1, num2 = primes[i], primes[i + 1]

    print(num1, num2)

left, right = map(int, input().split())
closest_primes(left, right)

