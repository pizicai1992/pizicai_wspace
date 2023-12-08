# -*- coding: utf-8 -*-
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层序遍历结果：
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
# 思路：
# 参考：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/python3-er-cha-shu-ceng-xu-bian-li-by-jo-nlx3/
# 使用队列来操作：
# 队列queue 表示的当前在遍历的 层级的节点，遍历这个queue然后组装成一个list 存储到结果集中，
# 继续遍历上述的 queue，将queue中每个节点的 子节点 存储到一个临时队列tmp_queue 中(可以理解为当前层的节点就是上一层的子节点)，
# 将上述的 tmp_queue 赋值给 queue，然后循环上述的步骤继续遍历 queue，
# 循环结束的标志就是 queue 为空，也就是叶子节点没有子节点的时候，正好循环结束。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def so(root:TreeNode):
    if not root: return []
    # 定义变量
    queue = [root] # 当前遍历的层级节点,初始化就开始遍历根节点
    res = [] # 最后返回的结果，是一个list
    # 开始循环
    while queue:
        res.append([node for node in queue]) # 将当前层的节点包装成 list 增加到结果中
        tmp_queue = [] # 一个临时队列，用来存储当前节点的子节点
        for n in queue:
            # 如果左节点不为空，就加入到tmp_queue中
            if n.left:
                tmp_queue.append(n.left)
            # 右节点不为空也加到 tmp_queue 中
            if n.right:
                tmp_queue.append(n.right)
        
        # 最后就把 tmp_queue 更新到 queue 里，继续开始循环
        queue = tmp_queue
    
    return res # 最后返回结果，是一个list，每一个元素也是list，表示各层的节点


