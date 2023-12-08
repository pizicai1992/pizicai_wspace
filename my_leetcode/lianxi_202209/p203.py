# -*- coding: utf-8 -*-

# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

# 思路：
# 要产出链表的一个节点，可以让 这个节点的 上一个节点的next 指向这个节点的下一个节点，相当于断开这个节点 

class ListNode(object):
    def __init__(self, x) -> None:
        self.val = x
        self.next = None 


def del_node(head, value):
    # 初始化，dummy 表示一个虚拟节点，它的next 指向 head,也就是相当于head的前置节点 
    dummy = ListNode(0)
    dummy.next = head 
    # cur 节点表示当前遍历到的节点 
    cur = dummy

    while cur.next:
        # 如果当前节点的下一个节点的值等于value（因为是从前置节点开始遍历的）
        if cur.next.val == value:
            # 此处删除掉对应节点
            cur.next = cur.next.next 

        else:
            # 当前遍历的节点前进一位 
            cur = cur.next
    
    return dummy.next


