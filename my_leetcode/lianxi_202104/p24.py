# -*- coding: utf-8 -*-
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 示例:
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 思路：


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def so(head: ListNode):
    dummy = ListNode(-1)  # 定义一个虚拟节点,最后返回的也是这个虚拟节点
    dummy.next = head     # 虚拟节点指向头节点
    prenode = dummy       # 这个表示需要交换的两个节点中的第一个节点的前置节点
    while head and head.next:
        first = head
        second = head.next # 定义需要交换的两个节点
        # 下面开始交换
        prenode.next = second # 前置节点的后置需要指向原先第二个节点
        first.next = second.next  #原先第一个节点的后置需要指向原先第二个节点的后置
        second.next = first #原先第二个节点的后置指向第一个节点
        # 为下一次循环做准备
        prenode = first
        head = first.next
    
    return dummy.next
