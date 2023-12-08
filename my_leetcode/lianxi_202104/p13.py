# -*- coding: utf-8 -*-
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，
# 所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

def so(rome_num):
    rome_dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} # 使用字典表示罗马数字与整数的对应关系
    if len(rome_num) == 1:
        return rome_dic[rome_num]
    result = 0 # 用来存储返回的整数值
    for idx in range(len(rome_num) - 1): # 此处只需要循环到倒数第二位
        if rome_dic[rome_num[idx]] < rome_dic[rome_num[idx + 1]]: #判断当前数字与下一位的大小,如果右面的大，就减去当前值
            result -= rome_dic[rome_num[idx]]
        else:
            result += rome_dic[rome_num[idx]] # 如果右面的小，就加上当前的值
    result += rome_dic[rome_num[-1]] # 循环时没有计算最后一位，此处要加上
    return result


