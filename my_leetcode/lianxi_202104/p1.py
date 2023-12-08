# -*- coding: utf-8 -*-
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

def so(num_list, target_num):
    # 先构造一个hashmap，存储索引和值
    hashMap = {}
    for i,num in enumerate(num_list):
        if target_num - num in hashMap:
            return [hashMap[target_num-num], i]
        hashMap[num] = i

lista = [1,2,2,4,5,8,4,4,4]
print (so(lista, 4))


def so2(base_arr, trg_num):
    idx_list = []
    for i, v1 in enumerate(base_arr[:-1]):
        for j, v2 in enumerate(base_arr[i+1:]):
            if v1 + v2 == trg_num:
                idx_list.append((i, i+j+1))
                break
    
    return idx_list


print (so2(lista, 4))

            

