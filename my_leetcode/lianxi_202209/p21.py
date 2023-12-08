# -*- coding: utf-8 -*-

# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# 思路：
# 需要一个新的头结点用来表示合并后的链表，还需要一个变量表示当前循环到的节点 
# 依次循环两个链表节点进行比较，将值小的节点链接到 当前节点后面，然后让这个节点前进一位，
# 同时当前节点也前进一位

class ListNode(object):
    def __init__(self, x):
        self.val = x 
        self.next = None 


def combine_list(l1:ListNode, l2:ListNode):
    # 初始化一个头结点、一个当前循环的节点 
    head = ListNode(0)
    cur = head

    # 进行循环迭代，结束条件是任何一个链表到尾了就停止 
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2 
            l2 = l2.next
        
        cur = cur.next

    # 循环结束后，还需要把 l1 或者 l2 剩余的部分节点链接到后面
    cur.next = l1 or l2 

    return head.next
