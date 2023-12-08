# -*- coding: utf-8 -*-

# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# 思路：
# 1. 需要一个 pre 节点表示当前节点的前置节点、需要一个 cur 节点表示当前循环到的 节点、
#    还需要一个 tmp 节点表示当前节点的 后置节点 
# 2. 开始交换，先将当前节点的后置节点 cur.next 赋值给 tmp，防止数据丢失 
# 3. 接下来将 当前节点的后置节点 指向到 前置节点上 cur.next = pre 
# 4. 将前置节点 后移 一位（移动到当前节点），在将 当前节点也后移一位（移动到原先的后置节点位置）

class ListNode(object):
    def __init__(self, x) -> None:
        self.val = x
        self.next = None 


def so(head: ListNode):
    # 初始化前置节点 
    pre = None 
    # 初始化当前节点，当前节点等于头结点
    cur = head 

    while cur:
        tmp = cur.next 
        cur.next = pre 
        pre = cur 
        cur = tmp 
    
    return pre 
