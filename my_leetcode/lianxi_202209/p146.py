# -*- coding: utf-8 -*-

# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

#  

# 示例：

# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4

# 思路：
# 需要使用数据结构 哈希链表，其中的 KEY 就是缓存的key，而VALUE是一个双链表，并且这个双链表中也需要存储当前的key
# 由于要判断缓存中数据的新旧状态，所以可以默认链表的尾部是最新节点，头部是旧节点
# 当有新数据进入缓存时（缓存容量未满），直接在链表尾部插入节点
# 当有新数据进入缓存时（缓存容量已满），此时需要删除头部的节点，然后在链表尾部插入新节点
# 当查询缓存中数据时，如果存在，返回具体的value值，还要将这个key对应的节点移动到尾部
# 当查询缓存中数据时，如果不存在则返回-1

# 先定义一个双链表类,与之前不同的是这个双链表要包含这个节点对应的key，后面会使用这个key来定位并删除哈希表的数据
# 双链表还包含前驱和后置节点


class ListNode(object):
    def __init__(self, key, val, prenode=None, nextnode = None):
        self.key = key
        self.val = val
        self.prenode = prenode
        self.nextnode = nextnode

# 定义一个哈希链表，KEY就是缓存中的KEY，VALUE就是上述定义的双链表，
# 此外为了方便后续的操作，还需要定义几个操作双链表节点的方法
class DoubleList():
    def __init__(self):
        # 初始化头结点和尾节点，这两个相当于是虚节点
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        # 最开始的时候这个双链表只有头尾节点，所以需要将两个节点连起来
        self.head.nextnode = self.tail
        self.tail.prenode = self.head
        # 还需要初始化一个变量，用来表示这个双链表的节点数（不包括头尾节点）
        self.size = 0
    
    # 在尾部增加一个节点
    def addLast(self, node:ListNode):
        node.nextnode = self.tail
        node.prenode = self.tail.prenode
        self.tail.prenode.nextnode = node
        self.tail.prenode = node
        # 当新增节点时要让双链表的节点数加1
        self.size += 1

    # 删除一个结点,这个方法的目的是当查询缓存时，如果存在相应的KEY，那就需要将这个KEY变为
    # "最新使用的"，做法就是先删除对应的节点，然后将删除的这个节点加到尾部就可以了
    # 调用此方法时默认缓存是存在对应的KEY值的
    def delNode(self, node:ListNode):
        node.prenode.nextnode = node.nextnode
        node.nextnode.prenode = node.prenode
        # 由于是删除节点，此时链表节点数要减去1
        self.size -= 1
    
    # 删除头部节点，如果缓存满了需要腾出位置，此时就删除头部节点,
    # 注意：这儿的头部节点不是head节点，而是head的后置节点-真正的第一个节点，此外还要返回这个节点
    def delHead(self):
        # 判断一下如果链表为空那就返回空
        if self.head.nextnode == self.tail or self.size == 0:
            return None
        # 取出“第一个”节点
        node = self.head.nextnode
        # 直接调用上面定义好的删除节点函数
        self.delNode(node)
        return node

    # 返回当前链表的节点数
    def getSize(self):
        return self.size
    
    # 在封装一个方法，作用是将查询到的节点提升为最近使用的，也就是挪到最后面
    def makeRecent(self, node):
        self.delNode(node)
        self.addLast(node)


# 定义LRUCache类，需要实现其中的get、put方法
class LRUCache():
    def __init__(self, capacity):
        # 定义缓存的大小，是一个int类型的数值
        self.capacity = capacity
        # 在定义一个哈希表，用来存储缓存中数据的映射关系
        self.map = {}
        # 定义缓存数据的类型，其实就是上面定义好的双链表
        self.cache = DoubleList()
    
    # 实现get方法,根据输入的key值查询缓存是否有相应的数据 
    def get(self, key):
        # 如果不在则返回默认的-1
        if key not in self.map:
            return -1
        
        # 如果存在需要返回这个key对应的节点的值
        val = self.map[key].val
        cacheNode = self.map[key]
        # 既然存在，还需要将这个key的缓存数据提升为最近使用的
        self.cache.makeRecent(cacheNode)
        return val
    
    # put方法
    # 如果key存在，则需要更新key的值
    # 如果key不存在且容量未满，则直接插入新的值
    # 如果key不存在且容量已满，则需要删除最久未使用的，然后在插入新数据
    def put(self, key, value):
        new_node = ListNode(key, value)
        if key in self.map:
            # 更新数据，先删除在插入尾部
            self.cache.delNode(self.map[key])
            self.cache.addLast(new_node)
        
        # 判断容量是否满了
        capSize = self.cache.getSize()
        if capSize == self.capacity:
            # 满了就删除头部节点,此处注意不仅要删除链表中的节点，
            # 还需要删除哈希表map中的K-V关系,这也就是链表节点需要存储key的原因
            delnode = self.cache.delHead()
            # 删除哈希表的数据
            self.map.pop(delnode.key)
        # 接下来插入新的节点
        self.cache.addLast(new_node)
        # 哈希表同步插入映射关系
        self.map[key] = new_node




