# -*- coding: utf-8 -*-
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

#思路：使用栈 这个数据结构，循环字符串，遇到左括号就压栈，遇到右括号就跟栈顶的元素比较，是否相等，如果相等就
# 弹出栈顶的元素，如此这般循环比较，最后看这个栈是否是空的，如果是空的说明字符串里的括号都能正确匹配到，如果不是
# 空的，说明这个字符串不满足要求

def solution(bracket_str):
    stack = []
    bracket_dic = {')':'(', ']':'[', '}':'{'}
    if len(bracket_str) % 2 == 1 or len(bracket_str) == 0:
        return False
    for i in bracket_str:
        if i in bracket_dic:
            top_element = stack[-1]
            if top_element == bracket_dic[i]:
                stack.pop()
        else:
            stack.append(i)
    
    print (stack)
    if len(stack) == 0 :
        return True
    else:
        return False
        
bra_str = '((([]))]'
print (solution(bra_str))