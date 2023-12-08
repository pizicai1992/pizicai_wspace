# -*- coding: utf-8 -*-
# 反转一个单链表。

# 示例:
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

# 思路：
# 要将链表 1 -> 2 -> 3 -> 4 -> Null 反转为 4 -> 3 -> 2 -> 1 -> Null ，
# 需要一个 cur 指针表示当前遍历到的节点；一个 pre 指针表示当前节点的前驱节点；
# 在循环中还需要一个中间变量 temp 来保存当前节点的后驱节点。

# 算法流程：
# 首先 pre 指针指向 Null，cur 指针指向 head；
# 当 cur != Null，执行循环。
# 先将 cur.next 保存在 temp 中防止链表丢失：temp = cur.next
# 接着把 cur.next 指向前驱节点 pre：cur.next = pre
# 然后将 pre 往后移一位也就是移到当前 cur 的位置：pre = cur
# 最后把 cur 也往后移一位也就是 temp 的位置：cur = temp
# 当 cur == Null，结束循环，返回 pre。

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def so(head:ListNode):
    pre = None # 初始化前驱节点，最后返回前驱节点
    cur = head  # 初始化当前节点
    if head is None or head.next is None:  # 兼容leetcode特殊用例，链表为空或只有1个节点
        return head
    
    while cur:
        tmp = cur.next # 先将当前的后驱节点保存到临时变量
        # 开始交换
        cur.next = pre # 当前节点的后驱节点指向前驱节点
        # 循环前进
        pre = cur # 前驱节点前进一位，也就是到当前节点位置
        cur = tmp # 当前节点也前进一位，也就是原先的后驱节点位置
    
    return pre



