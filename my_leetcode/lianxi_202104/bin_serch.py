# -*- coding: utf-8 -*-
# 二分查找

def bin_ser(numlist, val):
    low = 0  # 左边界
    high = len(numlist) - 1 # 右边界
    while low <= high:
        mid = (low + high) // 2 # 中间数的下标
        if numlist[mid] == val:
            return mid
        elif numlist[mid] > val:
            mid = high-1
        else:
            low = mid + 1
    
    return None

nums = range(3,16)
print (nums)
print (bin_ser(nums, 9))
