# -*- coding: utf-8 -*-
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

#思路：使用栈 这个数据结构，循环字符串，遇到左括号就压栈，遇到右括号就跟栈顶的元素比较，是否相等，如果相等就
# 弹出栈顶的元素，如此这般循环比较，最后看这个栈是否是空的，如果是空的说明字符串里的括号都能正确匹配到，如果不是
# 空的，说明这个字符串不满足要求

def so(bracket_str):
    stack = [] # 首先构造一个空的栈
    bracket_dic = {')':'(', ']':'[', '}':'{'}
    if len(bracket_str) % 2 == 1 or len(bracket_str) == 0:
        return False  # 输入的字符串不能为空，字符串长度也不能是奇数
    
    for i in bracket_str:
        if i in bracket_dic and stack: #如果是右括号,就跟栈顶的元素比较，如果能匹配就弹栈
            top_stack = stack[-1]
            if top_stack == bracket_dic[i]:
                stack.pop()
        else:
            stack.append(i) # 如果是左括号，就压栈
    
    if len(stack) == 0: #如果最后栈是空的，说明输入的字符串符合要求
        return True
    else:
        return False

ts = ']]'
print(so(ts))
