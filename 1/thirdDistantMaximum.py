# https://leetcode.com/problems/third-maximum-number/description/
def third_max(nums):
    max1 = max2 = max3 = float('-inf')
    unique_nums = []
    for i in nums:
        if i not in unique_nums:
            unique_nums.append(i)
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = i 
            elif i > max3:
                max3 = i 
                
    if max3 == float('-inf'):
        return max1
    return max3
    
n = int(input())
numbers = list(map(int, input().split()))
print(third_max(numbers))

    




