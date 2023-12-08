# -*- coding: utf-8 -*- 

def so(nums):
    n = len(nums)
    for i in range(n // 2):
        nums[i],nums[n-1-i] = nums[n-1-i], nums[i]
    
    return nums

nums = [1,2,3,4,5,6]
print (so(nums))
