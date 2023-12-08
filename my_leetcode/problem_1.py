# -*- coding: utf-8 -*-
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

def solution(num_list, target_num):
    idx_list = []
    for i,idx in enumerate(num_list[:-1]):
        # print (str(i) + ':' + str(idx))
        # print ('*********************')
        for j,jdx in enumerate(num_list[i+1:]):
            # print (str(i+j+1) + ':' + str(jdx))
            if idx + jdx == target_num:
                idx_list.append((i, i+j+1))
                print ('%d + %d = %d' % (idx, jdx, target_num))
    
    print ('数据下标是： %s' % str(idx_list))

def so2(num_list, target_num):
    # 使用一个dict模拟hashmap，存储数字的索引和值
    hashmap = {}
    for i,num_i in enumerate(num_list):
        hashmap[num_i] = i
    for i,num_i in enumerate(num_list):
        j = hashmap.get(target_num - num_i)
        if j is not None and i != j:
            return [i,j]

def so3(num_list, target_num):
    hashMap = {}
    for i,num in enumerate(num_list):
        if target_num - num in hashMap:
            return [hashMap[target_num-num], i]
        hashMap[num] = i

lista = [1,2,2,4,5,8,4,4,4]
solution(lista, 9)
print (so2(lista, 8))
print (so3(lista, 8))