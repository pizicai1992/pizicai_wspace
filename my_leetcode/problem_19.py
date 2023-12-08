# -*- coding: utf-8 -*-
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 示例：
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.

# 思路：
# 双指针解法，由于要删除的是倒数第N个节点，所以首先快指针先往前走N步，这时候快慢指针在一起向前走，
# 当快指针走到尾部的时候（此时fast.next = None），此时慢指针正好走到了倒数第N个节点的前驱节点，
# 然后慢指针节点的next 指向目标节点的next，这样就删除了目标节点

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def solution(head, n):
    slowNode = ListNode(None)
    slowNode.next = head
    fastNode = slowNode # 次数定义快慢两个指针节点，并且都指向head
    for i in range(n):
        fastNode = fastNode.next # 先让快指针往前走N步
    
    while fastNode:
        slowNode = slowNode.next
        fastNode = fastNode.next # 然后快慢指针同时向前，当快节点到尾部时，慢节点正好到目标节点的前一个节点
    
    if slowNode.next == head:
        head = head.next
    else:
        slowNode.next = slowNode.next.next
    return head
