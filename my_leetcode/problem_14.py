# -*- coding: utf-8 -*-
# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:

# 输入: ["flower","flow","flight"]
# 输出: "fl"

def solution(strs):
    prefix_str = ''
    for i in zip(*strs):
        # print (set(i))
        if len(set(i)) == 1:
            prefix_str += str(i[0])
        else:
            break
    
    return prefix_str


str_list = ["flower","flow","flight"]
print (solution(str_list))