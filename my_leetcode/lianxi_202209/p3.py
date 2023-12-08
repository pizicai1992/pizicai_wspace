# -*- coding: utf-8 -*-
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 示例 1:
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

def so(base_str):
    # 使用滑动窗口解法 ,先定义起始位置 结束位置的 下标 
    start = end = 0 
    # 在定义一个 hashMap 用来存储字符的 位置信息，用来判断字符是否重复了 
    hash_map = {}
    # 定义一个变量表示 子串的最大长度 
    max_lenth = 0 
    for i,v in enumerate(base_str):
        # 如果字符在map 里，说明有重复字符 
        if v in hash_map:
            # 第一步从map中取出的value值表示的这个重复字符的上一次位置，往前移动一位也就是+1
            # 第二步 取max 是为了保证start在滑动的过程中不会“倒退”
            # 比如 a b a a b a, 当循环到第三个 a 的时候，此时 start = 第二个a下标 + 1 ，
            # 在往下循环时 b 重复了，这时候如果没有 max ，那么 start = hash_Map[b] + 1 ，
            # 也就是第一个 b 的下标 + 1 ，发现 start 位置倒退了，这明显就不对了 所以要加上 max ，
            # 加上以后 那么 正确的 start 位置应该是 第二个 a 下标 + 1，与实际情况符合 
            start = max(hash_map[v] + 1, start) 
        
        end = i 
        # 存储每次循环时的字符长度，然后max比较大小 
        max_lenth = max(max_lenth, end-start+1) 
        # 更新 hash_map 中的字符的最新位置 
        hash_map[v] = end
    
    return max_lenth


bstr = 'abccbdabebbdfghsdaedf'
print(so(bstr))


