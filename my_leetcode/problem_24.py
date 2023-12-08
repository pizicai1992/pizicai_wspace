# -*- coding: utf-8 -*-
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 示例:
# 给定 1->2->3->4, 你应该返回 2->1->4->3.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def solution(head: ListNode):
    # 定义一个虚拟节点
    dummy = ListNode(-1)
    dummy.next = head
    prev_node = dummy  # 交换节点中的第一个节点的前驱节点
    while head and head.next:
        # 交换节点定义
        first_node = head
        second_node = head.next
        # 开始交换
        prev_node.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node
        # 为下一次交换重新初始化head和prev节点
        prev_node = first_node
        head = first_node.next
    return dummy.next
