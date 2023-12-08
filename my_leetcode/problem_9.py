# -*- coding: utf-8 -*-
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# 思路:
# 通过取整和取余操作获取整数中对应的数字进行比较。

# 举个例子：1221 这个数字。

# 通过计算 1221 / 1000， 得首位1
# 通过计算 1221 % 10， 可得末位 1
# 进行比较
# 再将 22 取出来继续比较

def solution(target_num):
    # result = True
    if target_num < 0:
        return False
    div = 1 # 初始化除数 
    while target_num / div >= 10:
        div *= 10  # 求出第一次操作的除数,比如要判断12121，则第一次应该除以10000
    
    while target_num > 0:
        left = int(target_num / div)
        right = target_num % 10
        print ('left:%d, right:%d' % (left, right))
        if left != right:
            # print ('不等')
            return False
        target_num = int((target_num % div) / 10)
        print ('target_num: ', target_num)
        div /= 100
    return True

tg_num = 10201

if solution(tg_num):
    print ('%d 是回文数' % tg_num)
else:
    print ('%d 不是回文数' % tg_num)