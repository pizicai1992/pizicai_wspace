# -*- coding: utf-8 -*-
# 二分查找
# 1. 循环思路
# 定义两个变量表示头尾的位置，还要一个变量表示中间位置，然后判断中间位置的变量与目标变量的大小
# 根据具体的大小调整头尾的位置，最终循环结束的条件就是当头元素位置大于了尾元素位置

def erfen_xunhuan(nums, trg):
    start = 0
    end = len(nums)-1
    mid = 0
    while start <= end:
        mid = (start+end) // 2
        if trg == nums[mid]:
            return mid
        elif trg < nums[mid]:
            end = mid-1
        else:
            start = mid+1
    
    return -1

numms = [1,3,4,6,8,9,23,34,55,56,67]
tt = 2
print(erfen_xunhuan(numms, tt))


# 2. 递归思路

def erfen_digui(nums, trg, start, end):
    while start <= end:
        mid = (start+end) // 2
        if trg == nums[mid]:
            return mid
        elif trg < nums[mid]:
            return erfen_digui(nums, trg, start, mid-1)
        else:
            return erfen_digui(nums, trg, mid+1, end)
    
    return -1

print(erfen_digui(numms, 9, 0, len(numms)-1))


