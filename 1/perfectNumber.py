# https://leetcode.com/problems/perfect-number/description/
def is_perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n: 
        return "Perfect"
    else:
        return "Not Perfect"

n = int(input())
print(is_perfect_number(n))
