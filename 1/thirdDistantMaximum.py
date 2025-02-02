# https://leetcode.com/problems/third-maximum-number/description/
def third_max(nums):
    max1 = max2 = max3 = float('-inf')
    unique_nums = []  

    for num in nums:
        if num not in unique_nums:  
            unique_nums.append(num)
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

    if max3 == float('-inf'):
        return max1
    return max3

numbers = list(map(int, input().split()))
print(third_max(numbers))



