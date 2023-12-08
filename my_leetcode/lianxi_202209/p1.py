# -*- coding: utf-8 -*-
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。


def so(base_arr, trg_num):
    if len(base_arr) < 1:
        return None 
    
    # 构造一个字典模拟hashMap，存储数组的元素（字典KEY）与下标（字典VALUE），好处是可以快速查找 
    hashMap = {}
    idx_list = []  # 存放最后的结果

    # 单次的fou循环，减少时间复杂度,enumerate可以同时取出下标 与 元素值
    for k, v in enumerate(base_arr):
        num1 = trg_num - v # 由于for循环已经取出了第一个加数，这时只需要判断第二个加数是否在字典中
        if num1 in hashMap:
            # 如果找到了直接返回，停止循环
            idx_list.append(k)
            idx_list.append(hashMap[num1])
            break
        else:
            # 如果没找到就将当前循环到的元素和下标存进这个字典里面
            hashMap[v] = k 
    
    return idx_list


ba = [6,4,8,1,3] 
tg = 5 

print(so(ba, tg))
