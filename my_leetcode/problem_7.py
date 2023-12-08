# -*- coding: utf-8 -*-
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

MAX_NUM = 2**31 -1
MIN_NUM = -2**31

def solution(target_num):
    result = 0 
    if target_num>MAX_NUM or target_num<MIN_NUM or target_num == 0:
        return result
    signal = 1
    if target_num < 0:
        signal = -1
    target_num *= signal
    while target_num > 0:
        result = result * 10 + target_num % 10
        target_num = int(target_num / 10)
    
    return result * signal

print (solution(1358473))
