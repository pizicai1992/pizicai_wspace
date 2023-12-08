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

def so(head, n):
    slow = ListNode(None)
    slow.next = head
    fast = slow #初始化快慢两个指针
    for i in range(n):
        fast = fast.next # 先让快指针向前走 n 步

    while fast:
        slow = slow.next
        fast = fast.next # 快慢指针同时向前走，当快指针走到末尾时停止

    if slow.next == head:
        head = head.next
    else:
        slow.next = slow.next.next
    
    return head 
