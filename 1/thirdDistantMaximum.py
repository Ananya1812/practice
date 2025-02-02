# https://leetcode.com/problems/third-maximum-number/description/
def third_max(nums):
    nums = sorted(set(nums), reverse=True)  
    return nums[2] if len(nums) >= 3 else nums[0]  

n = int(input()) 
nums = list(map(int, input().split()))  

print(third_max(nums))


#second solution
def thirdMax(nums):
    first_max = second_max = third_max = float('-inf')  
    seen = set() 
    
    for num in nums:
        if num not in seen: 
            seen.add(num) 
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num > second_max:
                third_max = second_max
                second_max = num
            elif num > third_max:
                third_max = num

    if third_max == float('-inf'):
        return first_max
    return third_max

nums = list(map(int, input().split()))
print(thirdMax(nums))


