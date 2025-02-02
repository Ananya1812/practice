# https://leetcode.com/problems/perfect-number/description/
def is_perfect_number(n):
    su = 0
    for i in range(1, n):
        if n % i == 0:
            su += i
    if su == n:
        return "Perfect"
    else:
        return "Not Perfect"

n = int(input())
print(is_perfect_number(n))
