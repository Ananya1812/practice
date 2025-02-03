def is_armstrong(n):
    power = len(str(n))
    armstrong_sum = 0

    while n > 0:
        digit = n % 10
        armstrong_sum += digit ** power
        n //= 10

    if armstrong_sum == n:
        print("Armstrong")
    else:
        print("Not Armstrong")

n = int(input())
is_armstrong(n)
