# -*- coding: utf-8 -*-

# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

# 思路：
# 可以用除法取余，由于是十进制，所以先除以10，第一次的余数就是 反转后的最高位


def reverse_num(num):
    MAX_VAL = 2 ** 31-1
    MIN_VAL = -2 ** 31

    if num < MIN_VAL or num > MAX_VAL:
        return 0 

    #定义一个变量用来标记原数字是正还是负，如果是负数还需要把它变成正数，这样好处理 
    flag = 1

    # 定义一个变量用来存储最终结果 
    result = 0

    if num < 0:
        flag = -1
    
    num = num * flag

    while num > 0 :
        result = result*10 + num % 10 #上次的结果 * 10，在加上本次的余数 
        num = num // 10  # 每次循环让原数字都除以10 并取整
    
    return result


base_num = 1546
print(reverse_num(base_num))



