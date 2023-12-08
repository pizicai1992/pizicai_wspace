# -*- coding: utf-8 -*-
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# 示例：

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def solution(l1, l2):
    head = cur = ListNode(0)
    while l1 and l2:
        if l1.val > l2.val:
            cur.next = l2
            l2 = l2.next
        else:
            cur.next = l1
            l1 = l1.next
        cur = cur.next
    cur.next = l1 or l2
    return head.next