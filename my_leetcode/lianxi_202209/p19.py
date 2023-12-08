# -*- coding: utf-8 -*-
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# 思路：
# 核心思路就是准确找到这个节点的位置 
# 使用快慢两个指针，先让快指针往前移动 n 个位置，然后快慢指针同时开始移动 
# 当快指针移动到结尾，也就是快指针对应的节点的next 是None的时候，慢指针节点刚好
# 是目标节点的 前置 节点，这时候就可以执行删除操作了，也就是慢节点的 next 指向 慢节点的next.next 

class ListNode(object):
    def __init__(self, x):
        self.value = x 
        self.next = None 



def del_node(head:ListNode, n):
    # 先初始化快慢两个指针 
    dummy = ListNode(0)
    dummy.next = head 
    slow = dummy
    fast = dummy 

    # 先让快节点往前走 n 步
    for i in range(n):
        fast = fast.next
    
    while fast:
        fast = fast.next
        slow = slow.next
    
    if slow.next == head:
        head = head.next
    else:
        slow.next = slow.next.next
    

    return head


