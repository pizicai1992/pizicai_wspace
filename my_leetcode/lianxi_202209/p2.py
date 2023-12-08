# -*- coding: utf-8 -*-
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例：

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


from curses import noecho


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    

def so(l1: ListNode, l2: ListNode) -> ListNode:
    # dummy 表示最后返回的链表节点 , p 表示中间结果的链接 
    dummy = p = ListNode(0)
    # carry 表示 进位
    carry = 0 
    # 相加的结果值用 mid_val 表示 
    mid_val = 0
    while l1 or l2 or carry:
        # 由于要考虑进位后的余数，所以要加上上一轮的 进位 carry，
        # l1 或者 l2节点不够时用 0 补充
        mid_val = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
        # 中间结果取余
        p.next = ListNode(mid_val % 10)
        # 前进一位
        p = p.next
        # 进位 
        carry = mid_val // 10
        # l1 l2 向前 
        l1 = l1.next if l1 else None 
        l2 = l2.next if l2 else None

    
    return dummy.next





