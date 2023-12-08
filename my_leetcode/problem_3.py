# -*- coding: utf-8 -*-
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 示例 1:
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

def solution(s):
    substr = set() # 存储子串的集合
    right = 0 #子串的右终止位置
    substr_length = 0 # 子串的长度
    for left in range(len(s)):
        while right < len(s) and s[right] not in substr:
            substr.add(s[right])
            right += 1
        if len(substr) > substr_length:
            substr_length = len(substr)
        print (substr)
        substr.remove(s[left])
        print (left)
        print (substr)
        print ('*' * 10)
    # print (str(substr))
    return substr_length

ss = 'pwwkew'
print (solution(ss))