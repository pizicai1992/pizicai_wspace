# -*- coding: utf-8 -*-

# 给你一个字符串 s，找到 s 中最长的回文子串。
# 示例 1：

# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：

# 输入：s = "cbbd"
# 输出："bb"


# 解法1：暴力求解，循环找出所有的子串，然后对这些子串挨个判断是否是回文子串 

from email.mime import base


class solution():
    def __init__(self) -> None:
        pass

    # 判断字符串是否是回文串 
    def is_huiwen(self,strs):
        low = 0 
        high = len(strs) - 1 

        while low < high:
            if strs[low] != strs[high]:
                return False
            
            low = low + 1
            high = high - 1
        
        return True
    
    
    def get_sub(self,base_str):
        huiwen_sub = ""
        max_len = 0 

        for i in range(len(base_str)):
            for j in range(i, len(base_str)):
                # 先判断 子串长度是否大于 已经 找到的最长回文子串的长度，如果不大于那就跳过 
                if j-i+1 <= max_len:
                    continue
                sub_str = base_str[i : j+1]
                if self.is_huiwen(sub_str):
                    max_len = len(sub_str)
                    huiwen_sub = sub_str
        
        return max_len, huiwen_sub


bss = 'abcdeedff'

soo = solution()

print(soo.get_sub(bss))


# 解法2：中心扩散法 


