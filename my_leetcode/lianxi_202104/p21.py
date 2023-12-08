# -*- coding: utf-8 -*-
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# 示例：

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def so(l1, l2):
    head = cur = ListNode(0)  # 初始化,head表示头节点，最后返回的也是头节点，cur表示当前节点，存储临时变量
    while l1 and l2:  # 当任何一个链表到尾部时停止循环
        if l1.val >= l2.val:
            cur.next = l2 # 比较两个链表的节点的值，将小的拼接到后面，对应的节点也前进一位
            l2 = l2.next
        else:
            cur.next = l1
            l1 = l1.next
        cur = cur.next # 当前节点往前一位
    
    cur.next = l1 or l2 # 对于长出来的部分直接拼接到后面

    return head.next

