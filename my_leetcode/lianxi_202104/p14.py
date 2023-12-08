# -*- coding: utf-8 -*-
# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:

# 输入: ["flower","flow","flight"]
# 输出: "fl"

# 思路：1. 首先将数组中的单个字符串使用zip函数拼接组装
#      2. 循环上述的结果，将每一个元组转换成set()，然后判断是否有重复值
#      3. 如果没有重复值，就拼接上述结果，否则就停止循环

def so(str_list):
    pre_str = ''
    for i in zip(*str_list):
        if len(set(i)) == 1:
            pre_str += str(i[0])
        else:
            break
    return pre_str

str_list = ["flower","flow","flight"]
print (so(str_list))

# 思路2：
# 另一种方法是纵向扫描。纵向扫描时，从前往后遍历所有字符串的每一列，
# 比较相同列上的字符是否相同，如果相同则继续对下一列进行比较，如果不相同则当前列不再属于公共前缀，当
# 前列之前的部分为最长公共前缀

def max_substr(str_list):
    # 如果输入为空则返回空 
    if not str_list:
        return ''
    
    # 首先需要知道这个数据有多少个元素（多少个字符串），然后就是假定以第一个字符串为标准进行判断
    length = len(str_list[0]) # 第一个字符串的长度，作为外循环的次数（也就是列数）
    str_count = len(str_list) # 字符串的个数，内循环 
    # 外循环从第一列开始判断
    for i in range(length):
        tmp_ss = str_list[0][i]  # 这个变量存储每次循环时（第一个字符串）那一列的值
        # 内循环，从第二个字符串开始 
        for j in range(1, str_count):
            # 判断，如果其他字符串的这一列都相等且不为空，就把这一列对应的元素加到公共子串后面，否则就退出循环
            # 此时公共子串是截止到前一位 ,还有一点要判断这个字符串的长度，也就是是不是最后一列了
            if i == len(str_list[j]) or str_list[j][i] != tmp_ss:
                return str_list[0][:i]
        
    
    return str_list[0]


str_list = ["flower","flow","flight"]
print (max_substr(str_list))


