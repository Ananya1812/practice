def kth_prime(k):
    num, count = 2, 0
    while count < k:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            count += 1
        num += 1
    return num - 1

k = int(input())
print(kth_prime(k))
