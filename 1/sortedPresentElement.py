# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
def search(num,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i 
    return -1
    
a,target=map(int,input().split())
nums = list(map(int, input().split()))
print(search(nums,target))
