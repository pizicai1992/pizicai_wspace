# -*- coding: utf-8 -*-
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例：

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def solution(l1, l2):
    # dummy 用来返回结果链表的头结点
    # p 是一个中间结果的暂存节点，把每次计算的结果链接起来，然后赋值给dummy ，最后
    # 只要返回dummy的 next 就行了
    dummy = p = ListNode(None)
    s = 0 # 存储中间计算时的结果
    while l1 or l2 or s:
        s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
        p.next = ListNode(s % 10)
        s //= 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next
