# -*- coding: utf-8 -*-
# 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。
# 示例 1：

# 输入: s = "leetcode"
# 输出: 0
# 示例 2:

# 输入: s = "loveleetcode"
# 输出: 2

# 思路：
# 可以使用一个hashmap来存储每个字符出现的次数，然后循环取出并判断每个字符的字数是否等于1
# 以上思路总体是需要循环遍历两次的（2N）

def so(s):
    hashmap={}
    for i in s:
        hashmap[i] = hashmap.get(i, 0)+1
    
    for idx, val in enumerate(s):
        if hashmap[val] == 1:
            return idx
    
    return -1

# ss = "loveleetcode"
ss = 'abcbacd'
print(so(ss))