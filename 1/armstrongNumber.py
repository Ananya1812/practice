def armstrong(n):
    original = n 
    power = len(str(n))
    sum = 0
    while n > 0:
        digit = n%10
        sum+= digit**power
        n //= 10
        
    if sum == original:
        print("Armstrong")
    else:
        print("Not Armstrong")
        
n = int(input())
armstrong(n)